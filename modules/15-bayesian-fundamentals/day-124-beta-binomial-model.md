# Day 124: The Beta-Binomial Model

*When you combine a Beta prior with Binomial data, the posterior is just basic addition.*

---

## Learning Objective

Apply the Beta-Binomial conjugate model to estimate binary conversion rates, interpret the parameters (α, β) as pseudo-observations, and calculate posterior updates.

---

## The Problem This Solves

You want to estimate a conversion rate. The data is binary (success/failure), which means the likelihood is **Binomial**. 

If you use a general probability distribution for the prior, calculating the posterior requires dividing by the marginal likelihood, which involves solving complex integrals. The Beta-Binomial conjugate model solves this analytically. The posterior is calculated in a fraction of a millisecond using simple addition.

---

## The Concept

### The Beta Distribution

The Beta distribution is bounded between `[0, 1]`, making it the perfect prior for a probability or rate (like conversion rate `θ`). It is defined by two shape parameters:

- **α (alpha):** Interpret as "prior successes"
- **β (beta):** Interpret as "prior failures"

```
Beta Prior: Prior(θ) = Beta(α_prior, β_prior)
```

### The Update Rule

If you observe new data with `k` successes (conversions) out of `n` trials (visitors):

```
Likelihood: Binomial(k, n)
```

Because the Beta distribution is conjugate to the Binomial likelihood, the posterior distribution is also a Beta distribution:

```
Posterior(θ) = Beta(α_prior + k,  β_prior + (n - k))
```

To update your belief, you simply:
1. Add actual successes (`k`) to your prior successes (`α`).
2. Add actual failures (`n - k`) to your prior failures (`β`).

### Parameter Visualizations

```
Prior: Beta(2, 2)                     Updated: Beta(2 + 20, 2 + 80) = Beta(22, 82)
(Flat, high uncertainty)              (Narrow, centered near 21%)

 Probability                           Probability
  ▲                                     ▲
  │   ┌───┐                             │         █
  │  ╱     ╲                            │        █ █
  │ ╱       ╲                           │      ▄█   █▄
  └──────────────────►                  └──────────────────►
  0       0.5       1                   0       0.21       1
```

---

## Why Should a Data Analyst Care?

Because Binary events are the most common metrics in business: conversion rates, click-through rates, retention rates, email open rates, and defect rates. The Beta-Binomial model is the standard mathematical tool for modeling these rates.

---

## Common Beginner Mistake

Setting prior parameters (`α`, `β`) to zero. A `Beta(0, 0)` prior is an improper prior and causes the update to fail if you observe 0 conversions (division by zero). Always start with at least `Beta(1, 1)` (flat uninformative prior) or an informative prior based on historical baselines.

---

## Real-World Example

An analyst estimates the conversion rate of a new landing page:
- **Prior belief:** Historical conversion is ~5%. We set an informative prior: **Beta(5, 95)**. (Equates to 5 prior successes and 95 prior failures).
- **New Data:** We run a test with **200 visitors** and **15 conversions**.
  - Successes (k) = 15
  - Failures (n - k) = 185

**Calculate the Posterior Distribution:**
- `α_posterior = 5 + 15 = 20`
- `β_posterior = 95 + 185 = 280`
- `Posterior = Beta(20, 280)`

**Interpretation:**
- The expected conversion rate (mean of Beta) is: `α / (α + β) = 20 / (20 + 280) = 6.67%`.
- The raw conversion rate was 15/200 = 7.5%. The prior pulled the estimate slightly toward the historical baseline (6.67%), protecting the business from over-optimism on a small sample of 200 users.

---

## 🔑 Key Takeaway

> For binary rates, the Beta-Binomial model calculates updated beliefs instantly. Add actual successes to the prior's α parameter and actual failures to the prior's β parameter to get the updated posterior distribution.

---

[← Day 123: Understanding Priors](day-123-understanding-priors.md) · [Next: Day 125 – Posterior Estimation & Credible Intervals →](day-125-credible-intervals.md)
