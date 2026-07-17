# Day 88: Random Forests

*One tree is fragile. A hundred trees, each slightly different, are remarkably accurate.*

---

## Learning Objective

Understand how Random Forests work by combining many decision trees, why ensemble methods outperform individual models, and how to interpret feature importance.

---

## The Problem This Solves

Decision trees are interpretable but unstable — small changes in data can produce completely different trees. They also overfit easily. Random Forests solve both problems by training hundreds of trees on slightly different data and averaging their predictions. The result: a model that's both accurate and stable.

---

## The Concept

### How Random Forests Work

1. **Bootstrap sampling:** Draw n random samples (with replacement) from the training data — each tree gets a slightly different dataset
2. **Random feature selection:** At each split, consider only a random subset of features (not all)
3. **Build many trees:** Train 100–500 independent decision trees
4. **Aggregate predictions:**
   - Classification → majority vote
   - Regression → average prediction

```
Data → [Bootstrap Sample 1] → Tree 1 → Prediction 1
     → [Bootstrap Sample 2] → Tree 2 → Prediction 2
     → [Bootstrap Sample 3] → Tree 3 → Prediction 3
     → ...                  → ...    → ...
     → [Bootstrap Sample N] → Tree N → Prediction N

Final Prediction = Average (regression) or Vote (classification)
```

### Why It Works

| Single Tree Problem | Random Forest Solution |
|--------------------|-----------------------|
| **Overfitting** | Each tree overfits differently; averaging cancels out noise |
| **Instability** | Different bootstrap samples → diverse trees → stable ensemble |
| **Bias toward strong features** | Random feature subsets → all features get a chance |

### Key Parameters

| Parameter | What It Controls | Default |
|-----------|-----------------|---------|
| `n_estimators` | Number of trees | 100–500 |
| `max_depth` | Maximum depth of each tree | None (grow fully) |
| `max_features` | Features considered at each split | √p (classification), p/3 (regression) |
| `min_samples_leaf` | Minimum observations per leaf | 1 |

### Feature Importance

Random Forests rank features by their contribution to prediction accuracy:

```
Feature Importance (from a churn model):

Monthly Charges   ████████████████████  0.28
Contract Length   ███████████████       0.22
Support Tickets   ██████████████        0.19
Tenure            ██████████            0.14
Internet Service  ████████              0.11
Payment Method    ███                   0.06
```

This is calculated by measuring how much each feature reduces impurity across all trees.

### Random Forest vs Regression

| Aspect | Regression | Random Forest |
|--------|-----------|--------------|
| **Interpretability** | High (coefficients) | Medium (feature importance) |
| **Non-linear patterns** | Needs manual specification | Captures automatically |
| **Interactions** | Must specify | Discovers automatically |
| **Performance ceiling** | Lower for complex patterns | Higher for complex patterns |
| **Explainability** | Full coefficient story | Feature ranking only |
| **Overfitting risk** | Low (if regularized) | Very low (ensemble) |

---

## Why Should a Data Analyst Care?

Because Random Forests are often the best "default" model for tabular business data. They handle non-linear patterns, interactions, and mixed data types without extensive preprocessing. When a stakeholder says "build me a prediction model," Random Forest is a strong starting point that rarely fails catastrophically.

---

## When to Use It

- **Tabular data** with mixed feature types (numerical + categorical)
- **When accuracy matters more than interpretability** — or when feature importance is sufficient
- **As a baseline** — before trying more complex models
- **When relationships are non-linear** — regression might miss the pattern

---

## Common Beginner Mistake

Treating Random Forests as "always better" than regression. For truly linear relationships, regression is more accurate, interpretable, and faster. Random Forests can also overfit on very small datasets. Also: interpreting feature importance as causal — it only measures predictive contribution, not causal effect.

---

## Real-World Example

An e-commerce company compares models for predicting customer lifetime value:

| Model | Train R² | Test R² | Features | Interpretability |
|-------|----------|---------|----------|-----------------|
| Linear Regression | 0.71 | 0.68 | 8 | Full coefficients |
| Ridge Regression | 0.69 | 0.69 | 8 (shrunk) | Full coefficients |
| Random Forest (200 trees) | 0.94 | 0.76 | 8 | Feature importance |

**Decision:** Random Forest wins on test accuracy (+7% over Ridge). The team uses Random Forest for automated predictions and keeps Ridge regression for stakeholder explanations. Both models agree on the top 3 features.

---

## 🔑 Key Takeaway

> Random Forests combine the strengths of many decision trees while averaging out their weaknesses. They're accurate, robust, and handle messy data well. Use them when prediction accuracy matters — but keep regression for when you need to explain *why*.

---

[← Day 87: Decision Trees](day-87-decision-trees.md) · [Next: Day 89 – Model Evaluation Metrics →](day-89-evaluation-metrics.md)
