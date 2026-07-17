# Day 80: Predictive Statistics Recap

*10 days. One skill: build models that explain the past and predict the future — honestly.*

---

## Learning Objective

Consolidate everything from Module 10 and understand the complete regression toolkit available for data analysis.

---

## What We Covered (Day 71–80)

| Day | Topic | Core Insight |
|-----|-------|-------------|
| 71 | Simple Linear Regression Review | One predictor → one slope, check assumptions |
| 72 | Multiple Linear Regression | Multiple predictors → partial effects, controlling for confounders |
| 73 | Dummy Variables | Include categories in regression with k-1 binary indicators |
| 74 | Interaction Effects | The effect of X₁ depends on X₂ → non-parallel slopes |
| 75 | Multicollinearity | Correlated predictors → unstable coefficients → check VIF |
| 76 | Model Selection | AIC/BIC and Adjusted R² → find the best model, not the biggest |
| 77 | Regularization | Ridge shrinks coefficients, Lasso zeros them out |
| 78 | Logistic Regression | Binary outcomes → odds ratios → classification |
| 79 | Regression Case Study | Full pipeline from data to business recommendation |

---

## The Regression Decision Framework

```
What type of outcome?
│
├── CONTINUOUS (price, revenue, score)
│   │
│   ├── One predictor → Simple Linear Regression
│   ├── Multiple predictors → Multiple Linear Regression
│   │   ├── Categorical predictors? → Add Dummy Variables
│   │   ├── Effects depend on each other? → Add Interactions
│   │   ├── VIF > 10? → Address Multicollinearity
│   │   └── Overfitting? → Regularization (Ridge/Lasso)
│   │
│   └── Too many predictors? → Model Selection (AIC/BIC)
│
└── BINARY (yes/no, churn/retain, click/ignore)
    └── Logistic Regression
        └── Evaluate: AUC, Precision, Recall (not just accuracy)

FOR ALL MODELS:
  1. Check assumptions (LINE)
  2. Report coefficients + CIs + effect sizes
  3. Validate on holdout data
  4. Translate to business language
```

---

## The Reporting Checklist

Every regression analysis you present should include:

| Item | Why |
|------|-----|
| **Model equation** | What was fitted |
| **R² and Adjusted R²** | How much variance is explained |
| **Coefficient table** (β, SE, p, CI) | What each predictor does |
| **VIF values** | Multicollinearity check |
| **Residual diagnostics** | Are assumptions met? |
| **Train vs Test performance** | Does the model generalize? |
| **Business interpretation** | What should stakeholders do? |

---

## How Module 10 Connects to What's Next

| Predictive Statistics (This Module) | Statistics for ML (Module 11) |
|-------------------------------------|------------------------------|
| Linear/Logistic Regression | Decision Trees, Random Forests |
| Regularization (Ridge/Lasso) | Bias-Variance Tradeoff |
| Adjusted R² for model selection | Cross-Validation |
| VIF for feature assessment | Feature Engineering |
| Holdout validation | Train/Test Split formalized |

Module 10 built prediction with statistical models.
Module 11 extends prediction with machine learning — keeping the statistical foundation you've built.

---

## 🔑 Key Takeaway

> Regression is not one technique — it's a family. Simple, multiple, regularized, logistic — each answers a different question. The skill is knowing which to use, diagnosing problems, and presenting results that stakeholders can act on. Master regression, and you can model almost any business problem.

---

[← Day 79: Regression Case Study](day-79-regression-case-study.md) · [Back to Module 10](README.md)
