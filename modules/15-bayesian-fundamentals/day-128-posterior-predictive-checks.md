# Day 128: Posterior Predictive Checks (Checking Bayesian Models)

*A model is a simplification of reality. A posterior predictive check asks: "Does our simplified model actually resemble the reality we observed?"*

---

## Learning Objective

Perform Posterior Predictive Checks (PPCs) to validate Bayesian models, compare simulated data against observed distributions, and diagnose model fit.

---

## The Problem This Solves

You build a Bayesian model to predict customer order sizes. The math is elegant, and the parameters converge. But when you look closely, your model assumes a normal distribution, while real order sizes have a massive spike at zero (users browsing without buying) and a long tail of high spend. 

If you use this model, your forecasts will be useless. Posterior predictive checks expose these structural mismatches by comparing your model's simulations against the actual raw data.

---

## The Concept

### What is a Posterior Predictive Check (PPC)?

A PPC simulates new datasets (`y_rep`) using the posterior distributions estimated by your model, and plots them alongside your actual observed data (`y`).

```
If the model fits the data:     Simulated data (y_rep) matches the shape of observed data (y).
If the model is broken:         Simulated data looks completely different from observed data.
```

### The Visual Check

```
Good Fit:                               Bad Fit (e.g. skewness missed):

  Density                                Density
   ▲                                      ▲
   │      Observed (y)                    │      Observed (y)
   │        ┌───┐                         │        ┌───┐
   │       ╱  │  ╲                        │       ╱     ╲
   │      ╱ - - - ╲  ← Simulations        │      ╱  - - - ╲  ← Simulations
   │     ╱ - - - - ╲   (y_rep)            │     ╱ - - - - - ╲  (missed skew)
   └─────────────────────────►            └─────────────────────────►
              Value                                  Value
```

### Step-by-Step PPC Workflow

```
1. Fit the Bayesian model on observed data (y)
          ↓
2. Draw parameter values (θ) from the posterior distribution
          ↓
3. Generate simulated datasets (y_rep) using those parameters
          ↓
4. Compare y_rep against y using plots (density, histograms)
          ↓
5. Check summary statistics (e.g., does the mean or min of y_rep match y?)
```

### Key Metrics to Audit

- **Extreme values:** Does the model generate negative prices if actual prices are always positive?
- **Sparsity:** Does the model match the proportion of zeros in the data?
- **Spread:** Does the variance of the simulated data match the actual variance?

---

## Why Should a Data Analyst Care?

Because business stakeholders will challenge your models. If you forecast inventory, and your model predicts a negative stock requirement on some days, the operations team will lose trust. Running PPCs allows you to catch and fix these structural issues before deploying the model.

---

## Common Beginner Mistake

Only evaluating parameter convergence (e.g. checking R-hat or trace plots) and skipping the predictive check. A model can converge perfectly on parameters while describing a distribution that makes zero sense for your data. Always plot simulated data against actual observed data.

---

## Real-World Example

A subscription service models customer support tickets per user:
- **Model A (Poisson prior):** Assumes standard count distribution.
- **PPC Diagnosis:** Observed data has 80% zeros (users who never file a ticket). Model A's simulated data only generates 30% zeros and predicts many users filing 1.5 tickets.
- **Action:** Reject Model A. Switch to a **Zero-Inflated Poisson (ZIP)** model, which explicitly models the excess zeros. The new PPC shows a perfect visual match.

---

## 🔑 Key Takeaway

> Posterior predictive checks validate models by comparing simulated datasets against actual observations. If the simulated shapes don't match the observed data, your model is structurally flawed — adjust your priors or likelihood family.

---

[← Day 127: Bayesian Regression](day-127-bayesian-regression.md) · [Next: Day 129 – Bayesian Case Study →](day-129-bayesian-case-study.md)
