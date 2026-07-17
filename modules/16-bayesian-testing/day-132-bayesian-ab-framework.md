# Day 132: The Bayesian A/B Testing Framework

*Frame your experiments with probability distributions, not single point estimates.*

---

## Learning Objective

Design a Bayesian A/B testing framework, understand how to model Control and Treatment parameters as joint posterior distributions, and explain the core outputs of a Bayesian test.

---

## The Problem This Solves

In frequentist testing, you compare two points (Control conversion rate = 4.2%, Treatment conversion rate = 4.8%) and run a hypothesis test to output a p-value. 

In the Bayesian framework, you compare **two distributions**. This allows you to compute the direct probability that the treatment is superior: `P(θ_B > θ_A | Data)`.

---

## The Concept

### The Bayesian A/B Setup

Instead of a null hypothesis, we model the parameters of both groups as probability distributions:

1. **Control Group (A):** Observed conversions `k_A` out of `n_A` visitors.
   - Posterior: `θ_A ~ Beta(α_prior + k_A,  β_prior + n_A - k_A)`
2. **Treatment Group (B):** Observed conversions `k_B` out of `n_B` visitors.
   - Posterior: `θ_B ~ Beta(α_prior + k_B,  β_prior + n_B - k_B)`

### The Joint Posterior Distribution

We construct a joint probability space of `θ_A` and `θ_B`. Since the groups are randomized, their distributions are independent:

```
P(θ_A, θ_B | Data) = P(θ_A | Data) * P(θ_B | Data)
```

We can visualize this joint space as a 3D landscape of likelihoods, where we want to know what portion of the landscape lies in the region where `θ_B > θ_A`.

```
    θ_B (Treatment)
      ▲
  1.0 │
      │          ╱ (Diagonal line where θ_B = θ_A)
      │        ╱
      │      ╱   ★ Region of Success: θ_B > θ_A
      │    ╱     (This is where we want our joint distribution to sit)
      │  ╱
      └────────────────────────► θ_A (Control)
     0                       1.0
```

### The Three Core Bayesian Outputs

| Output Metric | Formula / Calculation | Business Meaning |
|---------------|-----------------------|------------------|
| **Probability of Being Best** | `P(θ_B > θ_A)` | "There is a 94% chance that Variant B has a higher conversion rate than Control." |
| **Credible Interval of Lift** | Range of `(θ_B - θ_A) / θ_A` | "The new page is likely to drive a 3% to 12% relative conversion lift." |
| **Expected Loss (Risk)** | Expected value of `max(θ_A - θ_B, 0)` | "If we deploy Variant B and it is actually worse, we risk losing at most 0.02% in conversion." |

---

## Why Should a Data Analyst Care?

Because these outputs map directly to business logic. When you tell a stakeholder, *"There is a 94% chance B is better, and the expected loss if we make a mistake is less than 0.05%,"* they have all the information needed to evaluate risk and make a launch decision. This is far more useful than saying *"p = 0.03."*

---

## When to Use It

- **Product feature validation** — comparing UIs, copy, features
- **Pricing experiments** — testing price points while managing revenue risk
- **Continuous marketing testing** — updating banner CTRs daily
- **Small-traffic environments** — where frequentist tests take too long to run

---

## Common Beginner Mistake

Confusing `P(θ_B > θ_A) = 0.95` with "a 95% relative lift." `P(θ_B > θ_A)` is the *probability* that B is better than A, even if the difference is tiny. A model can be 99% certain that B is better than A, but the actual lift could be only 0.01%. Always look at the effect size (lift distribution) alongside the probability of success.

---

## Real-World Example

An analyst evaluates an A/B test with the following posteriors:
- **Control (A):** `Beta(40, 960)` (Mean = 4.0%)
- **Treatment (B):** `Beta(52, 948)` (Mean = 5.2%)

**Bayesian analysis results:**
- Expected Lift: +30% relative.
- Probability of Being Best: `P(θ_B > θ_A) = 0.945` (94.5%).

**Business Translation:** There is a 94.5% probability that Variant B has a higher conversion rate than Control, with an expected relative lift of 30%. This is highly actionable evidence for the product team.

---

## 🔑 Key Takeaway

> The Bayesian A/B testing framework compares posterior distributions instead of point estimates. It outputs direct, intuitive probabilities like "the probability that B is better than A," aligning statistical findings with business decision-making.

---

[← Day 131: Why Frequentist A/B Testing Fails in Business](day-131-why-frequentist-ab-fails.md) · [Next: Day 133 – Probability of Being Best →](day-133-probability-of-being-best.md)
