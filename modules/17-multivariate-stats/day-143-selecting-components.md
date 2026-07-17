# Day 143: Selecting Components

*You compressed your data from 50 variables to 50 principal components. Now, how do you decide where to cut the thread and drop the rest?*

---

## Learning Objective

Determine the optimal number of principal components to retain using the Kaiser Criterion, Scree Plots, and Cumulative Variance Explained thresholds.

---

## The Problem This Solves

PCA creates as many principal components as there are variables in your dataset. If you start with 20 columns, PCA gives you 20 components. If you keep all 20, you haven't reduced dimensionality at all. You need a systematic, evidence-based method to select the top `k` components that capture the signal and discard the rest.

---

## The Concept

### The Selection Criteria

We use three main techniques to decide how many components to keep:

#### 1. Cumulative Variance Explained (Threshold Method)
Keep enough components to capture a target percentage of the total variance in the dataset (usually **70% to 80%**).

#### 2. The Kaiser Criterion (Eigenvalue Rule)
Keep only components with an **eigenvalue greater than 1.0**. 
*Rationale:* A component with an eigenvalue of 1.0 explains exactly as much variance as one single standardized original variable. If a component explains *less* than 1.0, it is explaining less variance than a raw column — discard it.

#### 3. The Scree Plot (Elbow Method)
A line plot of the eigenvalues of each component, ordered from largest to smallest. Look for the "elbow" — the point where the curve flattens out. Keep all components *before* the elbow.

```
Eigenvalue
  ▲
 5│  ● (PC1)
 4│
 3│     ● (PC2)
 2│
 1│───────●─────────●─────────●──────► Kaiser Limit (Eigenvalue = 1.0)
 0│          (PC3)     (PC4)     (PC5)
  └───────────────────────────────► Component
              ▲
            Elbow (Keep PC1 and PC2; drop the rest)
```

---

## Why Should a Data Analyst Care?

Because model simplicity is a business requirement. If you present a model that uses 15 principal components, stakeholders will find it complex and hard to manage. If you can show a Scree plot proving that just 2 components capture 78% of the information, you justify a simpler, cheaper, and more robust operational model.

---

## Common Beginner Mistake

Keeping components blindly based on one rule. Sometimes the Kaiser criterion says keep 5 components, but the Scree plot elbow is at 2, and 2 components explain only 45% of the variance. 

Always look at all three criteria together. If 2 components explain 70% of the variance and represent the elbow, that is your selection, even if Kaiser suggests more.

---

## Real-World Example

A survey analyst evaluates a customer satisfaction survey with 12 questions. They run PCA:

| Component | Eigenvalue | Variance Explained (%) | Cumulative Variance (%) |
|-----------|------------|------------------------|-------------------------|
| **PC1** | 4.82 | 40.2% | 40.2% |
| **PC2** | 2.15 | 17.9% | 58.1% |
| **PC3** | 1.10 | 9.2% | **67.3%** |
| PC4 | 0.85 | 7.1% | 74.4% |
| PC5 | 0.62 | 5.2% | 79.6% |

**Evaluation:**
- **Kaiser Criterion:** Keep PC1, PC2, and PC3 (all have eigenvalues > 1.0).
- **Cumulative Variance:** Keeping 3 components captures 67.3% of the variance (near our 70% target).
- **Scree Plot:** The line flattens out starting at PC4.

**Decision:** Retain the first **3 principal components**. Drop the remaining 9. The dataset is successfully compressed by 75% (from 12 columns to 3) while preserving 67.3% of the survey information.

---

## 🔑 Key Takeaway

> Select the optimal number of principal components by balancing the Kaiser Criterion (eigenvalues > 1.0), the Scree Plot elbow, and cumulative variance targets (70-80%). Simpler models generalize better.

---

[← Day 142: What is PCA?](day-142-what-is-pca.md) · [Next: Day 144 – Eigenvalues, Eigenvectors, and Loadings →](day-144-eigenvalues-eigenvectors.md)
