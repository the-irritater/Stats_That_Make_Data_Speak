# Day 127: Bayesian Regression

*Frequentist regression finds the single line that fits the data best. Bayesian regression finds a distribution of lines that fit the data likely.*

---

## Learning Objective

Understand how Bayesian linear regression applies prior distributions to regression coefficients, and explain how this stabilizes estimates (especially on small samples).

---

## The Problem This Solves

You fit a regression model with 10 features on only 50 rows of customer data. Because the sample size is small, OLS regression outputs highly unstable coefficients with massive standard errors — some coefficients might even take extreme, unrealistic values due to noise. 

Bayesian regression stabilizes these estimates by using prior distributions to "shrink" coefficients toward realistic values, preventing overfitting.

---

## The Concept

### The Conceptual Difference

- **Frequentist OLS:** Finds a single vector of coefficients `β` that minimizes the sum of squared residuals.
- **Bayesian Regression:** Estimates the **posterior distribution** of the coefficients `P(β | Data)` using Bayes' Theorem.

```
P(β | Data)  ∝  Likelihood(Data | β)  ×  Prior(β)
```

### The Role of the Prior on Coefficients

For each coefficient `βⱼ`, we define a prior distribution:

```
βⱼ  ~  Normal(μ_prior, σ_prior)
```

- **μ_prior (mean):** Usually set to 0. We assume the feature has no effect until proven otherwise.
- **σ_prior (standard deviation / tightness):**
  - **Large σ (flat prior):** We let the data speak. Equivalent to standard OLS.
  - **Small σ (tight prior):** We pull the coefficient toward zero. This acts exactly like **regularization (Ridge/Lasso)**!

### The Connection to Regularization

| Prior Type | Regularization Equivalent | Effect on Coefficients |
|------------|---------------------------|------------------------|
| **Normal prior** centered at 0 | **Ridge Regression (L2)** | Shrinks coefficients toward zero, keeping all of them. |
| **Laplace prior** centered at 0 | **Lasso Regression (L1)** | Shrinks weak coefficients to exactly zero (feature selection). |

In Bayesian terms, regularization is not an ad-hoc penalty; it is simply the natural mathematical consequence of assuming a prior distribution around your coefficients.

---

## Why Should a Data Analyst Care?

Because business data is often small or collinear (highly correlated). When OLS regression fails (inflated coefficients, high VIF), Bayesian regression provides stable, generalizable estimates by leveraging informative priors (e.g., "we know price elasticity is typically negative").

---

## When to Use It

- **Small sample sizes** — prevents overfitting
- **High collinearity** — priors stabilize overlapping variables
- **Causal regression** — incorporating prior literature estimates as informative priors
- **When prediction intervals are needed** — Bayesian regression outputs a distribution of predictions, natively capturing model uncertainty

---

## Common Beginner Mistake

Using flat priors on small datasets. If you set wide, uninformative priors (e.g., `Normal(0, 1000)`), your Bayesian regression will yield the exact same unstable coefficients as OLS. The value of Bayesian regression on small data comes from using weakly informative priors (e.g., `Normal(0, 1)`) to stabilize the model.

---

## Real-World Example

Predicting customer spend from age and marketing clicks on a small cohort (n = 30):

```
OLS Model:
Spend = 12.0 + 45.2 × (Clicks)
(Standard Error of Clicks = 25.1, p = 0.08)
Interpretation: The effect of clicks is huge ($45) but highly unstable.

Bayesian Model (Prior on Clicks ~ Normal(0, 5)):
Spend = 15.0 + 8.4 × (Clicks)
(95% Credible Interval: [2.1, 14.7])
Interpretation: The prior stabilized the coefficient to a realistic value ($8.40) with a stable, positive credible interval.
```

**Business Decision:** Rely on the Bayesian estimate. OLS overfit to a few high-clicking outliers in the small sample, yielding an unrealistic coefficient.

---

## 🔑 Key Takeaway

> Bayesian regression models coefficients as probability distributions rather than fixed points. By using priors centered at zero, it stabilizes estimates on small samples — acting as a natural, mathematically sound equivalent to Ridge and Lasso regularization.

---

[← Day 126: Bayesian Updating](day-126-bayesian-updating.md) · [Next: Day 128 – Posterior Predictive Checks →](day-128-posterior-predictive-checks.md)
