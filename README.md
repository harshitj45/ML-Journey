<div align="center">

# 🤖 ML Journey — Harshit

### From Python Fundamentals to Junior ML Engineer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-In%20Progress-F7931E?logo=scikitlearn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Progress](https://img.shields.io/badge/Progress-Week%207%20of%2016-yellow)

</div>

---

## 👋 About Me

I'm **Harshit**, a final-year (4th year) B.Tech CSE student at **TMU Moradabad**, graduating in 2027. I'm building this repository as a public, day-by-day record of my transition from software fundamentals into Machine Learning — with the goal of working as a **Junior ML Engineer** (or AI/GenAI Engineer — see note below) at a product-focused startup.

I built this repo on one rule: **understand the concept before moving to the next one.** Every algorithm and data structure here was implemented from scratch before I touched the library version of it — so when I use `sklearn` or `PyTorch`, I know exactly what's happening underneath.

---

## 🎯 Goal

Land a **Junior ML Engineer / AI Engineer** role at a product startup — India-based or remote — by building genuine depth in Python, mathematics for ML, and core machine learning, rather than skipping straight to frameworks.

> **A second repository** covering Applied AI Engineering (LLMs, RAG, LangChain, AI Agents, deployment) will follow once this roadmap is complete — this repo stays focused on classical ML fundamentals done properly.

---

## 📊 Progress Tracker

| Phase | Topic | Status | Programs |
|---|---|---|---|
| **Week 1** | Python Fundamentals | ✅ Complete | 18 programs + 1 project |
| **Week 2** | Functions, OOP, Exceptions & File I/O | ✅ Complete | 21 programs |
| **Week 3** | Advanced Python + Maths Intro | ✅ Complete | 21 programs |
| **Week 4** | Maths for ML + NumPy Deep Dive | ✅ Complete | 33 programs |
| **Week 5** | Pandas | ✅ Complete | 31 programs |
| **Week 6** | Data Visualization (Matplotlib/Seaborn) + EDA Framework | ✅ Complete | 9 programs |
| **Project 1** | Olist E-Commerce Customer Satisfaction EDA | ✅ Complete | Full real-dataset project |
| **Week 7** | Core ML (Scikit-learn) — sklearn API, preprocessing, Logistic Regression | 🔄 In Progress | 6 programs so far |
| Upcoming | Precision/Recall/F1, Regularization, Cross-Validation | ⏳ Planned | - |
| Upcoming | Decision Trees, Random Forest, Ensembles | ⏳ Planned | - |
| Upcoming | **Project 2** — Deployed Classification Pipeline | ⏳ Planned | - |
| Upcoming | NLP + Deep Learning (PyTorch, HuggingFace) | ⏳ Planned | - |
| Upcoming | **Project 3** — Deployed NLP App | ⏳ Planned | - |
| Upcoming | DSA + SQL | ⏳ Planned | - |
| Upcoming | Deployment (FastAPI, Docker) + **Project 4** | ⏳ Planned | - |

**139 hands-on programs written and pushed so far**, across 6 completed weeks, plus one full real-dataset project.

---

## 🗂 Repository Structure

```text
ML-Journey/
│
├── python/ → Week 1: Python Fundamentals
├── Week-2-python/ → Week 2: OOP, Exceptions & File I/O
├── Week-3-Python/ → Week 3: Advanced Python + Maths Intro
├── Week-4-python+numpy/ → Week 4: Maths for ML + NumPy Deep Dive
├── Week-5-pandas/ → Week 5: Pandas
├── Week-6-visualization-eda/ → Week 6: Matplotlib, Seaborn, EDA Framework
├── day46_project1/ → Project 1: Olist E-Commerce EDA
├── Week-7-core-ml/ → Week 7: Scikit-learn (in progress)
├── Project/
│ └── Student grade management system/ → Week 1 milestone project
├── .gitattributes
├── .gitignore
└── README.md
```

Each week's folder contains that week's daily programs. Raw datasets (CSV files) are excluded via `.gitignore` — see each project's own README for the data source and how to obtain it.

---

## 🏗️ Milestone Projects

### 1. Student Grade Management System (Week 1)
Menu-driven CLI app for tracking and analyzing student grades. **Concepts:** loops, dictionaries, comprehensions, functions.

### 2. Student Record System (Week 2)
A `Person → Student/Teacher` system built on an abstract base class, with `@property`-validated fields and full file persistence. **Concepts:** OOP, inheritance, abstract classes, custom exceptions, file I/O.

### 3. ML Data Pipeline Toolkit (Week 3)
A batch-processing pipeline combining a custom decorator, a generator-based batch loader, a context manager for run-timing, and NumPy matrix operations. **Concepts:** decorators, generators, context managers, NumPy.

### 4. Linear Regression from Scratch (Week 4)
A multi-feature linear regression model trained with gradient descent, using the same `fit()`/`predict()`/`score()` interface as Scikit-learn. **Concepts:** linear algebra, calculus, statistics, OOP.

### 5. E-Commerce Sales Pipeline (Week 5)
A realistic messy-data pipeline: two raw tables with duplicates, missing values, and outliers — cleaned, merged, and analyzed into business insights. **Concepts:** Pandas cleaning, merging, groupby, time series.

### 6. Project 1 — Olist E-Commerce Customer Satisfaction EDA 🌟
A full 8-step EDA on a real 99K-order Brazilian e-commerce dataset (orders + reviews). Engineered delivery-delay features, merged datasets, and found that **1-star orders are 19x more likely to be late** than 5-star orders (36.6% vs 1.9%) — a signal the raw mean delay masked due to outlier skew. Also found the review-text subset skews toward negative, longer reviews, and is written in Portuguese, which will shape the NLP project later.
**Concepts:** feature engineering, merge/groupby, outlier-robust analysis, hypothesis testing, data storytelling.
📁 [`day46_project1/`](./day46_project1) — full README with all findings inside.

---

## 🧭 Project Standard Going Forward

Every project from here on is built as a **live, testable product** — a small FastAPI wrapper with a public URL wherever feasible — not left as a notebook-only analysis. **Project 2 (Core ML) is the first to follow this fully**, rather than saving deployment for the final project alone. The reasoning: with a portfolio that needs to carry more weight than a transcript, something a recruiter can actually click and test beats a notebook they have to run themselves.

---

## 🧠 Skills Demonstrated

**Python (Advanced)**
`OOP & Inheritance` `Abstract Classes` `Decorators` `Generators/Iterators` `Context Managers` `Type Hints` `Custom Exceptions`

**Mathematics for ML**
`Linear Algebra` `Statistics & Probability` `Bayes' Theorem` `Hypothesis Testing` `Calculus (Gradient Descent)`

**Data Engineering (Pandas)**
`Cleaning (missing values, outliers, duplicates)` `Merging & Joins` `GroupBy/Pivot` `Time Series` `String Processing`

**Data Visualization & EDA**
`Matplotlib` `Seaborn` `Structured 8-Step EDA Framework` `Feature Hypothesis Testing`

**Core ML (in progress)**
`Scikit-learn API` `train_test_split` `Preprocessing (Scaling, Encoding)` `ColumnTransformer` `Logistic Regression` `Confusion Matrix Evaluation`

**Engineering Practice**
Every concept implemented from first principles before using the library version — including a from-scratch Naive Bayes classifier and a from-scratch gradient-descent Linear Regression.

---

## 🛠 Tech Stack

**Currently using:** `Python` `NumPy` `SciPy` `Pandas` `Matplotlib` `Seaborn` `Scikit-learn`

**Coming up:** `XGBoost` `PyTorch` `HuggingFace` `FastAPI` `Docker`

---

## 📚 Learning Philosophy

- No topic is copy-pasted — every program is written and understood before moving forward.
- Every mini-project combines everything learned that week, rather than testing concepts in isolation.
- Projects use real, non-cliché datasets (no Titanic/Iris/MNIST) — messy, real-world data with genuine findings.
- From Project 2 onward, projects are built as live, deployed products, not just notebooks.
- Each phase ends with active recall — explaining concepts from memory, without notes — before starting the next one.

---

## 🔭 Roadmap Ahead

Week 7 → Core ML: Scikit-learn (in progress)
Week 8-9 → Evaluation Metrics, Regularization, Ensembles + Project 2 (deployed)
Week 10-13 → NLP + Deep Learning (PyTorch, HuggingFace) + Project 3 (deployed)
Week 14-15 → DSA + SQL
Week 16 → Deployment (FastAPI, Docker) + Project 4


---

## 📫 Connect With Me

- **LinkedIn:** [your-linkedin-url]
- **Email:** [your-email]

---

<div align="center">

*If you're on a similar path, feel free to star ⭐ this repo and follow along.*

</div>