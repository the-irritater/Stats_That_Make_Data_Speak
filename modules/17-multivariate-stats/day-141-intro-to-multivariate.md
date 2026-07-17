# Day 141: What is Multivariate Statistics?

*Univariate statistics looks at one variable. Bivariate looks at two. Multivariate looks at the entire web of relationships simultaneously.*

---

## Learning Objective

Understand what multivariate statistics is, differentiate between univariate, bivariate, and multivariate analysis, and identify business problems that demand multivariate methods.

---

## The Problem This Solves

You want to evaluate a marketing campaign. You track:
1. Website signups (yes/no)
2. Average order value (AOV) ($)
3. Time spent on site (minutes)

If you run three separate tests (a Chi-Square on signups, a t-test on AOV, and a t-test on time), you suffer from **multiple comparisons error inflation** (Day 98) and miss the fact that these three outcomes are highly correlated with each other. 

Multivariate statistics analyzes all three dependent variables in a single, unified test, preserving the covariance structure.

---

## The Concept

### The Variable Classifications

```
  Univariate (1 Y):        Bivariate (1 X, 1 Y):      Multivariate (Multiple Xs and Ys):
     Y = sales                Y = sales, X = ads         Y₁, Y₂ = sales, retention
                                                         X₁, X₂ = ads, price, season
```

### Key Differences

| Aspect | Univariate / Bivariate | Multivariate |
|--------|------------------------|--------------|
| **Dependent Variables (Y)** | Exactly one (e.g. sales) | Two or more (e.g. sales, retention, satisfaction) |
| **Independent Variables (X)** | One or more | One or more |
| **Mathematical Engine** | Scalar algebra, simple variance | Linear algebra, matrices, covariance matrices |
| **Considers** | Individual column distributions | The **covariance** (overlapping relationships) among columns |
| **Error Control** | Susceptible to Type I error inflation | Controls family-wise error across multiple outcomes |

### The Covariance Matrix (Σ)

The mathematical heart of multivariate statistics. For `p` variables, it is a `p x p` matrix showing the variance of each variable on the diagonal, and the covariance between variables on the off-diagonal:

```
          Variable 1 | Variable 2 | Variable 3
Variable 1 |  Var(1)  |  Cov(1,2)  |  Cov(1,3)
Variable 2 |  Cov(2,1)|  Var(2)    |  Cov(2,3)
Variable 3 |  Cov(3,1)|  Cov(3,2)  |  Var(3)
```

By decomposing this covariance matrix, we extract components, factors, and multivariate tests.

---

## Why Should a Data Analyst Care?

Because real business outcomes are multi-dimensional. Customer loyalty is not measured by a single column; it is a composite of purchase frequency, lifetime value, survey scores, and app usage. If you only know univariate stats, you will simplify these variables into single averages, losing the rich patterns hidden in their correlations.

---

## Common Beginner Mistake

Running multiple regression and calling it "multivariate statistics." Multiple regression has multiple independent variables (Xs) but only **one** dependent variable (Y). That is **multiple univariate** analysis. True multivariate statistics has multiple dependent variables (Ys) modeled simultaneously (e.g. MANOVA).

---

## Real-World Example

A hotel chain wants to compare guest satisfaction across three locations:
- **Outcomes (Ys):** Room cleanliness score (1-5), Staff helpfulness score (1-5), Food quality score (1-5).
- **The wrong approach:** Run 3 separate ANOVAs. This inflates the false positive rate and ignores the fact that a guest who rates cleanliness highly is likely to rate staff highly (correlated errors).
- **The multivariate approach:** Run a **MANOVA** (Multivariate Analysis of Variance) to test if the vector of all three scores differs across locations in a single step.

---

## 🔑 Key Takeaway

> Multivariate statistics models multiple dependent variables simultaneously. It relies on the covariance matrix to control family-wise error rates and capture overlapping relationships that univariate models miss.

---

[← Module 17 README](README.md) · [Next: Day 142 – What is PCA? →](day-142-what-is-pca.md)
