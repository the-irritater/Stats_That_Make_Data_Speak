# Day 71: Simple Linear Regression — Review

*You learned regression on Day 26. Now let's make sure you truly understand it — because everything in this module builds on it.*

---

## Learning Objective

Review simple linear regression with a deeper focus on interpretation, assumptions, and diagnostics — moving beyond formula memorization to genuine understanding.

---

## The Problem This Solves

You need to quantify the relationship between one predictor and one outcome. Not just "are they correlated?" but "by how much does Y change when X increases by one unit?" and "how confident should I be in that estimate?"

---

## The Concept

### The Model

```
Y = β₀ + β₁X + ε

Where:
  Y  = outcome (dependent variable)
  X  = predictor (independent variable)
  β₀ = intercept (predicted Y when X = 0)
  β₁ = slope (change in Y per 1-unit change in X)
  ε  = error term (what the model doesn't explain)
```

### What Each Part Means

| Component | Statistical Meaning | Business Meaning |
|-----------|-------------------|------------------|
| **β₀ (intercept)** | Y when X = 0 | Baseline value |
| **β₁ (slope)** | ΔY per unit ΔX | The effect size of the predictor |
| **R² (R-squared)** | Proportion of Y variance explained by X | How much of the outcome the predictor accounts for |
| **p-value of β₁** | Probability of observing this slope under H₀: β₁ = 0 | Is this relationship real? |
| **95% CI of β₁** | Plausible range for the true slope | The uncertainty around the estimate |

### The Five Assumptions (LINE + I)

| Assumption | What It Means | How to Check |
|-----------|--------------|-------------|
| **L**inearity | Relationship between X and Y is linear | Scatter plot, residual vs fitted plot |
| **I**ndependence | Observations are independent | Study design (not auto-correlated) |
| **N**ormality | Residuals are normally distributed | Q-Q plot, Shapiro-Wilk test |
| **E**qual variance | Residual spread is constant (homoscedasticity) | Residual vs fitted plot, Breusch-Pagan test |
| (**I**) No influential outliers | No single point dominates the fit | Cook's distance |

### Residual Diagnostics

```
Residual = Observed Y - Predicted Y = yᵢ - ŷᵢ
```

A good model has residuals that are:
- Centered around zero
- Randomly scattered (no pattern)
- Constant in spread
- Approximately normal

---

## Why Should a Data Analyst Care?

Because regression is the foundation of prediction, causal inference, and business modeling. Every forecast, every A/B test analysis, every "what drives X?" question starts with regression. Understanding it deeply — not just the formula, but the assumptions and diagnostics — is what separates analysis from guesswork.

---

## Common Beginner Mistake

Interpreting R² as the quality of a prediction. R² = 0.40 doesn't mean the model is "bad" — it means X explains 40% of Y's variance. In social sciences, R² = 0.30 is often excellent. In physics, R² = 0.99 is expected. Context matters. Also: ignoring residual plots. A model can have high R² and still violate assumptions — the coefficients and p-values would be unreliable.

---

## Real-World Example

A retail analyst models the relationship between advertising spend (X, in $1,000s) and weekly revenue (Y, in $1,000s):

```
ŷ = 12.4 + 3.2x

R² = 0.62
β₁ = 3.2, 95% CI: [2.5, 3.9], p < 0.001
```

**Interpretation:**
- Every additional $1,000 in advertising is associated with $3,200 more revenue
- Advertising explains 62% of weekly revenue variation
- The true effect is plausibly between $2,500 and $3,900 per $1,000 spent
- This is an association, not proven causation — other factors could explain the relationship

---

## 🔑 Key Takeaway

> Simple linear regression does more than draw a line through data. It quantifies relationships, tests their significance, and estimates uncertainty. But it only works when its assumptions hold — always check the residuals.

---

## See It Applied

→ [Predicting customer spend](../../applied/notebooks/04-predicting-customer-spend.ipynb) — Simple regression with residual diagnostics
→ [Restaurant Tipping Behavior](../../applied/case-studies/restaurant-tipping-behavior/) — Bill size predicting tip amount

---

[← Day 70: Module 9 Recap](../09-decision-analysis/day-70-decision-framework-recap.md) · [Next: Day 72 – Multiple Linear Regression →](day-72-multiple-linear-regression.md)
