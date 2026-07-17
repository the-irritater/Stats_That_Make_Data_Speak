# Day 76: Model Selection

*Adding predictors always improves R². But it doesn't always improve the model.*

---

## Learning Objective

Learn systematic approaches to choosing the right set of predictors, understand information criteria (AIC/BIC), and know when to stop adding variables.

---

## The Problem This Solves

You have 15 potential predictors. Including all of them gives R² = 0.82, but many are non-significant, some are collinear, and the model is hard to explain. Including only 3 gives R² = 0.65, but maybe you're missing important drivers. Model selection finds the sweet spot — enough predictors to capture real patterns, few enough to remain interpretable and generalizable.

---

## The Concept

### Why Not Just Include Everything?

| Problem | What Happens |
|---------|-------------|
| **Overfitting** | Model fits noise in the training data |
| **Multicollinearity** | Correlated predictors destabilize coefficients |
| **Interpretability** | Stakeholders can't act on 15 drivers |
| **R² always increases** | Even random noise adds R² — it's misleading |

### Model Selection Methods

#### 1. Stepwise Selection

| Method | How It Works | Limitation |
|--------|-------------|------------|
| **Forward** | Start empty, add best predictor one at a time | May miss combinations |
| **Backward** | Start full, remove worst predictor one at a time | Expensive with many predictors |
| **Stepwise** | Combination — add and remove at each step | Can be unstable |

#### 2. Information Criteria

Score models on fit vs complexity — lower is better:

```
AIC = n × ln(RSS/n) + 2k
BIC = n × ln(RSS/n) + k × ln(n)

Where:
  n = sample size
  k = number of predictors
  RSS = residual sum of squares
```

| Criterion | Penalty for Complexity | Best For |
|-----------|----------------------|----------|
| **AIC** | Lighter (2k) | Prediction — allows more predictors |
| **BIC** | Heavier (k × ln(n)) | Explanation — prefers simpler models |

#### 3. Adjusted R²

```
Adjusted R² = 1 - [(1 - R²)(n - 1) / (n - k - 1)]
```

Unlike R², Adjusted R² *decreases* when a useless predictor is added.

#### 4. Domain Knowledge

The best model selection method. Ask:
- Does this predictor make business sense?
- Can we collect this data in production?
- Would a stakeholder understand why it's in the model?

---

## The Practical Approach

```
1. Start with domain knowledge → identify candidate predictors
2. Check correlations → remove redundant predictors (VIF > 10)
3. Fit the full model → examine p-values and coefficient signs
4. Compare models using AIC/BIC and Adjusted R²
5. Validate on holdout data → does the simpler model generalize?
6. Choose the model that balances accuracy, simplicity, and interpretability
```

---

## Why Should a Data Analyst Care?

Because every model you present must be defensible. "Why did you include that variable?" is a question you'll always face. Model selection gives you a systematic, evidence-based answer instead of "I tried everything and kept what worked."

---

## When to Use It

- **Any multiple regression** — even with 3 predictors, consider whether all belong
- **High-dimensional data** — many potential features
- **Before stakeholder presentations** — simpler models are easier to explain and trust
- **Before deployment** — fewer features = fewer data requirements in production

---

## Common Beginner Mistake

Using stepwise selection and reporting the final model as if it was chosen by theory. Stepwise methods are data-driven — they can produce different models on slightly different data. Always validate the selected model on holdout data and justify inclusions with domain reasoning, not just p-values.

---

## Real-World Example

An analyst builds a customer lifetime value model with 12 candidate predictors:

| Model | Predictors | R² | Adj R² | AIC | BIC |
|-------|-----------|------|--------|-----|-----|
| Full (12 vars) | All | 0.74 | 0.71 | 1842 | 1901 |
| Reduced (6 vars) | Top 6 by BIC | 0.72 | 0.71 | 1831 | 1860 |
| Minimal (3 vars) | Top 3 by domain | 0.68 | 0.67 | 1856 | 1870 |

**Decision:** The 6-variable model has the best AIC/BIC, same Adjusted R² as the full model, and each predictor is interpretable. The full model offers no meaningful improvement for twice the complexity.

---

## 🔑 Key Takeaway

> Model selection is about finding the model that explains enough without explaining noise. Use AIC/BIC and Adjusted R² to compare objectively, domain knowledge to filter practically, and holdout data to validate honestly.

---

[← Day 75: Multicollinearity](day-75-multicollinearity.md) · [Next: Day 77 – Regularization (Ridge & Lasso) →](day-77-regularization.md)
