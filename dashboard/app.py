import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import numpy as np
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Análise de Perfil de Aprendizado",
    page_icon="https://institutocriativo.com.br/assets/instituto_criativo_logo-CfKDAQNn.png",
    layout="wide",
)

# ── Constants ─────────────────────────────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/dataset_dashboard.csv")
REC_PATH  = os.path.join(BASE_DIR, "../data/recommendations.csv")

PROFILE_COLORS = {
    "Analytical":    "#D85A30",
    "Communicative": "#378ADD",
    "Kinesthetic":   "#1D9E75",
    "Balanced":      "#888780",
}

SCORE_COLUMNS = [
    "linguistic_score",
    "logical_math_score",
    "spatial_score",
    "bodily_kinesthetic_score",
    "interpersonal_score",
    "intrapersonal_score",
    "emotional_regulation",
    "engagement_frequency",
]

SCORE_LABELS = {
    "linguistic_score":         "Linguistic",
    "logical_math_score":       "Logical-Math",
    "spatial_score":            "Spatial",
    "bodily_kinesthetic_score": "Bodily-Kinesthetic",
    "interpersonal_score":      "Interpersonal",
    "intrapersonal_score":      "Intrapersonal",
    "emotional_regulation":     "Emotional Regulation",
    "engagement_frequency":     "Engagement",
}

# ── Data loading ──────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df  = pd.read_csv(DATA_PATH)
    rec = pd.read_csv(REC_PATH)
    return df, rec

# ── Sidebar ───────────────────────────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        st.title("Análise de Perfil de Aprendizado")
        st.caption("Instituto Criativo · XP Educação · 2026")
        page = st.radio(
            "Navegação",
            ["Visão Geral da Turma", "Perfil do Aluno", "Recomendações"],
            label_visibility="collapsed",
        )
        st.caption(
            "Baseado na Teoria das Inteligências Múltiplas de Gardner (1983) "
            "e indicadores socioemocionais."
        )
    return page

# ── Page 1 — Class Overview ───────────────────────────────────────────────────
def page_class_overview(df):
    st.header("Visão Geral da Turma")
    st.caption(f"Dataset: {len(df)} alunos · {df['profile'].nunique()} perfis de aprendizado identificados")
    st.divider()

    # ── Metric cards
    cols = st.columns(4)
    for i, profile in enumerate(["Analytical", "Communicative", "Kinesthetic", "Balanced"]):
        count = len(df[df["profile"] == profile])
        pct   = count / len(df) * 100
        with cols[i]:
            st.metric(
                label=profile,
                value=count,
                delta=f"{pct:.0f}% da turma",
            )

    st.divider()
    col1, col2 = st.columns(2)

    # ── Bar chart — profile distribution
    with col1:
        st.subheader("Distribuição dos Perfis")
        dist = df["profile"].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        bars = ax.barh(
            dist.index,
            dist.values,
            color=[PROFILE_COLORS.get(p, "#ccc") for p in dist.index],
        )
        for bar, val in zip(bars, dist.values):
            ax.text(val + 0.3, bar.get_y() + bar.get_height() / 2,
                    str(val), va="center", fontsize=10)
        ax.set_xlabel("Número de alunos")
        ax.set_xlim(0, dist.values.max() + 6)
        sns.despine(ax=ax)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # ── Radar chart — mean scores per profile
    with col2:
        st.subheader("Médias por Perfil")
        labels  = list(SCORE_LABELS.values())
        N       = len(labels)
        angles  = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(6, 5), subplot_kw=dict(polar=True))
        for profile, color in PROFILE_COLORS.items():
            means  = df[df["profile"] == profile][SCORE_COLUMNS].mean().tolist()
            means += means[:1]
            ax.plot(angles, means, linewidth=2, color=color, label=profile)
            ax.fill(angles, means, alpha=0.08, color=color)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, size=8)
        ax.set_ylim(4, 10)
        ax.set_yticks([5, 6, 7, 8, 9, 10])
        ax.set_yticklabels(["5","6","7","8","9","10"], size=7)
        ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.1), fontsize=9)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # ── Heatmap — cluster profiles
    st.subheader("Médias por Perfil - Heatmap")
    cluster_means = (
        df.groupby("profile")[SCORE_COLUMNS]
        .mean()
        .rename(columns=SCORE_LABELS)
        .round(2)
    )
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.heatmap(
        cluster_means,
        annot=True, fmt=".2f",
        cmap="YlOrRd",
        vmin=4, vmax=10,
        linewidths=0.5,
        ax=ax,
    )
    ax.set_ylabel("Perfil")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()


# ── Page 2 — Student Profile ──────────────────────────────────────────────────
def page_student_profile(df, rec):
    st.header("Perfil do Aluno")
    st.divider()

    col_sel, col_info = st.columns([1, 2])
    with col_sel:
        student_name = st.selectbox(
            "Selecionar aluno",
            sorted(df["student_name"].tolist()),
        )

    student = df[df["student_name"] == student_name].iloc[0]
    profile  = student["profile"]
    color    = PROFILE_COLORS.get(profile, "#ccc")

    with col_info:
        st.metric(label="Perfil de Aprendizado", value=profile)

    # ── Recommendations ───────────────────────────────────────────────────────
    st.divider()
    st.subheader("Recomendações Pedagógicas")
    profile_recs = rec[rec["profile"] == profile].reset_index(drop=True)

    for _, row in profile_recs.iterrows():
        with st.container(border=True):
            st.write(row["recommendation"])
            st.caption(f"{row['source']}")

    # ── Charts ────────────────────────────────────────────────────────────────
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Scores vs Média da Turma")
        labels       = list(SCORE_LABELS.values())
        student_vals = [student[c] for c in SCORE_COLUMNS]
        class_means  = df[SCORE_COLUMNS].mean().tolist()

        x   = np.arange(len(labels))
        w   = 0.35
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.bar(x - w/2, student_vals, w, label=student_name, color=color, alpha=0.85)
        ax.bar(x + w/2, class_means,  w, label="Class mean",  color="#ccc", alpha=0.85)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=9)
        ax.set_ylim(0, 11)
        ax.set_ylabel("Score (0–10)")
        ax.legend(fontsize=9)
        sns.despine(ax=ax)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Radar Individual")
        labels  = list(SCORE_LABELS.values())
        N       = len(labels)
        angles  = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]
        vals    = [student[c] for c in SCORE_COLUMNS]
        vals   += vals[:1]

        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
        ax.plot(angles, vals, linewidth=2, color=color)
        ax.fill(angles, vals, alpha=0.15, color=color)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, size=8)
        ax.set_ylim(4, 10)
        ax.set_yticks([5, 6, 7, 8, 9, 10])
        ax.set_yticklabels(["5","6","7","8","9","10"], size=7)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # ── Score table ───────────────────────────────────────────────────────────
    st.subheader("Detalhamento dos Scores")
    score_table = pd.DataFrame({
        "Dimensão":  labels,
        student_name: [round(student[c], 1) for c in SCORE_COLUMNS],
        "Média da Turma": [round(df[c].mean(), 1) for c in SCORE_COLUMNS],
        "Diferença": [round(student[c] - df[c].mean(), 1) for c in SCORE_COLUMNS],
    })
    st.dataframe(score_table, use_container_width=True, hide_index=True)

# ── Page 3 — Recommendations ──────────────────────────────────────────────────
def page_recommendations(df, rec):
    st.header("Recomendações Pedagógicas")
    st.caption("Recomendações derivadas de Gardner (1983), Armstrong (2001), Antunes (1998), CASEL (2020) e MEC/SEESP.")
    st.divider()

    selected_profile = st.selectbox(
        "Selecionar Perfil",
        ["Analytical", "Communicative", "Kinesthetic", "Balanced"],
    )

    color   = PROFILE_COLORS[selected_profile]
    profile_recs = rec[rec["profile"] == selected_profile].reset_index(drop=True)

    st.markdown(
        f"""
        <div style='background:#f8f9fa;border-radius:8px;padding:1rem;
                    border-left:4px solid {color};margin-bottom:1rem'>
            <p style='margin:0;font-size:18px;font-weight:600;color:{color}'>
                {selected_profile} Profile
            </p>
            <p style='margin:0;font-size:13px;color:#666'>
                {len(df[df["profile"]==selected_profile])} alunos neste perfil
                ({len(df[df["profile"]==selected_profile])/len(df)*100:.0f}% da turma)
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for _, row in profile_recs.iterrows():
        with st.container(border=True):
            st.write(row["recommendation"])
            st.caption(f"{row['source']}")

    st.divider()
    st.subheader("Alunos neste perfil")
    students = df[df["profile"] == selected_profile][
        ["student_name"] + SCORE_COLUMNS
    ].rename(columns=SCORE_LABELS).round(1)
    st.dataframe(students, use_container_width=True, hide_index=True)

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    matplotlib.use("Agg")
    sns.set_theme(style="whitegrid", palette="muted")

    try:
        df, rec = load_data()
    except FileNotFoundError:
        st.error(
            "Dataset not found. Run `notebooks/02_modeling.ipynb` first "
            "to generate `data/dataset_dashboard.csv`."
        )
        st.stop()

    page = render_sidebar()

    if page == "Visão Geral da Turma":
        page_class_overview(df)
    elif page == "Perfil do Aluno":
        page_student_profile(df, rec)
    elif page == "Recomendações":
        page_recommendations(df, rec)

if __name__ == "__main__":
    main()
    