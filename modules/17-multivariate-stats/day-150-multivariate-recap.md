# Day 150: Module Recap

*10 days. One framework: map high-dimensional relationships, rotate coordinate space, select components, identify latent causes, and build indexes.*

---

## Learning Objective

Consolidate everything from Module 17 into a repeatable multivariate analysis workflow you can apply to any complex, high-dimensional dataset.

---

## What We Covered (Day 141–150)

| Day | Topic | Core Insight |
|-----|-------|-------------|
| 141 | What is Multivariate? | Models multiple dependent variables simultaneously using covariance |
| 142 | What is PCA? | Data compressor that rotates coordinates to maximize orthogonal variance |
| 143 | Selecting Components | Balance Scree plots, Kaiser (eigenvalues > 1), and cumulative variance |
| 144 | Eigenvalues & Loadings | Eigenvectors show direction; loadings show correlation with raw variables |
| 145 | Factor Analysis | Identifies latent/hidden causes of covariance, filtering unique noise |
| 146 | EFA vs. CFA | EFA discovers patterns; CFA tests theoretical path models |
| 147 | MANOVA | Compares group centroids across multiple continuous outcomes |
| 148 | Canonical Correlation | Measures correlation between two sets of variables |
| 149 | Case Study | Constructing a Customer Experience Index using PCA & Factor Analysis |

---

## The Multivariate Analysis Workflow

Use this framework when handling datasets with high dimensionality or multiple outcomes:

```
START: What is the goal of your analysis?
│
├── Compress dimensions / fix multicollinearity (Unsupervised)
│   └── PCA (Day 142)
│       ├── Check Kaiser Criterion (eigenvalues > 1) & Scree Plot
│       ├── Select top k components (Target 70-80% cumulative variance)
│       └── Interpret components using Loading Matrix (correlations)
│
├── Identify hidden constructs or validate a survey index (Latent Modeling)
│   └── Factor Analysis (Day 145)
│       ├── EFA to discover structure (exploratory)
│       └── CFA to validate theoretical mappings (confirmatory)
│
├── Compare group differences across multiple outcomes (Supervised)
│   └── MANOVA (Day 147)
│       ├── Check Pillai's Trace or Wilks' Lambda
│       └── If significant: run follow-up ANOVAs with Bonferroni adjustments
│
└── Measure correlation between two sets of variables (Correlation)
    └── Canonical Correlation Analysis (CCA) (Day 148)
```

---

## The Multivariate Checklist

Before presenting any compressed index or PCA model, verify these 4 points:

- [ ] **Standardization:** Did you scale (z-score) the features before running PCA/Factor Analysis?
- [ ] **Collinearity check:** Did you review the correlation matrix to ensure the features share enough covariance to reduce?
- [ ] **Component Names:** Have you interpreted and named the components based on the factor loadings, or did you leave them as abstract PC1/PC2?
- [ ] **Validation split:** If confirming a structure via CFA, did you use a separate holdout dataset?

---

## 🏆 Career Milestone 5: The Advanced Statistician

Congratulations on completing Day 150. 
**Your new milestone:** You can model continuous probability updates (Bayesian updating), run risk-based Bayesian experiments, and reduce high-dimensional corporate datasets using PCA, Factor Analysis, and Canonical Correlation.

---

## 🎯 Capstone Challenge 5: Bayesian & Dimensionality Analysis

Apply your Phase 2 skills to this practical challenge:

1. **Find a dataset:** Download a public customer feedback dataset containing demographic features and 10+ satisfaction questions.
2. **Dimension Reduction:** Standardize the survey columns. Run PCA and EFA. Choose the optimal number of components using the Kaiser criterion and a Scree plot. Name the components based on the factor loadings.
3. **Index Creation:** Build a single Customer Loyalty Index (CLI) from the factor scores.
4. **Bayesian Check:** Estimate the probability that new customers have a higher CLI than repeat customers using a Bayesian regression model with weakly informative priors.
5. **Report:** Write a 1-page executive summary translating the statistical findings into operational business recommendations.

---

[← Day 149: Case Study: Customer Experience Index](day-149-multivariate-case-study.md) · [Back to Module 17](README.md) · [Back to Main](../../README.md)
