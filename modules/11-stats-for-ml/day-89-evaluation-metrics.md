# Day 89: Model Evaluation Metrics

*Accuracy is the most popular metric in machine learning — and often the most misleading.*

---

## Learning Objective

Learn the key metrics for evaluating regression and classification models, understand when accuracy fails, and know which metric to choose based on the business problem.

---

## The Problem This Solves

Your fraud detection model has 99% accuracy. Impressive? Not if only 1% of transactions are fraud — a model predicting "not fraud" for everything also scores 99%. Choosing the right metric means measuring what actually matters.

---

## The Concept

### Regression Metrics

| Metric | What It Measures | When to Use |
|--------|-----------------|-------------|
| **R²** | Proportion of variance explained | Comparing models on same data |
| **MAE** | Average magnitude of errors | When all errors matter equally |
| **RMSE** | Average error, penalizes large ones | When large errors are costly |
| **MAPE** | Error as percentage | When relative error matters |

### Classification Metrics

#### The Confusion Matrix

```
                    Predicted
                  Pos      Neg
Actual  Pos  [   TP    |   FN   ]
        Neg  [   FP    |   TN   ]
```

| Metric | Formula | What It Answers |
|--------|---------|----------------|
| **Accuracy** | (TP + TN) / Total | How often correct overall? |
| **Precision** | TP / (TP + FP) | Of predicted positives, how many are correct? |
| **Recall** | TP / (TP + FN) | Of actual positives, how many did we catch? |
| **F1 Score** | 2 × (P × R) / (P + R) | Balance between precision and recall |
| **AUC-ROC** | Area under ROC curve | Overall discriminative ability |

### When Accuracy Fails

| Scenario | Majority Class | Accuracy of "Predict Majority" | Better Metric |
|----------|---------------|-------------------------------|---------------|
| Fraud detection | 99% legitimate | 99% | Precision, Recall |
| Disease screening | 95% healthy | 95% | Recall |
| Spam filtering | 80% not spam | 80% | F1 Score |

### The Precision-Recall Tradeoff

| Business Need | Optimize For | Accept Trade-off |
|--------------|-------------|-----------------|
| Don't block real emails | **Precision** | Miss some spam |
| Don't miss cancer cases | **Recall** | More false alarms |
| Balance needed | **F1 Score** | Moderate both |

### Connecting to Statistics

| Statistical Metric | ML Equivalent |
|-------------------|--------------|
| R² | R² (same!) |
| Residual standard error | RMSE |
| Type I Error (false positive) | 1 - Precision |
| Type II Error (false negative) | 1 - Recall |
| Statistical Power | Recall (in detection context) |

---

## Why Should a Data Analyst Care?

Because the metric you optimize defines what the model learns. Optimizing accuracy on imbalanced data means the model ignores the minority class. The right metric aligns the model with the business objective.

---

## When to Use Which

| Business Goal | Metric |
|--------------|--------|
| Forecast revenue | RMSE or MAE |
| Detect fraud | Precision + Recall |
| Rank customers by likelihood | AUC-ROC |
| Minimize percentage error | MAPE |
| Compare regression models | R² + Adjusted R² |

---

## Common Beginner Mistake

Reporting only one metric. R² can be high while RMSE is unacceptable in dollar terms. Accuracy can be 95% while recall is 0% for the class you care about. Always report multiple complementary metrics and interpret them together.

---

## Real-World Example

A bank's loan default model:

| Metric | Value | What It Means |
|--------|-------|---------------|
| Accuracy | 94% | Looks great... |
| Precision | 72% | 28% of flagged defaults are false alarms |
| Recall | 45% | Missing 55% of actual defaults |
| F1 | 0.55 | Poor balance |

The bank loses money on every missed default. They retrain optimizing for recall, accepting more false alarms (manual reviews) to catch more actual defaults.

---

## 🔑 Key Takeaway

> The right metric depends on the cost of being wrong. Accuracy hides problems on imbalanced data. Precision and recall reveal them. Always ask: "What happens when my model makes a mistake?" — then choose the metric that measures that cost.

---

## See It Applied

→ [Predicting customer spend](../../applied/notebooks/04-predicting-customer-spend.ipynb) — RMSE and R² evaluation
→ [Is this campaign actually working?](../../applied/notebooks/07-is-campaign-working.ipynb) — Evaluating treatment effects

---

[← Day 88: Random Forests](day-88-random-forests.md) · [Next: Day 90 – Machine Learning Mini Project →](day-90-ml-mini-project.md)
