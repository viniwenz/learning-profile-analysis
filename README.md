# Learning Profile Analysis

A data science project that classifies children's learning profiles
using unsupervised machine learning, based on Howard Gardner's
Theory of Multiple Intelligences.

Developed as part of the Applied Project for the Bachelor's Degree
in Data Science at XP Educação (2026), in partnership with
Instituto Criativo.

---

## Problem Statement

How can we use data to identify a child's learning profile
and recommend personalized pedagogical strategies?

Teachers often have valuable information about their students
but lack accessible tools to transform that data into structured
diagnoses. This project aims to bridge that gap.

---

## Solution Overview

- Synthetic dataset with 100–150 records based on scientific literature
- 8 variables derived from Gardner's Multiple Intelligences dimensions
  and socioemotional indicators
- K-Means clustering to identify natural learning profiles
- 2–3 pedagogical recommendations per identified profile
- Interactive dashboard for results visualization

---

## Project Structure
```
learning-profile-analysis/
├── .devcontainer/      # Dev Container configuration
├── dashboard/          # Interactive dashboard
├── data/               # Synthetic dataset and EDA outputs
├── docs/               # References and documentation
├── notebooks/          # Jupyter notebooks (EDA, modeling, results)
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## Getting Started

### Requirements
- Docker
- Docker Compose

### Option 1 — Docker (run notebooks in browser)
```bash
git clone https://github.com/viniwenz/learning-profile-analysis.git
cd learning-profile-analysis
docker-compose up notebook
```

Open your browser at: `http://localhost:8888`

### Option 2 — Dev Container (recommended for development)

Open the project in VSCode and run:
```
Ctrl+Shift+P → Dev Containers: Reopen in Container
```

VSCode will open the project inside the container with Python 3.11
and all dependencies pre-installed.

---

## Execution Order

Before running the dashboard, execute the notebooks in order:

1. `notebooks/01_exploratory_analysis.ipynb` — generates `data/synthetic_dataset.csv`
2. `notebooks/02_modeling.ipynb` — generates `data/dataset_dashboard.csv`
3. `notebooks/03_dashboard.ipynb` — generates `data/recommendations.csv`

---

### Run the dashboard
```bash
streamlit dashboard/run app.py --server.address=0.0.0.0 --server.port=8501
```

Open your browser at: `http://localhost:8501`

---

## Using Real Data

This project supports two modes:

| Mode | How to activate |
|---|---|
| **Synthetic (default)** | Just run the notebook as-is |
| **Real data** | Place a CSV named `real_data.csv` inside `data/` with the same column names. The notebook will detect it automatically. |

Expected columns:
```
student_name, linguistic_score, logical_math_score, spatial_score,
bodily_kinesthetic_score, interpersonal_score, intrapersonal_score,
emotional_regulation, engagement_frequency
```
All score columns must be numeric values between 0 and 10.

## Tech Stack

- Python 3.11
- Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook
- Streamlit

---

## Theoretical Foundation

- Gardner, H. *Frames of Mind: The Theory of Multiple Intelligences*. Basic Books, 1983.
- CASEL. *SEL Framework*. Collaborative for Academic, Social, and Emotional Learning, 2020.
- Fredricks, J. A.; Blumenfeld, P. C.; Paris, A. H. School engagement. *Review of Educational Research*, 2004.

---

## Author

Vinícius Wenz dos Santos
Bachelor's Degree in Data Science — XP Educação
[LinkedIn](https://www.linkedin.com/in/vinicius-wenz-dos-santos/) · [GitHub](https://github.com/viniwenz)