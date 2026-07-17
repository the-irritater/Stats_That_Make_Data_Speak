# Day 138: Peeking in Bayesian A/B Tests

*In frequentist statistics, peeking at your data is a sin. In Bayesian statistics, peeking is the point.*

---

## Learning Objective

Understand why the Bayesian framework is immune to the frequentist "peeking penalty," and know the mathematical rules that protect Bayesian sequential decisions.

---

## The Problem This Solves

You launch a critical experiment. On day 2, conversions drop by 80% in the treatment group due to a bug. 
- **Under frequentist rules:** If you stop the test, you violate sample size assumptions. If you keep running, you lose thousands of dollars.
- **Under Bayesian rules:** You evaluate the posterior distribution immediately. The probability of B being best drops to 0%, and the expected loss surges. You stop the test immediately with complete statistical justification.

---

## The Concept

### Why Peeking Breaks Frequentist Tests

Frequentist testing relies on the **p-value**, which is calculated assuming a fixed, pre-specified sample size. If you look at the data early (peek) and stop the test if p < 0.05, you are increasing the number of times you test the hypothesis. 

Each test is a chance to roll a false positive. By day 10, your true false positive rate has ballooned (Day 131).

### Why Bayesian is Immune to Peeking

Bayesian statistics does not calculate p-values. It calculates the **posterior distribution** given the evidence *currently observed*. 

According to the **Likelihood Principle**, all the information about the parameter `θ` is contained in the observed data, regardless of *how* or *when* the investigator decided to stop the experiment.

```
Frequentist:  Significance depends on:  What data might have been observed in hypothetical repeated trials.
Bayesian:     Significance depends on:  The data that was actually observed up to this second.
```

### The Bayesian Stopping Boundary

Instead of a fixed sample size, a Bayesian test uses three indicators to decide when to stop:

| Metric | Condition to Stop | Decision |
|--------|-------------------|----------|
| **Expected Loss L(B)** | `L(B) < ε` (threshold of caring) | **Stop & Rollout B** (Risk of error is negligible) |
| **Expected Loss L(A)** | `L(A) < ε` | **Stop & Stick with A** (Treatment failed to beat Control) |
| **Max Duration Reached** | Time limit exceeded | **Stop & Declare Draw** (No meaningful difference found) |

You can check these metrics hourly. Peeking does not change the posterior distribution; it only updates it with more evidence.

---

## Why Should a Data Analyst Care?

Because business operations demand flexibility. Product managers check dashboards daily. If you force them to ignore the charts using frequentist warnings, they will lose faith in analytics. By using Bayesian stopping rules, you allow them to monitor experiments in real-time safely.

---

## Common Beginner Mistake

Stopping a Bayesian test early when sample sizes are tiny (e.g. under 100 users per group). While peeking doesn't inflate false positives mathematically, small samples are dominated by your prior. If you stop too early, the posterior is simply reflecting your prior assumptions, not real user behavior. Set a minimum sample threshold (e.g. 1,000 users) before applying stopping rules.

---

## Real-World Example

A SaaS app tests a new payment gate layout:
- **Baseline (Control):** 8.0% conversion.
- **Epsilon (ε) threshold:** 0.1%.
- **Day 2 (n = 200 per group):** Treatment has a bug, conversion drops to 2.0%.
  - **Bayesian check:** `L(A) = 0.01%` (below 0.1% threshold). The risk of keeping Control is near zero.
  - **Action:** Stop the test immediately and kill the bugged treatment.

---

## 🔑 Key Takeaway

> Bayesian A/B tests are immune to the peeking penalty because they adhere to the Likelihood Principle. You can monitor experiments continuously and stop as soon as Expected Loss falls below your business threshold of caring (ε).

---

[← Day 137: Thompson Sampling](day-137-thompson-sampling.md) · [Next: Day 139 – Case Study: E-commerce Bayesian A/B Test →](day-139-bayesian-ab-case-study.md)
