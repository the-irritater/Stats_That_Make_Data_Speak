# Day 77: Regularization (Ridge & Lasso)

*Regularization is how you tell a model: "Learn the pattern, but don't overthink it."*

---

## Learning Objective

Understand what regularization does, the difference between Ridge (L2) and Lasso (L1), and when to apply each to prevent overfitting and improve model stability.

---

## The Problem This Solves

Your regression has 20 features. On training data, R² = 0.94. On test data, R² = 0.61. The model overfits — it memorized noise. Regularization adds a penalty for large coefficients, forcing the model to focus on the strongest signals.

---

## The Concept

Standard OLS minimizes only the prediction error:

```
OLS Loss = Σ(yᵢ - ŷᵢ)²
```

Regularization adds a penalty term:

### Ridge Regression (L2)

```
Ridge Loss = Σ(yᵢ - ŷᵢ)² + λ × Σβⱼ²
```

- Penalty: sum of **squared** coefficients
- Effect: **shrinks** all coefficients toward zero — none reach exactly zero
- Best for: multicollinearity, keeping all predictors with reduced influence

### Lasso Regression (L1)

```
Lasso Loss = Σ(yᵢ - ŷᵢ)² + λ × Σ|βⱼ|
```

- Penalty: sum of **absolute** coefficients
- Effect: **zeros out** weak coefficients — automatic feature selection
- Best for: sparse models, identifying the most important predictors

### Comparison

| Aspect | OLS | Ridge (L2) | Lasso (L1) |
|--------|-----|-----------|-----------|
| **Penalty** | None | Sum of β² | Sum of \|β\| |
| **Coefficients** | Unbiased, high variance | Biased, low variance | Biased, sparse |
| **Feature selection** | No | No | Yes (zeros out weak features) |
| **Multicollinearity** | Fails | Handles well | Picks one, drops others |
| **When to use** | Few predictors, no collinearity | Many correlated predictors | Many irrelevant predictors |

### The λ (Lambda) Parameter

| λ Value | Effect |
|---------|--------|
| λ = 0 | No regularization → OLS |
| Small λ | Light penalty → close to OLS |
| Large λ | Heavy penalty → coefficients → 0 |
| Optimal λ | Found via **cross-validation** |

---

## Why Should a Data Analyst Care?

Because real data has noise, and OLS will fit that noise if given the chance. Regularization is the standard safeguard in any regression with more than a handful of predictors. Lasso is especially valuable because it tells you which features matter — an insight stakeholders always want.

---

## When to Use It

- **Many predictors relative to observations** — regularization prevents overfitting
- **Multicollinearity present** — Ridge stabilizes coefficients
- **Feature selection needed** — Lasso identifies the strongest predictors
- **Building production models** — regularized models are more stable on new data

---

## Common Beginner Mistake

Forgetting to **standardize** features before regularization. The penalty treats all coefficients equally, but raw coefficients depend on feature scale. A coefficient of 500 for "income in dollars" will be penalized more than 0.2 for "age in years" — not because income matters less, but because of units. Always standardize (z-score) before applying Ridge or Lasso.

---

## Real-World Example

Predicting employee attrition risk using 25 HR features:

| Model | Features Used | Train R² | Test R² |
|-------|--------------|----------|---------|
| OLS | 25 | 0.89 | 0.58 |
| Ridge (λ = 1.0) | 25 (all shrunk) | 0.82 | 0.76 |
| Lasso (λ = 0.5) | 8 (17 zeroed out) | 0.79 | 0.77 |

Lasso's 8 surviving features: `overtime_hours`, `years_at_company`, `salary_band`, `manager_rating`, `commute_distance`, `last_promotion_years`, `training_hours`, `satisfaction_score`.

Fewer features. Better generalization. Clearer story for HR.

---

## 🔑 Key Takeaway

> Regularization trades a small amount of bias for a large reduction in variance. Ridge stabilizes all coefficients. Lasso drops the weak ones entirely. Both produce models that work better on new data than unregularized OLS.

---

## See It Applied

→ [Predicting customer spend](../../applied/notebooks/04-predicting-customer-spend.ipynb) — Regression with out-of-sample evaluation
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — HC3-robust inference with coefficient analysis

---

[← Day 76: Model Selection](day-76-model-selection.md) · [Next: Day 78 – Logistic Regression →](day-78-logistic-regression.md)
