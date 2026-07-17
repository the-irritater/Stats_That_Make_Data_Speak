# Day 139: Case Study: E-commerce Bayesian A/B Test

*One conversion test. Two variants. Zero p-values. This is how you run and report a Bayesian experiment.*

---

## Learning Objective

Integrate Bayesian A/B testing concepts — posteriors, probability of being best, expected loss, and stopping rules — to analyze a real-world checkout conversion experiment.

---

## The Business Challenge

An e-commerce site wants to test a "One-Click Checkout" button (Variant B) against their standard multi-step checkout (Control A).

**Business targets:**
- **Primary Metric:** Checkout conversion rate.
- **Baseline Conversion (Control):** ~8.0%.
- **Epsilon (ε) threshold of caring:** 0.1% absolute conversion rate loss.
- **Prior:** Weakly informative **Beta(8, 92)** (Mean = 8%, reflects baseline but with low confidence).

---

## The Experiment Lifecycle

### Day 5 (Intermediate Peek)
Traffic is monitored daily.

- **Control (A):** n = 4,200, conversions = 336.
  - Posterior: `Beta(8 + 336,  92 + 3864) = Beta(344, 3956)` (Mean = 8.0%)
- **Treatment (B):** n = 4,180, conversions = 376.
  - Posterior: `Beta(8 + 376,  92 + 3804) = Beta(384, 3896)` (Mean = 9.0%)

**Metrics via Monte Carlo Simulation (100K runs):**
- **P(B is Best):** 94.1%
- **Expected Loss L(B):** 0.14% (0.0014 absolute)

**Decision:** Keep running. While B is leading (94.1% win probability), the **Expected Loss (0.14%) is still above our threshold of caring (0.10%)**. The risk of error is too high to stop.

---

### Day 10 (Final Evaluation)
More traffic has arrived.

- **Control (A):** n = 9,500, conversions = 760.
  - Posterior: `Beta(8 + 760,  92 + 8740) = Beta(768, 8832)` (Mean = 8.0%)
- **Treatment (B):** n = 9,450, conversions = 926.
  - Posterior: `Beta(8 + 926,  92 + 8524) = Beta(934, 8616)` (Mean = 9.8%)

**Metrics via Monte Carlo Simulation (100K runs):**
- **P(B is Best):** 99.8%
- **Expected Loss L(B):** 0.01% (0.0001 absolute)

**Decision:** **Stop the test and roll out Variant B.** 
- The probability of B being best is near-certain (99.8%).
- The **Expected Loss (0.01%) is well below our threshold of caring (0.10%)**. The risk of making an error is practically zero.

```
Posterior distributions on Day 10:

  Density
   ▲
   │        Control (A)           Treatment (B)
   │           ┌───┐                  ┌───┐
   │          ╱  │  ╲                ╱  │  ╲
   │         ╱   │   ╲              ╱   │   ╲
   └─────────┴───┴───┴──────────────┴───┴───┴───────►
            7.5% 8.0% 8.5%         9.3% 9.8% 10.3%  (Conversion Rate)
```

---

## Executive Report (Day 117)

You present these findings to the leadership team:

- **What we found:** The One-Click Checkout (Variant B) increased checkout conversion rates from **8.0% to 9.8%**.
- **The confidence:** We are **99.8% certain** that Variant B outperforms the Control.
- **The risk:** The expected conversion loss if this decision is wrong is **0.01%** (well below our safety limit of 0.1%).
- **Financial impact:** At our average order value ($45) and weekly checkout traffic (20,000 users), this 1.8% conversion lift will generate an **estimated $16,200 in additional weekly revenue**.
- **Recommendation:** Deploy Variant B to 100% of traffic immediately.

---

## 🔑 Key Takeaway

> Bayesian A/B testing allows you to make decisions based on risk. By stopping the test when Expected Loss falls below your safety threshold (ε), you protect the business from revenue damage while maximizing development speed.

---

[← Day 138: Peeking in Bayesian A/B Tests](day-138-peeking-in-bayesian-ab.md) · [Next: Day 140 – Module Recap →](day-140-bayesian-ab-recap.md)
