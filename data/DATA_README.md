# Data Management & Provenance

This directory contains the datasets used across all modules, case studies, dashboards, and notebooks in the Stats Series project. It is meant to answer three questions for every dataset: where the data came from, what it contains, and what limitations should be remembered before interpreting results.

---

## Folder Structure

```text
data/
├── DATA_README.md        # This document
├── data-schema.json      # Machine-readable schema definitions
├── raw/                  # Immutable raw source data
│   ├── customer_discounts.csv
│   ├── ecommerce.csv
│   ├── marketing_campaign.csv
│   ├── screen_time.csv
│   └── tips.csv
└── processed/            # Reproducible aggregations and processed outputs
    ├── customer_discounts_retention_summary.csv
    ├── ecommerce_regression_summary.csv
    ├── marketing_conversions_summary.csv
    ├── screen_time_productivity_summary.csv
    └── tips_aggregations.csv
```

---

## Repository Data Rules

* `data/raw/` stores immutable input datasets. Do not edit these files directly after analyses depend on them.
* `data/processed/` stores reproducible summaries and model-ready outputs generated from raw data.
* Dataset schemas live in `data/data-schema.json`; tests should validate raw files against those schemas.
* Public datasets must include source and license notes. Synthetic datasets must include generation assumptions and, ideally, a generation script or fixed random seed.

---

## Dataset Catalog & Provenance

### 1. Restaurant Tips (`tips.csv`)
* **Source type:** Public educational dataset.
* **Source:** Originally collected by Bryant & Smith (1995) in *Practical Data Analysis: Case Studies in Business Statistics*. Also distributed through the Seaborn sample-data repository.
* **Reference URL:** `https://github.com/mwaskom/seaborn-data/blob/master/tips.csv`
* **Description:** Details restaurant tipping behavior based on total bill, gender, day of week, time of day, smoking status, and party size.
* **Metadata:** 244 records, 7 columns.
* **PII status:** No direct personal identifiers.
* **License / reuse note:** Treat as public educational sample data for portfolio work. Verify upstream licensing before commercial redistribution.
* **Known limitations:** Small observational dataset from one restaurant context; use associative language, not causal claims.

### 2. E-commerce Customer Spend (`ecommerce.csv`)
* **Source type:** Synthetic educational dataset inspired by public retail analytics schemas.
* **Source:** Derived structure from the UCI Machine Learning Repository Online Retail dataset, with synthetic extensions to support multivariable modeling.
* **Reference URL:** `https://archive.ics.uci.edu/dataset/352/online+retail`
* **Description:** Charts customer session behaviors (duration, page views, discount usage) and monetary outcomes (spend, recency, frequency).
* **Metadata:** 1,000 records, 9 columns.
* **PII status:** Synthetic `Customer_ID` values only; no real customer identifiers.
* **License / reuse note:** UCI source material should be attributed when discussed. Synthetic extensions are intended for MIT-style educational reuse inside this project.
* **Known limitations:** Not real transaction evidence; business recommendations should be framed as modeling practice.

### 3. Marketing Campaign A/B Test (`marketing_campaign.csv`)
* **Source type:** Synthetic educational dataset.
* **Source:** Generated in 2024 to mimic standard digital marketing A/B tests.
* **Description:** Logs user interaction and conversion behavior under control vs test conditions (promotional campaign vs baseline).
* **Metadata:** 2,500 records, 4 columns.
* **PII status:** Synthetic `User_ID` values only.
* **License / reuse note:** MIT-style educational reuse.
* **Known limitations:** Random assignment is assumed by construction; results should not be presented as evidence about a real campaign.

### 4. Screen Time vs Productivity (`screen_time.csv`)
* **Source type:** Synthetic educational dataset.
* **Source:** Generated in 2024 using normal and negative exponential distributions.
* **Description:** Correlates daily screen time hours with self-reported employee productivity index, along with demographic parameters (age, profession).
* **Metadata:** 150 records, 5 columns.
* **PII status:** Synthetic `User_ID`, age group, and profession categories only.
* **License / reuse note:** MIT-style educational reuse.
* **Known limitations:** Productivity is simulated and self-report-like; use this dataset to teach correlation, binning, and nonlinear patterns, not workplace policy.

### 5. Customer Discount Retention (`customer_discounts.csv`)
* **Source type:** Synthetic educational dataset.
* **Source:** Generated in 2024 to model retention behavior.
* **Description:** Records discount rate depth (0% to 50%) alongside customer retention outcome (retained vs churned), tenure, and spend.
* **Metadata:** 301 records, 5 columns.
* **PII status:** Synthetic `Customer_ID` values only.
* **License / reuse note:** MIT-style educational reuse.
* **Known limitations:** Discount depth is modeled, not randomly assigned in a real experiment; do not infer causal effects without stronger design.

---

## Reproducibility Checklist

* Raw datasets are versioned in `data/raw/`.
* Processed outputs should be regenerated from code, not hand-edited.
* Statistical claims in case-study READMEs should be covered by tests when they include exact p-values, coefficients, or row counts.
* Synthetic datasets should have generation scripts, fixed seeds, and parameter notes added before this repository is treated as fully reproducible.

---

## Ethical & Legal Statement

> [!NOTE]
> **Data Privacy & GDPR Wording:**
> The project follows GDPR-inspired data minimization principles and avoids storing personally identifiable information. This project uses synthetic/public datasets and does not contain personally identifiable information (PII). All user IDs, purchase amounts, and demographic markers are simulated or pre-anonymized.
