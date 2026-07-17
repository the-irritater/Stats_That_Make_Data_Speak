# Day 84: Cross-Validation

*One split gives you one estimate. Cross-validation gives you a reliable one.*

---

## Learning Objective

Understand cross-validation as a technique for robust model evaluation, learn k-fold CV and its variants, and know when each is appropriate.

---

## The Problem This Solves

You split your data 80/20 and get R² = 0.72. But what if that particular split was lucky? What if the test set happened to contain "easy" observations? A single split gives a single estimate — and single estimates are unreliable. Cross-validation runs multiple splits and averages the results.

---

## The Concept

### K-Fold Cross-Validation

Split data into k equal parts (folds). Train on k-1 folds, test on the remaining one. Repeat k times.

```
5-Fold Cross-Validation:

Fold 1: [TEST] [Train] [Train] [Train] [Train] → Score₁
Fold 2: [Train] [TEST] [Train] [Train] [Train] → Score₂
Fold 3: [Train] [Train] [TEST] [Train] [Train] → Score₃
Fold 4: [Train] [Train] [Train] [TEST] [Train] → Score₄
Fold 5: [Train] [Train] [Train] [Train] [TEST] → Score₅

Final Score = mean(Score₁ ... Score₅) ± std
```

Every sample is used for testing exactly once.

### Variants

| Method | When to Use | Key Feature |
|--------|-------------|-------------|
| **5-Fold or 10-Fold** | Default for most problems | Good balance of bias and variance |
| **Stratified K-Fold** | Imbalanced classification | Preserves class proportions in each fold |
| **Leave-One-Out (LOO)** | Very small datasets (n < 50) | Each sample is its own test set |
| **Time Series Split** | Temporal data | Always trains on past, tests on future |
| **Repeated K-Fold** | When you need tight estimates | Run k-fold multiple times with different shuffles |

### Single Split vs Cross-Validation

| Aspect | Single Split | K-Fold CV |
|--------|-------------|-----------|
| **Performance estimates** | 1 | k |
| **Reliability** | Depends on the split | Averaged across splits |
| **Data efficiency** | 20% wasted for training | Every sample used for testing |
| **Variance of estimate** | High | Low |
| **Speed** | Fast | k× slower |

---

## Why Should a Data Analyst Care?

Reporting "R² = 0.72 ± 0.03 across 5 folds" is far more credible than "R² = 0.72 on one split." Cross-validation also reveals model stability — high variance across folds means the model is sensitive to which data it sees, which is a red flag for production deployment.

---

## When to Use It

- **Model selection** — fairly comparing algorithms (same folds for each model)
- **Hyperparameter tuning** — testing configurations robustly
- **Small datasets** — can't afford to waste 20% on a single test set
- **Performance reporting** — whenever you need a confidence interval

---

## Common Beginner Mistake

Using cross-validation on the test set. CV should happen within the training set for model selection and tuning. The test set remains untouched until final evaluation. Also: using standard K-Fold on time series data — this trains on future data and tests on past data, which is leakage.

---

## Real-World Example

An analyst compares two models for customer lifetime value:

| Model | Single Split R² | 5-Fold CV R² (mean ± std) |
|-------|-----------------|---------------------------|
| Linear Regression | 0.68 | 0.65 ± 0.02 |
| Random Forest | 0.74 | 0.71 ± 0.08 |

Single split says Random Forest wins. But CV reveals high variance (±0.08) — its performance swings across folds. Linear Regression is more consistent (±0.02). For a production system that needs reliable predictions, the analyst chooses Linear Regression and documents the reasoning.

---

## 🔑 Key Takeaway

> Cross-validation trades compute time for reliability. Instead of hoping one split is representative, you test on every portion of the data. It's the difference between an anecdote and evidence.

---

[← Day 83: Train/Test Split](day-83-train-test-split.md) · [Next: Day 85 – Bias–Variance Tradeoff →](day-85-bias-variance-tradeoff.md)
