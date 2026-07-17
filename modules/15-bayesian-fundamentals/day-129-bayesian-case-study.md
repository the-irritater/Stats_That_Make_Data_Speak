# Day 129: Bayesian Case Study — Click-Through Rate Estimation

*How to estimate click-through rates for a new product category when you have almost no traffic.*

---

## Learning Objective

Integrate the Beta-Binomial conjugate model, prior specification, posterior updating, and credible intervals to solve a real-world click-through rate (CTR) estimation problem.

---

## The Business Challenge

An e-commerce platform launches a new niche product category: "Smart Gardening." 
- **The marketing VP** wants to know the click-through rate (CTR) of the category banner to estimate revenue.
- **The problem:** The banner has been live for only 3 days. It has received **40 views** and **0 clicks**.
- **The dilemma:** A frequentist estimate says CTR = 0/40 = 0%. If this is true, the category is dead. 

You must use a Bayesian model to provide a realistic CTR estimate and quantify the uncertainty.

---

## The Analysis Pipeline

### Step 1: Specifications of the Prior (Day 123)

We know this banner is similar to other niche category banners launched in the past. 
- **Historical benchmark:** Niche banner CTRs typically average **2.0%**, and rarely exceed 5%.
- **Setting the Prior (Beta Distribution):**
  - We want a Beta distribution with a mean of 0.02.
  - We choose **Prior = Beta(2, 98)**.
  - *Interpret as:* Equivalent to having observed 2 clicks in 100 views. This is a weakly informative prior that reflects our historical baseline.

### Step 2: Incorporate the Data (Day 124)

Over 3 days, we observe:
- **Views (n):** 40
- **Clicks (k):** 0
- **Failures (n - k):** 40

### Step 3: Calculate the Posterior (Day 126)

Using the Beta-Binomial update rule:
- `α_posterior = α_prior + k = 2 + 0 = 2`
- `β_posterior = β_prior + (n - k) = 98 + 40 = 138`
- **Posterior = Beta(2, 138)**

### Step 4: Parameter Estimation (Day 125)

We calculate the statistics of our posterior distribution `Beta(2, 140)`:
- **Mean (Expected CTR):** `α / (α + β) = 2 / (2 + 138) = 1.43%`
- **95% Credible Interval (Highest Density Interval):** `[0.17%, 3.75%]`

```
  Prior (Beta(2, 98)):                  Posterior (Beta(2, 138)):
  Mean = 2.0%                           Mean = 1.43% (95% Credible Interval: [0.17%, 3.75%])

   Density                               Density
    ▲                                     ▲
    │      /\                             │     /\
    │     /  \                            │    /  \
    │    /    \                           │   /    \
    └───────────────────►                 └───────────────────►
    0        0.02       1                 0       0.014       1
```

---

## Executive Communication (Day 117)

You present these findings to the marketing VP:

- **What we found:** The initial CTR estimate for the Smart Gardening banner is **1.43%**.
- **The range of uncertainty:** Because traffic is low (40 views), the true CTR plausibly lies between **0.17% and 3.75%** (95% Credible Interval). We can confidently state the CTR is *not* 0%.
- **The recommendation:** Keep the banner live. The 1.43% estimate is within our target performance range. Re-evaluate in two weeks when views reach 500 to narrow our uncertainty interval.

---

## 🔑 Key Takeaway

> When data is sparse (e.g. 0 clicks in 40 views), frequentist statistics output impossible 0% estimates with infinite margins. The Bayesian Beta-Binomial model leverages historical prior baselines to provide realistic estimates and actionable credible intervals.

---

[← Day 128: Posterior Predictive Checks](day-128-posterior-predictive-checks.md) · [Next: Day 130 – Module Recap →](day-130-bayesian-recap.md)
