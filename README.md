# Stats That Make Data Speak

**I turn statistical concepts into rigorous, real-world data decisions using Python and analytical pipelines.**

> [!NOTE]
> **Educational & Portfolio Disclaimer:** Most datasets in this repository are synthetic and are used for educational and statistical demonstration. Findings should be interpreted as portfolio examples, not real business evidence.

<!-- Identity & CI Status Badges -->
<p align="center">
  <a href="https://github.com/the-irritater/Stat_That_Make_Data_Speak">
    <img src="https://img.shields.io/badge/🔮_StatSphere-Making_Data_Make_Sense-1A365D?style=for-the-badge&labelColor=0D1B2A&color=2B6CB0" alt="StatSphere" />
  </a>
  <a href="https://www.linkedin.com/in/sanman-kadam-7a4990374/">
    <img src="https://img.shields.io/badge/by-Sanman_Kadam-E53E3E?style=for-the-badge&labelColor=1A365D" alt="Author" />
  </a>
  <a href="https://github.com/the-irritater/Stat_That_Make_Data_Speak/actions/workflows/tests.yml">
    <img src="https://github.com/the-irritater/Stat_That_Make_Data_Speak/actions/workflows/tests.yml/badge.svg" alt="CI Build" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License" />
  </a>
</p>

---

### 💼 Recruiter Summary
> This repository showcases end-to-end analytical rigor, translating raw, noisy datasets into statistical proof and actionable business strategies. Built with Python (`pandas`, `scipy`, `statsmodels`, `scikit-learn`), it demonstrates out-of-sample predictive validation, linear model assumption checking, and robust effect-size reporting. Every project transitions from data cleaning and schema validation to automated testing and interactive, stakeholder-facing dashboards.

---

### 🚀 Try the Live Dashboard
Explore all statistical studies, regression diagnostics, relative risk engines, and tipping tests interactively:
👉 **[StatSphere Analytics Hub (Streamlit Cloud)](https://statsphere-hub.streamlit.app)** *(Instructions for local deployment are listed below)*

---

### 🏆 Featured Projects (Best Work)

1. **[Signature Project: End-to-End Customer Analytics](applied/signature-project/)**
   - **Focus:** Custom schema verification, multiple OLS regression, RFM customer segmentation, and Chi-Square independence testing.
   - **Key Finding:** Page clicks are the strongest spend predictor (Standardized Beta: 0.62, $p < 0.001$). RFM segment membership does not statistically predict repeat purchase rates ($p = 0.551$, Cramer's V: 0.0345), warning against blanket segment-wide loyalty campaigns.
   - **Artifacts:** [Jupyter Notebook](applied/signature-project/notebooks/customer_analytics.ipynb) | [Executive Business Report](applied/signature-project/outputs/report.md)

2. **[Restaurant Tipping Behavior Welch's t-test & OLS](applied/case-studies/restaurant-tipping-behavior/)**
   - **Focus:** Welch's two-sample t-test, OLS regression with VIF collinearity and residuals diagnostics (Shapiro-Wilk, Breusch-Pagan).
   - **Key Finding:** Sunday dinners yield the highest median spend. Tipping percentage shows no significant difference between lunch and dinner (p = 0.51), confirming table turnover volume should be Saturdays' primary focus.
   - **Artifacts:** [Analysis Notebook](applied/case-studies/restaurant-tipping-behavior/analysis.ipynb)

3. **[Discount Retention & Relative Risk Analysis](applied/case-studies/discount-vs-retention/)**
   - **Focus:** Chi-Square Test of Independence, Relative Risk (Risk Ratio) and retention lift with 95% Confidence Intervals.
   - **Key Finding:** Capping promotions at 20% maximizes LTV. Deep 50% discounts attract transient coupon-hunting churners, yielding the worst long-term retention.
   - **Artifacts:** [Analysis Notebook](applied/case-studies/discount-vs-retention/discount_retention.ipynb)

---

### ✅ Demonstrated Analytical Competencies
- [x] **Predictive Validity:** Out-of-sample test splits (80/20) evaluated on RMSE/MAE against simple historical mean baselines.
- [x] **Regression Diagnostics:** Testing VIF for multicollinearity, Shapiro-Wilk/Jarque-Bera for residuals normality, and Breusch-Pagan for heteroscedasticity.
- [x] **Rigorous Inference:** Reporting Cohen's d / h effect sizes, Cramer's V, and 95% confidence intervals next to p-values to evaluate practical vs. statistical significance.
- [x] **Data Pipelines & Schema Validation:** Column type checks and duplicate primary key checking via automated JSON schema validations.
- [x] **Interactive Data Products:** A dynamic Streamlit dashboard displaying interactive statistical tests and diagnostic residual plots.
- [x] **Software Engineering Best Practices:** Automated `Makefile` targets, pre-commit styling (`black`/`isort`), and unit testing (`pytest` with >= 85% coverage gate in CI).

---

### 📐 Project Architecture & Data Flow

```mermaid
graph TD
    A[Raw Datasets .csv] --> B[DataLoader / Schema Validation]
    B -->|Check column presence, types, primary key duplicates| C[Valid DataFrames]
    C --> D[Applied Analyses & Notebooks]
    C --> E[Streamlit Interactive Dashboard]
    D -->|Perform Welch's t-test, OLS, RFM, Chi-Square| F[Outputs, Visualizations & Reports]
    E -->|Interactive filtering & diagnostic plots| G[Stakeholder Decision Support]
```

---

### 🛠️ Repository Maturity Roadmap
| Component | Features Implemented | CI Verification | Status |
|-----------|----------------------|-----------------|--------|
| **Data Ingestion** | Schema validation, duplicate primary key checks, type assertions | Yes (pytest) | 100% Complete |
| **Statistical Notebooks** | Pre-analysis rules, effect sizes, CIs, diagnostic checks, non-causal phrasing | Yes (Jupyter Execution CI) | 100% Complete |
| **Interactive Dashboard** | Landing page, download buttons, interactive t-tests/RR, residual plots, VIF | Manual & Pytest | 100% Complete |
| **Testing Suite** | Pytest unit tests, coverage reports | Yes (GitHub Actions, >85% Gate) | 100% Complete |

---

## Learning Path

### Part 1: Theory — Stats Foundations

The concepts behind every data decision. Each module = 5–10 days of focused learning.

| Module | Topic | Days | Status |
|--------|-------|------|--------|
| 1 | [**Basics**](modules/01-basics/) — What statistics is, types of data, how we collect it | Day 1–5 | Complete |
| 2 | [**Descriptive Stats**](modules/02-descriptive-stats/) — Summarizing data, central tendency, spread | Day 6–10 | Complete |
| 3 | [**Probability**](modules/03-probability/) — Chance, conditional probability, Bayes | Day 11–15 | Complete |
| 4 | [**Distributions**](modules/04-distributions/) — Normal, binomial, CLT | Day 16–20 | Complete |
| 5 | [**Inference**](modules/05-inference/) — Confidence intervals, hypothesis testing | Day 21–25 | Complete |
| 6 | [**Modeling**](modules/06-modeling/) — Regression, correlation, ANOVA | Day 26–30 | Complete |
| 7 | [**Data Foundations**](modules/07-data-foundations/) — Datasets, data types, cleaning, EDA | Day 31–40 | Complete |
| 8 | [**Applied Methods**](modules/08-applied-methods/) — Visualization, bias, assumptions, diagnostics | Day 41–60 | Complete |

### Part 2: Applied — Python + Real Data

Theory means nothing without application. These notebooks answer **real business questions** using real datasets.

| # | Notebook | Business Question | Key Skill |
|---|----------|-------------------|-----------|
| 1 | [What does our sales data actually look like?](applied/notebooks/01-what-does-sales-data-look-like.ipynb) | Understanding data before making decisions | EDA, Distributions |
| 2 | [Analyzing customer spending patterns](applied/notebooks/02-customer-spending-patterns.ipynb) | Where does the money come from? | Mean, Median, Grouping |
| 3 | [What actually drives sales?](applied/notebooks/03-what-drives-sales.ipynb) | Which factors matter most? | Correlation Analysis |
| 4 | [Predicting customer spend](applied/notebooks/04-predicting-customer-spend.ipynb) | Can we forecast revenue? | Linear Regression |
| 5 | [Do discounts increase repeat purchases?](applied/notebooks/05-do-discounts-work.ipynb) | Should we keep running promos? | A/B Testing |
| 6 | [Who are our best buyers?](applied/notebooks/06-who-are-best-buyers.ipynb) | How do we target the right people? | Customer Segmentation |
| 7 | [Is this campaign actually working?](applied/notebooks/07-is-campaign-working.ipynb) | Are we wasting marketing budget? | Hypothesis Testing |

### Part 3: Case Studies & Projects

Complete analyses that show the full pipeline: question → data → analysis → business insight.

| Case Study | Key Finding |
|------------|-------------|
| [Screen Time vs Productivity](applied/case-studies/screen-time-vs-productivity/) | Higher screen time (>6 hrs) shows negative correlation with productivity scores |
| [Do Discounts Drive Retention?](applied/case-studies/discount-vs-retention/) | Discount depth doesn't predict customer return rate |
| [Restaurant Tipping Behavior (Real-World)](applied/case-studies/restaurant-tipping-behavior/) | Bill size and party size explain 46.8% of variance in tips; tipping percentage is similar between lunch and dinner (p = 0.51) |
| [Signature Project: Customer Analytics](applied/signature-project/) | Multiple regression spend forecasts and RFM profiles |

---

## Project Purpose

**Stats That Make Data Speak** is a comprehensive, hands-on framework designed to bridge the gap between academic statistical theory and practical business decisions. Data alone is silent; statistics provides the structured language to translate data shape, variation, and trends into clear business recommendations. This portfolio is engineered to demonstrate complete analytics pipelines:
*   **Data Validation:** Guaranteeing schema validity, type checks, and ethical standards.
*   **Exploratory Data Analysis (EDA):** Separating typical trends from outliers using robust statistics (e.g., medians over skewed averages).
*   **Inference & Regression Modeling:** Quantifying drivers and testing business promotions under rigorous significance thresholds.
*   **Interactive Controls:** Enabling stakeholders to explore and slice datasets dynamically.

---

## Quick Start & Usage Guide

### 1. Environment & Dependency Setup
This project supports automated environment management using [Poetry](https://python-poetry.org/) or [Make](https://www.gnu.org/software/make/).

Using setup helper script:
```bash
# Clone the repository
git clone https://github.com/the-irritater/Stat_That_Make_Data_Speak.git
cd Stat_That_Make_Data_Speak

# Create a virtual environment and install packages automatically
./setup.sh --install-deps
```

Or execute via `make` directly:
```bash
# Clean up setup and install pinned dependencies
make setup
```

*Note: If you do not wish to use Poetry or Make, you can install packages manually using the convenience requirements fallback file:*
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

### 2. Run Interactive Dashboard
Explore statistical analyses, regressions, A/B tests, and tipping thresholds via a premium Streamlit dashboard:
```bash
make run-dashboard
```

### 3. Launch Notebooks
```bash
source .venv/bin/activate
jupyter notebook
```

---

## How to Reproduce

You can reproduce all results and start the interactive components with these exact commands:

```bash
make setup            # Setup virtual environment and install all dependencies
make test             # Run unit tests and generate coverage report
make generate-data    # Precompute analytical aggregates from raw datasets
make run-dashboard    # Launch the interactive Streamlit dashboard
```

---

## Reproducibility Checklist

To guarantee the reliability and exact replication of all figures, metrics, and models:
1.  **Environment Alignment:** Always run `git pull` followed by `make setup` to align local packages with pinned dependencies.
2.  **Dataset Integrity:** Ensure raw data remains untouched in `data/raw/`. Re-run data loader tests (`make test`) to check file hashes and schemas.
3.  **Timestamp Snapshots:** For any external or time-sensitive data analysis, capture and log timestamp snapshots in your local workspace to anchor regression fits against real-world drift.
4.  **Local Pipeline Testing:** Execute the entire test suite and verify coverage using:
    ```bash
    make test
    ```
5.  **Format Verification:** Format code with `make format` to ensure style rules are met before commits.

---

## Contributing Guide

We welcome peer review, validation, and extensions to the analysis pipelines.

### PR Requirements
1.  **Code Quality & Format:** Run `make lint` locally. All Python code must be formatted using `black` (120 char length) and sorted using `isort`.
2.  **Unit & Integration Tests:** Any new analytical routines or loading helpers must be accompanied by pytest unit tests in the `tests/` directory. Tests should use tolerance-based assertions.
3.  **Replication Check:** Execute the peer validation template notebook [collaborative_peer_validation.ipynb](applied/notebooks/collaborative_peer_validation.ipynb) to verify existing models are not broken.
4.  **No Unnecessary Files:** Do not commit temporary logs, workspace configs (`.vscode/`), cached metrics, or internal planning documents. Make sure files like LinkedIn drafts or internal calendars are filtered out by `.gitignore`.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.11** | Core language |
| **pandas** | Data manipulation |
| **NumPy** | Numerical computation |
| **matplotlib** | Base visualizations |
| **seaborn** | Statistical visualizations |
| **scipy** | Statistical tests |
| **statsmodels** | Regression & modeling |
| **scikit-learn** | Segmentation & ML basics |
| **Jupyter** | Interactive analysis |

---

## About

**Author:** StatSphere (Sanman Kadam)

I am building this resource as part of my journey into data analytics — learning in public, applying statistics to real-world business problems, and sharing data-driven insights.

**Find me on LinkedIn:** [Sanman Kadam](https://www.linkedin.com/in/sanman-kadam-7a4990374/)

*If this repo helped you, give it a star — it helps others find it too.*

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

