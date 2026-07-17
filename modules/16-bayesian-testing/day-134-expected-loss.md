# Day 134: Expected Loss & Risk Metrics

*Statistical significance tells you if there is a difference. Expected loss tells you the financial risk of making a mistake.*

---

## Learning Objective

Understand Expected Loss in Bayesian A/B testing, calculate the risk of rolling out a treatment variant, and use it as a stopping criterion for business experiments.

---

## The Problem This Solves

Your A/B test shows Variant B is outperforming Control. The product manager asks: *"If our test is wrong, and Variant B is actually worse than Control, how much conversion rate do we risk losing by rolling it out?"* 

Frequentist p-values cannot answer this. They only tell you if a difference is "significant," not its magnitude or risk. Expected Loss calculates the exact mathematical risk of making a mistake, allowing the business to set clear safety thresholds.

---

## The Concept

### What is Expected Loss?

The **Expected Loss** (risk metric) is the average amount by which we expect to decrease our performance if we choose Variant B and it turns out to be inferior to Control (A).

If `θ_B` is actually greater than `θ_A`, our loss is 0. If `θ_A` is greater than `θ_B`, our loss is `θ_A - θ_B`.

### The Mathematical Formula

```
Expected Loss L(B) = E[ max(θ_A - θ_B, 0) ]

Estimated via Monte Carlo simulation:
L(B) = (1 / N) * Σ max(θ_A_i - θ_B_i, 0)
```

### The Stopping Rule (Decision Threshold)

Instead of waiting for a p-value to cross 0.05, we stop a Bayesian test when our expected loss drops below a pre-specified threshold `ε` (epsilon):

```
Stop the test and roll out B if: L(B) < ε

Where ε is the threshold of caring (e.g. 0.0005, or a 0.05% conversion loss).
```

If the risk of rolling out B is trivially small, we stop the test and deploy — even if the p-value is not significant. We are safe to launch because the worst-case scenario is business-as-usual.

```
Expected Loss L(B)
  ▲
  │  ● (Day 1: High risk of error)
  │   ╲
  │    ● (Day 5: Risk dropping)
  │     ╲
  │──────●───────────────────────────► Epsilon Threshold (ε = 0.05%)
  │       ╲  ● (Day 12: STOP test and launch B - risk is negligible)
  └───────────────────────────────────► Time (n)
```

---

## Why Should a Data Analyst Care?

Because businesses run on risk management, not statistical purity. If an experiment has an expected loss of $5/month, keeping the test running for three more weeks to hit a frequentist sample size costs more than the risk of deploying a winner. Expected Loss allows you to make economically rational decisions.

---

## When to Use It

- **A/B test stopping criteria** — the modern standard in tech companies (VWO, Optimizely use expected loss)
- **High-stakes experiments** — where rolling out a bad variant has major cost implications (e.g., checkout flows)
- **Pricing optimization** — calculating the revenue risk of price increases

---

## Common Beginner Mistake

Setting the threshold of caring (`ε`) to zero. Expected loss will never reach exactly zero because there is always some theoretical uncertainty in continuous probability distributions. You must define a realistic `ε` based on what the business considers "too small to care about."

---

## Real-World Example

An analyst evaluates a subscription checkout flow test (baseline = 5.0%):
- **Epsilon (ε) threshold:** 0.05% (0.0005 absolute conversion rate loss).

**Test Results (Monte Carlo evaluation):**
- **P(B is Best):** 89.2%
- **Expected Loss L(B):** 0.03% (0.0003 absolute).

**Decision:** Stop the test and roll out Variant B. 
- While the probability of B being best (89.2%) is below the typical 95% threshold, the **expected loss (0.03%) is below our threshold of caring (0.05%)**. 
- Even if Variant B is actually worse, the estimated damage to our conversion rate is negligible. The business risk is covered.

---

## 🔑 Key Takeaway

> Expected Loss measures the risk of rolling out a variant if it turns out to be worse than Control. Stop tests when the expected loss drops below a business threshold of caring (ε), optimizing for speed and safety over abstract significance.

---

[← Day 133: Probability of Being Best](day-133-probability-of-being-best.md) · [Next: Day 135 – Bayesian Decision Theory →](day-135-bayesian-decision-theory.md)
