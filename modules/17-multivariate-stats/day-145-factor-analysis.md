# Day 145: Factor Analysis

*PCA compresses data to explain variance. Factor Analysis models data to find the hidden constructs that cause the variance.*

---

## Learning Objective

Understand the conceptual differences between PCA and Factor Analysis, identify when to use each, and learn the role of latent variables and unique variance.

---

## The Problem This Solves

You want to measure "Brand Trust." You cannot measure trust directly (it's not a database column). You ask 5 survey questions about honesty, reliability, safety, quality, and recommendations. 

If you use PCA, you are simply summarizing the variance of those 5 columns. If you use Factor Analysis, you are modeling the theory that an unobserved, hidden trait ("Brand Trust") **causes** the answers to those 5 questions. Factor Analysis isolates the common cause.

---

## The Concept

### PCA vs. Factor Analysis (EFA)

While they look similar (both reduce dimensions), they have opposite mathematical structures:

#### PCA (Principal Component Analysis)
- **Goal:** Data compression. Explains maximum variance.
- **Direction:** Raw variables combine to create components: `X₁ + X₂ + X₃ → PC1`.
- **Assumption:** No measurement error model.

#### Factor Analysis (Exploratory Factor Analysis - EFA)
- **Goal:** Identify latent structure. Explains covariance among variables.
- **Direction:** Hidden factors cause the observed variables: `Latent Factor → X₁, X₂, X₃`.
- **Assumption:** Every variable has common variance (caused by the factor) and unique variance (error/noise).

```
PCA (Compression):                      Factor Analysis (Causal Latent Model):

  [ X₁ ] ──┐                                   [ X₁ ] ◄── [ Latent ] ──► [ X₂ ]
  [ X₂ ] ──┼─► [ Component ]                                 │
  [ X₃ ] ──┘                                                 ▼
                                                           [ X₃ ]
```

### The Factor Analysis Equation

For variable `Xᵢ`:

```
Xᵢ = λᵢ * F + eᵢ

Where:
  F  = Common Latent Factor
  λᵢ = Factor Loading (strength of effect of F on Xᵢ)
  eᵢ = Unique Variance (specific to Xᵢ, representing measurement error)
```

By separating `eᵢ` (unique variance/noise) from the common variance, Factor Analysis provides a purer estimate of the underlying construct than PCA, which mixes signal and noise.

---

## Why Should a Data Analyst Care?

Because many critical business concepts are latent variables: customer satisfaction, brand loyalty, employee engagement, user frustration, risk tolerance. You cannot measure these directly with a single metric. Factor Analysis is the standard statistical methodology for validating that your survey questions actually measure these hidden business drivers.

---

## When to Use Which

| Scenario | Better Choice | Why |
|-----------|--------------|-----|
| Eliminate multicollinearity before ML | **PCA** | Just need orthogonal columns; don't care about underlying theories. |
| Compress massive datasets | **PCA** | Computationally efficient, captures maximum variance. |
| Validate a customer satisfaction index | **Factor Analysis** | Need to prove a single latent construct (CSAT) drives the survey answers. |
| Separate measurement error from signal | **Factor Analysis** | Specifically models unique variance/error. |

---

## Common Beginner Mistake

Using PCA and claiming you found "latent factors." PCA does not model latent variables or measurement error. If you want to claim that your survey questions are caused by a hidden trait (e.g. "Customer Loyalty"), you must run Factor Analysis, not PCA.

---

## Real-World Example

A HR analyst runs an employee engagement survey with 4 questions:

1. "I am proud to work here."
2. "I recommend this company to others."
3. "I see myself here in 2 years."
4. "I like the office coffee."

**Factor Analysis Results:**
- Factor 1 ("Engagement") loads heavily (>0.75) on Questions 1, 2, and 3.
- Question 4 has a loading of 0.15 on Factor 1 and a **unique variance of 0.95**.

**Interpretation:** Questions 1, 2, and 3 are driven by the latent factor "Engagement." Question 4 ("office coffee") is noise specific to that question and should be excluded from the Engagement index. PCA would have struggled to isolate and ignore this specific noise column.

---

## 🔑 Key Takeaway

> PCA is for data compression; Factor Analysis is for identifying latent variables that cause the covariance in your data. Use Factor Analysis to measure unobservable business concepts (like loyalty or trust) while filtering out question-specific measurement error.

---

[← Day 144: Eigenvalues, Eigenvectors, and Loadings](day-144-eigenvalues-eigenvectors.md) · [Next: Day 146 – Exploratory vs. Confirmatory Factor Analysis →](day-146-efa-vs-cfa.md)
