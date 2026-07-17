# Day 142: What is PCA?

*Principal Component Analysis (PCA) is the ultimate data compressor. It collapses 50 correlated variables into 3 orthogonal axes without losing the information that matters.*

---

## Learning Objective

Understand Principal Component Analysis (PCA) as a dimensionality reduction technique, learn how it constructs orthogonal components, and explain why it is used to fix multicollinearity.

---

## The Problem This Solves

You want to predict credit risk. Your dataset has 100 features, including `number_of_debts`, `outstanding_balance`, `credit_limit_utilization`, and `times_delinquent`. Most of these features are highly correlated (multicollinearity). 

If you feed them directly into a linear model, the coefficients will be unstable and uninterpretable. PCA compresses these 100 correlated features into a few uncorrelated (orthogonal) components, giving you clean, stable inputs for your regression model.

---

## The Concept

### What is PCA?

PCA is an unsupervised technique that rotates your dataset's coordinate system to align with the directions of maximum variance. It transforms a set of correlated variables into a set of values of linearly uncorrelated variables called **principal components (PCs)**.

### Orthogonality (Uncorrelated Components)

Each principal component is perpendicular (orthogonal) to the others. This means they share zero correlation:

```
Correlation between PC1 and PC2 = 0
```

### The Visual Rotation

Imagine a 2D scatter plot of two correlated variables (e.g. age vs. income):

```
  Income
    ▲
    │          ●
    │       ●  / (PC1: Direction of maximum variance / spread)
    │     ●  /
    │   ●  /  ╲ (PC2: Perpendicular axis, capturing remaining variance)
    │ ●  /      ╲
    └──────────────────► Age
```

PCA rotates the axes so that:
- **PC1 (Principal Component 1):** Captures the longest axis of the data ellipse (maximum spread).
- **PC2 (Principal Component 2):** Captures the remaining spread, perpendicular to PC1.

If PC1 captures 90% of the total variance, we can drop PC2 entirely, reducing our dataset from 2 dimensions to 1 while retaining 90% of the information.

---

## Why Should a Data Analyst Care?

Because high-dimensional data is hard to visualize and model (the "curse of dimensionality"). PCA is the industry standard for:
1. **Data Visualization:** Compressing 10 variables to 2 (PC1 and PC2) so they can be plotted on a standard scatter plot.
2. **Preprocessing for ML:** Eliminating multicollinearity before regression or clustering.
3. **Data Compression:** Reducing database storage requirements by keeping only the top components.

---

## Common Beginner Mistake

Applying PCA without standardizing (scaling) the data first. PCA is highly sensitive to the scale of your variables. If `income` ranges from $0 to $100,000 and `age` ranges from 18 to 80, PCA will focus almost 100% of its variance capture on income because its numerical spread is larger. Always apply z-score standardization (Day 7) before running PCA.

---

## Real-World Example

A retail analyst has 20 customer behavior metrics (clicks, pages, add-to-carts, scrolls, shares, etc.):
- **The issue:** High collinearity. OLS regression fails VIF checks.
- **The PCA solution:** They run PCA on the 20 standardized columns.
  - PC1 captures 65% of variance (overall website activity).
  - PC2 captures 15% of variance (social sharing tendency).
  - Together, PC1 and PC2 explain **80% of the total variance**.

The analyst replaces the 20 noisy columns with these 2 principal components. The regression model is now stable, collinearity is eliminated, and the model generalizes to new datasets.

---

## 🔑 Key Takeaway

> PCA reduces dimensionality by rotating data coordinates to align with directions of maximum variance. It outputs orthogonal (uncorrelated) components, making it the default tool for fixing multicollinearity and compressing features.

---

[← Day 141: What is Multivariate Statistics?](day-141-intro-to-multivariate.md) · [Next: Day 143 – Selecting Components →](day-143-selecting-components.md)
