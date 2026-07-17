# Day 90: Machine Learning Mini Project — Customer Churn Prediction

*90 days. The final test: can you take a raw dataset, build a prediction model, evaluate it honestly, and make a business recommendation?*

---

## Learning Objective

Apply the complete ML pipeline — from data understanding to model evaluation — in a single end-to-end project that uses every skill from this module.

---

## The Project

**Business problem:** A telecom company wants to predict which customers will churn next month so the retention team can intervene proactively.

**Dataset:** 2,000 customers with demographics, account info, and churn label.

---

## The Pipeline

### Step 1: Understand the Data

| Variable | Type | Description |
|----------|------|-------------|
| `gender` | Categorical | Male / Female |
| `tenure` | Continuous | Months as customer |
| `monthly_charges` | Continuous | Monthly bill ($) |
| `total_charges` | Continuous | Cumulative charges ($) |
| `contract` | Categorical | Month-to-month / 1-year / 2-year |
| `internet_service` | Categorical | DSL / Fiber / None |
| `support_tickets` | Discrete | Number of tickets filed |
| `churned` | Binary (target) | 1 = churned, 0 = retained |

**Class distribution:** 26% churned, 74% retained (imbalanced → accuracy will be misleading)

### Step 2: Feature Engineering (Day 86)

From raw data, create predictive features:

| Engineered Feature | Source | Rationale |
|-------------------|--------|-----------|
| `avg_monthly_charge` | total_charges / tenure | Normalized spending |
| `is_new_customer` | tenure < 6 months | Early churn risk |
| `has_fiber` | internet_service = Fiber | Higher churn in fiber customers |
| `is_month_to_month` | contract type | Flexibility = easier to leave |

### Step 3: Train/Test Split (Day 83)

```
2,000 customers
├── Train: 1,600 (80%) — stratified to preserve 26% churn rate
└── Test: 400 (20%) — final evaluation only
```

### Step 4: Model Training & Cross-Validation (Day 84)

Compare three models using 5-fold stratified CV on training data:

| Model | CV Accuracy | CV AUC | CV F1 |
|-------|-----------|--------|-------|
| Logistic Regression | 0.78 ± 0.02 | 0.83 ± 0.02 | 0.62 ± 0.03 |
| Decision Tree (depth=5) | 0.76 ± 0.03 | 0.79 ± 0.04 | 0.58 ± 0.05 |
| Random Forest (200 trees) | 0.81 ± 0.02 | 0.87 ± 0.02 | 0.68 ± 0.03 |

Random Forest wins on all metrics — and has low variance (±0.02).

### Step 5: Feature Importance (Day 88)

Random Forest feature importance:

```
monthly_charges    ████████████████████  0.24
tenure             ██████████████████    0.21
total_charges      █████████████████     0.18
contract_m2m       ██████████████        0.15
support_tickets    ██████████            0.11
has_fiber          ████████              0.07
is_new_customer    ██████                0.04
```

### Step 6: Final Evaluation on Test Set (Day 89)

| Metric | Value | Interpretation |
|--------|-------|---------------|
| Accuracy | 82% | 82% of predictions are correct |
| Precision | 71% | 29% of churn predictions are false alarms |
| Recall | 65% | Catches 65% of actual churners |
| F1 Score | 0.68 | Moderate balance |
| AUC-ROC | 0.86 | Strong discriminative ability |

**Confusion Matrix (Test Set):**

```
                 Predicted
               Churn   Retain
Actual Churn  [  68  |   36  ]    (Recall = 68/104 = 65%)
Actual Retain [  28  |  268  ]    (Specificity = 268/296 = 91%)
```

### Step 7: Business Recommendation

**Finding:** The model identifies 65% of future churners with 71% precision.

**ROI Analysis:**
- Average customer lifetime value: $2,400
- Retention intervention cost: $50 per customer
- Without model: lose ~520 customers/year × $2,400 = $1.25M
- With model: save 65% of churners = 338 customers → $811K saved
- Intervention cost: 96 × 12 × $50 = $57.6K (including false positives)
- **Net benefit: ~$753K/year**

**Recommendations:**
1. **Deploy** the Random Forest model for monthly churn scoring
2. **Prioritize** high monthly charges + month-to-month contracts for retention outreach
3. **Monitor** model performance monthly — retrain quarterly as data shifts
4. **Next step:** Test whether proactive outreach actually reduces churn (A/B test the intervention)

---

## The 90-Day Journey

```
Days 1–30:  UNDERSTAND STATISTICS    → Concepts, probability, inference
Days 31–60: WORK WITH REAL DATA      → EDA, assumptions, diagnostics
Days 61–70: MAKE STATISTICAL DECISIONS → t-tests, ANOVA, Chi-Square
Days 71–80: BUILD PREDICTIVE MODELS  → Regression, regularization, logistic
Days 81–90: TRANSITION TO ML         → Trees, forests, evaluation, deployment
```

Every concept built on the one before. Statistics gave you the thinking. ML gave you the tools. Together, they make data speak.

---

## What's Next

If you continue beyond Day 90:

| Days | Module | Focus |
| Days | Module | Focus |
|------|--------|-------|
| 91–100 | Experimental Design & Causal Inference | A/B testing, MDE, power, and natural experiments |
| 101–110 | Time Series & Forecasting | Trends, seasonality, decomposition, Holt-Winters, ARIMA |
| 111–120 | Modern Analytics & Decision Science | KPIs, cohorts, funnels, dashboard storytelling |
| 121–150 | Bayesian Statistics & Advanced Inference | Prior/posterior updates, MCMC, Bayesian A/B testing |
| 151–180 | Multivariate Statistics | PCA, Factor Analysis, MANOVA, Structural Equation Modeling (SEM) |
| 181–210 | Statistical Learning | Regularization, ensembles, feature selection, explainability |
| 211–240 | Advanced Machine Learning | XGBoost, LightGBM, SHAP, Optuna, Calibration |
| 241–365 | Capstone Projects & Portfolio | Industry case studies and end-to-end portfolio projects |

---

## 🔑 Key Takeaway

> Machine learning is not the end of the journey — it's the point where statistics scales. Every concept in this mini project traces back to something you learned in the first 60 days. The difference is: now you can build, evaluate, and deploy models that make real business impact.

> *Because data alone does not speak. Statistics makes it speak. Machine learning makes it act.*

---

[← Day 89: Model Evaluation Metrics](day-89-evaluation-metrics.md) · [Next: Day 91 – Correlation vs Causation →](../12-experimental-design/day-91-correlation-vs-causation.md)
