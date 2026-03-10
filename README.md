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
- 6–8 variables derived from Gardner's Multiple Intelligences dimensions
  and socioemotional indicators
- K-Means clustering to identify natural learning profiles
- 2–3 pedagogical recommendations per identified profile
- Interactive dashboard for results visualization

---

## Project Structure
```
learning-profile-analysis/
├── dashboard/          # Interactive dashboard
├── data/               # Synthetic dataset
├── docs/               # References and documentation
├── notebooks/          # Jupyter notebooks (EDA, modeling, results)
├── docker-compose.yml
├── Dockerfile
├── READM.md
└── requirements.txt
```

---

## Getting Started

### Requirements
- Docker
- Docker Compose

### Run with Docker
```bash
git clone https://github.com/your-username/learning-profile-analysis.git
cd learning-profile-analysis
docker-compose up notebook
```

Open your browser at: `http://localhost:8888`

---

## Tech Stack

- Python 3.11
- Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook
- Streamlit

---

## Theoretical Foundation

- Gardner, H. *Frames of Mind: The Theory of Multiple Intelligences*. Basic Books, 1983.
- Socioemotional learning indicators as referenced by Instituto Criativo.

---

## Author

Vinícius Wenz dos Santos  
Bachelor's Degree in Data Science — XP Educação  
[LinkedIn](https://www.linkedin.com/in/vinicius-wenz-dos-santos/) · [GitHub](https://github.com/viniwenz)