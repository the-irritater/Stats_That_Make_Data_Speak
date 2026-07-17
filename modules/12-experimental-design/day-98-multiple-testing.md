# Day 98: Multiple Testing Problem

*If you test 20 different metrics in your A/B test at a 5% significance level, you are mathematically guaranteed to find a "significant" result — even if the changes did absolutely nothing.*

---

## Learning Objective

Understand how running multiple hypothesis tests inflates the family-wise error rate, and learn how to control false positives using the Bonferroni correction and False Discovery Rate (FDR).

---

## The Problem This Solves

A product team tests a landing page. They check conversion rate, average spend, bounce rate, email signups, page views, and 15 other metrics. They find that "average spend among mobile users on Tuesdays" has a p-value of 0.03. They celebrate and launch. Spend drops.

Why? They fell victim to the **multiple testing problem** (data dredging). Testing many hypotheses increases the chance of finding a false positive by pure random chance.

---

## The Concept

### Family-Wise Error Rate (FWER)

When you run a single test at `α = 0.05`, the probability of a false positive is 5%. If you run `m` independent tests, the probability of at least one false positive (FWER) is:

```
FWER = 1 - (1 - α)ᵐ

For m = 1 test:   FWER = 0.05  (5%)
For m = 5 tests:  FWER = 0.22  (22%)
For m = 20 tests: FWER = 0.64  (64%!)
```

At 20 tests, your false positive rate is 64%. You are no longer doing science; you are rolling dice.

### The Solutions

#### 1. Bonferroni Correction (Conservative)
Adjust the significance threshold α by dividing it by the number of tests `m`.

```
Adjusted α = α / m

With 20 tests:
  Adjusted α = 0.05 / 20 = 0.0025
```

A p-value must be below 0.0025 to be declared significant. 
*Tradeoff:* Very conservative. Reduces false positives but increases false negatives (misses real changes).

#### 2. Benjamini-Hochberg Procedure (FDR Control)
Instead of controlling the probability of *any* false positive, control the **proportion** of false positives among all declared discoveries.

```
Rank p-values from smallest to largest (i = 1 to m).
Find the largest rank i where: p_i ≤ (i / m) * Q

Where Q is the target False Discovery Rate (usually 10%).
Reject the null hypothesis for all tests ranked 1 through i.
```

*Advantage:* Higher statistical power than Bonferroni while keeping false discoveries under control.

---

## Why Should a Data Analyst Care?

Because metrics dashboards automatically track dozens of cuts (by browser, country, device, channel). If you report a win simply because one metric in one sub-segment had p < 0.05, you will damage your credibility when those wins fail to materialize in the company's financial statements.

---

## Common Beginner Mistake

Running a test, finding no effect on the primary metric, and then slicing the data by 50 different customer segments until finding one with p < 0.05. This is called **p-hacking** or subgroup dredging. If you perform subgroup analysis, you must pre-specify it or adjust the significance threshold.

---

## Real-World Example

A mobile game developer tests a new ad layout. They analyze 10 metrics (Retention, Revenue, Sessions, CTR, Ad views, Ad clicks, Level completions, Invites, Chat messages, Time spent):

- **Target α:** 0.05
- **Observation:** CTR has p = 0.02. All other metrics have p > 0.05.

**The Naive Approach:** Declare a win for CTR and rollout.
**The Rigorous Approach (Bonferroni):**
- Adjusted α = 0.05 / 10 = 0.005.
- Since CTR's p-value (0.02) is greater than the adjusted threshold (0.005), **fail to reject the null hypothesis**. The CTR lift is likely random noise.

---

## 🔑 Key Takeaway

> More metrics mean more false alarms. When testing multiple metrics or subgroups, you must adjust your significance threshold using Bonferroni or FDR. If you don't adjust, your "wins" are likely illusions.

---

## See It Applied

→ [Is this campaign actually working?](../../applied/notebooks/07-is-campaign-working.ipynb) — Implementing Bonferroni corrections on A/B metrics

---

[← Day 97: Power Analysis & Minimum Detectable Effect (MDE)](day-97-power-analysis-mde.md) · [Next: Day 99 – Business Experiment Case Study →](day-99-experiment-case-study.md)
