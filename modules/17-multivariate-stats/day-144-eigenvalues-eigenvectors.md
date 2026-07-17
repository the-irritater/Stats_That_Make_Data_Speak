# Day 144: Eigenvalues, Eigenvectors, and Loadings

*Under the hood, PCA is just matrix decomposition. Eigenvectors show the direction, eigenvalues show the magnitude, and loadings show the correlation.*

---

## Learning Objective

Understand the mathematical foundations of PCA, define eigenvalues and eigenvectors, and interpret PCA factor loadings to explain what components mean in business terms.

---

## The Problem This Solves

You ran PCA and selected the top 2 components. You tell your manager: *"PC1 predicts customer spend."* 

The manager asks: *"But what actually IS PC1? What does it represent in the real world?"* 

If you don't understand factor loadings, you can't answer. Loadings show the correlation between your raw columns and the principal components, allowing you to translate abstract dimensions into business concepts.

---

## The Concept

### The Mathematical Engine

PCA decomposes the covariance matrix `Σ` of your dataset into eigenvalues and eigenvectors:

```
Σ * v = λ * v

Where:
  Σ = covariance matrix
  v = eigenvector (direction of the component axis)
  λ = eigenvalue (magnitude / variance captured by the component)
```

- **Eigenvector (v):** A vector of weights (coefficients) that defines the linear combination of raw features to create the component.
- **Eigenvalue (λ):** The amount of variance captured by that eigenvector. The sum of all eigenvalues equals the number of variables (if standardized).

### Component Loadings

A loading is the correlation between an original variable and a principal component. It ranges from `-1.0` (strongly negative correlation) to `+1.0` (strongly positive).

```
Loading = Eigenvector_weight * sqrt(Eigenvalue)
```

We map these loadings in a **Loading Matrix** to interpret the components:

| Original Variable | PC1 Loadings | PC2 Loadings |
|-------------------|--------------|--------------|
| `pages_visited` | **0.85** | -0.12 |
| `session_duration`| **0.82** | -0.10 |
| `shares_clicked` | 0.15 | **0.78** |
| `comments_left` | 0.18 | **0.75** |

### Interpreting the Components

Looking at the loadings above, we can name the abstract components:
- **PC1** has high loadings on `pages_visited` and `session_duration`. We label PC1: **"General Engagement"**.
- **PC2** has high loadings on `shares_clicked` and `comments_left`. We label PC2: **"Social Activity"**.

---

## Why Should a Data Analyst Care?

Because data compression is useless without interpretation. If you use principal components in a predictive model, you must be able to explain what the predictors represent. Loading matrices turn abstract mathematical vectors into concrete, nameable business dimensions.

---

## Common Beginner Mistake

Confusing **eigenvectors** (weights used to calculate component scores) with **loadings** (correlations between variables and components). While they are mathematically related, loadings are scaled by the component's variance (eigenvalue), making them the correct metric to use for interpretation.

---

## Real-World Example

A financial analyst runs PCA on 4 economic indicators to build an index:

```
Eigenvalues: λ_1 = 2.84,  λ_2 = 0.85

Loading Matrix:
Variable             | PC1 Loading
─────────────────────┼─────────────
GDP Growth           |  0.88
Employment Rate      |  0.84
Consumer Confidence  |  0.79
Inflation Rate       | -0.12
```

**Interpretation:**
- PC1 captures 2.84 / 4 = 71% of the total variance.
- PC1 loads heavily and positively on GDP, Employment, and Confidence, and has near-zero correlation with Inflation.
- **Business translation:** PC1 represents **"Economic Momentum"**. The analyst can confidently use PC1 as a single index variable in corporate reports.

---

## 🔑 Key Takeaway

> Eigenvectors define the direction of PCA axes, and eigenvalues measure their variance magnitude. Use the loading matrix (correlations between raw variables and components) to translate abstract components into nameable business dimensions.

---

[← Day 143: Selecting Components](day-143-selecting-components.md) · [Next: Day 145 – Factor Analysis →](day-145-factor-analysis.md)
