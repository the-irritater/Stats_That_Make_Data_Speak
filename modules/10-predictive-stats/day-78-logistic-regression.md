# Day 78: Logistic Regression

*When the outcome is yes or no, linear regression breaks. Logistic regression is built for this.*

---

## Learning Objective

Understand logistic regression as the standard method for predicting binary outcomes, learn to interpret odds ratios and log-odds, and know how it differs from linear regression.

---

## The Problem This Solves

You want to predict whether a customer will churn (yes/no), whether a loan will default (yes/no), or whether a user will click (yes/no). Linear regression can predict values below 0 or above 1 — which makes no sense for a probability. Logistic regression constrains predictions to the [0, 1] range using the logistic (sigmoid) function.

---

## The Concept

### The Model

Instead of predicting Y directly, logistic regression predicts the **log-odds** (logit) of Y = 1:

```
log(p / (1 - p)) = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ

Where p = P(Y = 1) = probability of the event
```

The **sigmoid function** converts log-odds to probability:

```
p = 1 / (1 + e^(-(β₀ + β₁X₁ + ...)))

       1.0 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ╱──────
           │                           ╱
       0.5 │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╱─ ─ ─ ─
           │                       ╱
       0.0 ──────────────────────╱─ ─ ─ ─ ─ ─
           └────────────────────────────────────
                           X
```

### Interpreting Coefficients

In logistic regression, coefficients are in **log-odds** units. To make them interpretable, convert to **odds ratios**:

```
Odds Ratio (OR) = e^β
```

| OR Value | Meaning |
|----------|---------|
| OR = 1 | No effect |
| OR > 1 | Increases the odds of Y = 1 |
| OR < 1 | Decreases the odds of Y = 1 |
| OR = 2.5 | 2.5× higher odds per unit increase in X |

### Linear vs Logistic Regression

| Aspect | Linear Regression | Logistic Regression |
|--------|------------------|-------------------|
| **Outcome** | Continuous (revenue, score) | Binary (yes/no, 0/1) |
| **Predicts** | Mean of Y | Probability of Y = 1 |
| **Range** | (-∞, +∞) | [0, 1] |
| **Coefficients** | Change in Y per unit X | Change in log-odds per unit X |
| **Evaluation** | R², RMSE | Accuracy, AUC, Precision/Recall |
| **Assumptions** | Normality of residuals | No normality assumption |

### Model Evaluation

Logistic regression doesn't use R². Instead:

| Metric | What It Measures |
|--------|-----------------|
| **Accuracy** | Percentage correct (but misleading if classes are imbalanced) |
| **AUC-ROC** | Overall discriminative ability |
| **Precision** | Of predicted positives, how many are correct? |
| **Recall** | Of actual positives, how many were detected? |
| **Confusion Matrix** | Detailed breakdown of TP, FP, TN, FN |

---

## Why Should a Data Analyst Care?

Because many business outcomes are binary: will the customer buy, churn, click, convert, default, or return? Logistic regression is the standard starting point for classification — it's interpretable, well-understood, and works surprisingly well even when fancier models exist.

---

## When to Use It

- **Binary outcome prediction** — churn, default, conversion, click
- **When interpretability matters** — odds ratios are directly meaningful to stakeholders
- **As a baseline** — before trying complex models, logistic regression sets the benchmark
- **Risk scoring** — assign probabilities to individual records

---

## Common Beginner Mistake

Using accuracy as the only metric on imbalanced data. If 95% of customers don't churn, predicting "no churn" for everyone gives 95% accuracy — but catches zero actual churners. Use AUC, precision, and recall alongside accuracy. Also: interpreting logistic coefficients like linear ones. β = 0.5 means a 0.5 increase in *log-odds*, not a 0.5 increase in probability.

---

## Real-World Example

Predicting customer churn (1 = churned, 0 = retained):

| Predictor | β | OR (e^β) | p-value | Interpretation |
|-----------|---|----------|---------|---------------|
| Intercept | -2.3 | — | < 0.001 | Baseline log-odds |
| Monthly Charges ($10 units) | 0.42 | 1.52 | < 0.001 | Each $10 → 52% higher churn odds |
| Contract Length (months) | -0.08 | 0.92 | 0.003 | Each extra month → 8% lower churn odds |
| Support Tickets (count) | 0.31 | 1.36 | 0.001 | Each ticket → 36% higher churn odds |
| Has Partner (yes=1) | -0.55 | 0.58 | 0.012 | Partners → 42% lower churn odds |

**Business insight:** The biggest churn drivers are high monthly charges and support tickets. Customers with partners and longer contracts are more stable. Actionable: target high-charge, ticket-heavy customers for retention outreach.

---

## 🔑 Key Takeaway

> Logistic regression predicts probabilities for binary outcomes. Its coefficients, expressed as odds ratios, are directly interpretable: "each unit increase in X multiplies the odds by OR." It's the bridge between statistical inference and classification — learn it deeply before moving to complex ML models.

---

## See It Applied

→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Binary outcome analysis
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — RFM segment prediction

---

[← Day 77: Regularization](day-77-regularization.md) · [Next: Day 79 – Regression Case Study →](day-79-regression-case-study.md)
