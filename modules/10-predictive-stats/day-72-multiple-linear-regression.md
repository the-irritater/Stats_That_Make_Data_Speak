# Day 72: Multiple Linear Regression

*One predictor gives you a trend. Multiple predictors give you a model.*

---

## Learning Objective

Understand multiple linear regression as the natural extension of simple regression, learn to interpret coefficients as partial effects, and know what changes when you add more predictors.

---

## The Problem This Solves

In simple regression, you found that advertising spend predicts revenue. But revenue also depends on price, seasonality, and competitor activity. Multiple regression lets you model the effect of advertising *while controlling for* these other factors — isolating each predictor's unique contribution.

---

## The Concept

### The Model

```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε
```

Each coefficient βⱼ represents the change in Y for a 1-unit increase in Xⱼ, **holding all other predictors constant**.

### Simple vs Multiple Regression

| Aspect | Simple Regression | Multiple Regression |
|--------|------------------|-------------------|
| **Predictors** | 1 | 2 or more |
| **Interpretation** | Total effect of X on Y | Partial effect of Xⱼ, controlling for others |
| **R²** | Variance explained by one predictor | Variance explained by all predictors together |
| **Risk** | Omitted variable bias | Multicollinearity |

### Standardized Coefficients (Beta Weights)

Raw coefficients (β) depend on the units of each variable — you can't compare a $3.20 coefficient with a 0.15 coefficient. Standardized coefficients (β*) put all predictors on the same scale:

```
β* = β × (s_x / s_y)

β* of 0.45 means: a 1 standard deviation increase in X
is associated with a 0.45 standard deviation increase in Y
```

This lets you rank predictors by importance.

### Adjusted R²

When you add predictors, R² always increases — even if the new predictor is noise. Adjusted R² penalizes for the number of predictors:

```
Adjusted R² = 1 - [(1 - R²)(n - 1) / (n - k - 1)]
```

- If a new predictor improves the model: Adjusted R² goes up
- If a new predictor adds noise: Adjusted R² goes down

Always report Adjusted R² for multiple regression.

---

## Why Should a Data Analyst Care?

Because real outcomes have multiple causes. "What drives customer spend?" is never answered by a single predictor. Multiple regression lets you disentangle overlapping effects and identify which factors independently matter — the foundation for every business recommendation.

---

## When to Use It

- **Multiple potential drivers** — revenue depends on price, marketing, season
- **Controlling for confounders** — isolating the effect of one variable while holding others constant
- **Building prediction models** — forecasting outcomes using available information
- **Quantifying relative importance** — which predictor matters most?

---

## Common Beginner Mistake

Interpreting coefficients as if other variables don't exist. In multiple regression, β₁ is the effect of X₁ *holding X₂, X₃, ... constant*. A predictor's coefficient can change dramatically — even flip sign — when other variables are added. This is not a bug; it's the model correctly isolating partial effects.

---

## Real-World Example

Predicting monthly sales ($K) for a retail chain:

| Predictor | β (raw) | β* (standardized) | p-value | 95% CI |
|-----------|---------|-------------------|---------|--------|
| Intercept | 15.2 | — | < 0.001 | [10.1, 20.3] |
| Ad Spend ($K) | 2.8 | 0.42 | < 0.001 | [2.1, 3.5] |
| Store Size (sqft/1000) | 4.5 | 0.35 | < 0.001 | [3.2, 5.8] |
| Avg Price ($) | -1.2 | -0.18 | 0.012 | [-2.1, -0.3] |
| Competitor Count | -0.8 | -0.11 | 0.089 | [-1.7, 0.1] |

**Model:** Adjusted R² = 0.71

**Interpretation:**
- Ad spend is the strongest predictor (β* = 0.42): each $1K in ads → $2.8K more sales
- Store size matters independently (β* = 0.35)
- Higher average prices are associated with lower sales, controlling for other factors
- Competitor count is not significant (p = 0.089) — might be dropped in model selection

---

## 🔑 Key Takeaway

> Multiple regression doesn't just add predictors — it isolates their independent effects. Each coefficient tells you what happens when *one* variable changes and everything else stays the same. That's the closest observational data gets to causal thinking.

---

## See It Applied

→ [Predicting customer spend](../../applied/notebooks/04-predicting-customer-spend.ipynb) — Multiple regression with R² = 0.473
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — Full MLR with standardized betas and VIF

---

[← Day 71: Simple Linear Regression Review](day-71-simple-linear-regression-review.md) · [Next: Day 73 – Dummy Variables →](day-73-dummy-variables.md)
