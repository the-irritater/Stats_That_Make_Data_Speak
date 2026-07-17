# Day 82: Supervised vs Unsupervised Learning

*Every ML problem starts with one question: do you have the answer key, or don't you?*

---

## Learning Objective

Understand the two fundamental paradigms in machine learning — supervised and unsupervised learning — and know when to use each based on your data and business question.

---

## The Problem This Solves

You have data and want the machine to learn patterns. But the approach depends on whether your data includes the outcome:

- **You have labeled outcomes** (e.g., "churned" / "retained") → **Supervised Learning**
- **You don't have labels** (e.g., "find groups in this customer base") → **Unsupervised Learning**

---

## The Concept

### Supervised Learning

The model learns from **labeled examples** — input-output pairs where the correct answer is known.

| Task | Input (X) | Output (Y) | Algorithm Examples |
|------|-----------|------------|-------------------|
| **Regression** | House features | Price ($) | Linear Regression, Decision Tree, Random Forest |
| **Classification** | Customer features | Churn (yes/no) | Logistic Regression, Decision Tree, Random Forest |

### Unsupervised Learning

The model finds **hidden structure** without any labels.

| Task | Input | Output | Algorithm Examples |
|------|-------|--------|-------------------|
| **Clustering** | Customer behavior | Group assignments | K-Means, DBSCAN |
| **Dimensionality Reduction** | Many features | Compressed representation | PCA, t-SNE |

### The Connection to Statistics

| ML Paradigm | Statistical Equivalent |
|-------------|----------------------|
| Supervised regression | Linear/logistic regression (Module 10) |
| Supervised classification | Discriminant analysis, logistic regression |
| Unsupervised clustering | Mixture models, RFM segmentation |

You already did supervised learning in Module 10 (regression) and unsupervised learning in your Signature Project (RFM clustering). ML formalizes what you've been doing.

---

## Why Should a Data Analyst Care?

Choosing wrong wastes months. If your question has a measurable target (predict churn, forecast sales), use supervised learning. If you're exploring ("what types of customers do we have?"), use unsupervised. Mixing them up leads to models that answer the wrong question.

---

## Common Beginner Mistake

Treating clustering output as ground truth. K-Means will always give you clusters — even if the data has no natural groups. Always validate that clusters make business sense. Compare cluster profiles and test whether they predict meaningful outcomes.

---

## Real-World Example

An e-commerce company uses both approaches:

1. **Predict which customers will churn** → Supervised (classification). Train on historical data where you know who churned.
2. **Discover natural customer segments** → Unsupervised (clustering). Feed in purchase behavior and let K-Means find groups.

Same data. Different questions. Different methods.

---

## 🔑 Key Takeaway

> Supervised learning predicts known outcomes. Unsupervised learning discovers unknown patterns. The right choice depends on whether you have the answer key — not on which algorithm sounds more impressive.

---

## See It Applied

→ [Predicting customer spend](../../applied/notebooks/04-predicting-customer-spend.ipynb) — Supervised regression
→ [Who are our best buyers?](../../applied/notebooks/06-who-are-best-buyers.ipynb) — Unsupervised RFM segmentation

---

[← Day 81: Statistics vs Machine Learning](day-81-statistics-vs-ml.md) · [Next: Day 83 – Train/Test Split →](day-83-train-test-split.md)
