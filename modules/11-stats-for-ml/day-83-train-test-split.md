# Day 83: Train/Test Split

*A model that only works on data it has already seen is not a model — it's a memory.*

---

## Learning Objective

Understand why splitting data into training and test sets is essential for building models that generalize, and know the rules for doing it correctly.

---

## The Problem This Solves

You build a model. It scores R² = 0.95 on your data. You deploy it. It fails on new customers. Why? The model memorized the training data instead of learning the pattern. The train/test split measures performance on data the model has never seen — the only honest evaluation.

---

## The Concept

### The Split

```
Full Dataset (100%)
├── Training Set (70-80%) → Model learns patterns here
└── Test Set (20-30%)     → Model is evaluated here (ONCE)
```

### The Three-Way Split (For Model Tuning)

When comparing multiple models or tuning hyperparameters:

```
Full Dataset (100%)
├── Training Set (60%)    → Fit models
├── Validation Set (20%)  → Compare models, tune parameters
└── Test Set (20%)        → Final evaluation (touch ONCE)
```

### The Critical Rules

| Rule | Why |
|------|-----|
| **Split before any preprocessing** | Prevents data leakage |
| **Never train on test data** | Defeats the purpose of evaluation |
| **Never tune using test data** | Turns test set into a second training set |
| **Use stratification for classification** | Preserves class proportions in both sets |
| **Use time-based splits for time series** | Future can't predict past |

### Train/Test vs Statistical Holdout

You've already done this! In Module 10, every regression used out-of-sample validation. ML formalizes this practice:

| Statistical Practice | ML Equivalent |
|---------------------|--------------|
| Holdout validation | Train/test split |
| Reporting test R²/RMSE | Model evaluation on test set |
| Avoiding overfitting | Generalization |

### What Happens Without Splitting

```
Training Performance:  R² = 0.95  ← "Wow, great model!"
Test Performance:      R² = 0.42  ← "Oh no, it memorized noise"

The gap = overfitting
```

---

## Why Should a Data Analyst Care?

Because every stakeholder will ask: "How well does this model perform?" If your answer is based on training data, it's meaningless. The only honest answer comes from test set performance — data the model never trained on. This is the single most important habit in predictive modeling.

---

## When to Use It

- **Always** when building any predictive model
- **Always** when reporting performance metrics
- **Even for simple regressions** — one line of code prevents overconfidence

---

## Common Beginner Mistake

Repeatedly tweaking the model to improve test set performance. Each time you do this, the test set leaks information into your modeling decisions. After 20 rounds of "test → tweak → re-test," the test set is effectively part of training. Use a validation set for tuning; save the test set for one final evaluation.

---

## Real-World Example

A marketing team predicts campaign conversion rates:

| Metric | Training Set | Test Set |
|--------|-------------|----------|
| Accuracy | 89% | 72% |

The 17-point gap signals overfitting. They simplify the model (fewer features, add regularization):

| Metric | Training Set | Test Set |
|--------|-------------|----------|
| Accuracy | 78% | 74% |

Lower training accuracy, but the gap narrowed — this model generalizes. They report 74% to the VP, not 89%.

---

## 🔑 Key Takeaway

> Training accuracy measures memorization. Test accuracy measures learning. Only the test set tells you if the model will work on new data — and you only get to use it once.

---

## See It Applied

→ [Predicting customer spend](../../applied/notebooks/04-predicting-customer-spend.ipynb) — 80/20 split with RMSE evaluation
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — Out-of-sample validation pipeline

---

[← Day 82: Supervised vs Unsupervised Learning](day-82-supervised-vs-unsupervised.md) · [Next: Day 84 – Cross-Validation →](day-84-cross-validation.md)
