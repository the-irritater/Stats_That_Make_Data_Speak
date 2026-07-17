# Day 63: Paired t-Test

*When the same subjects are measured twice, you don't compare groups — you compare changes.*

---

## Learning Objective

Understand when and how to use a paired t-test, why it's more powerful than an independent t-test for before/after designs, and how to interpret the results for business decisions.

---

## The Problem This Solves

A company runs a training program and measures employee productivity before and after. Productivity improved from an average of 72 to 78. But is that a real improvement, or just natural variation?

You can't use an independent t-test here because the *same people* were measured twice. The paired t-test accounts for this by analyzing the *differences within each person*, removing individual variability.

---

## The Concept

### When to Use It

- The **same subjects** are measured at two time points (before/after)
- Or subjects are **matched** in pairs (e.g., twins, same store in different seasons)
- Outcome is **continuous**

### How It Works

Instead of comparing two group means, you:

1. Calculate the **difference** for each pair: dᵢ = After_i − Before_i
2. Test whether the **mean difference** (d̄) is significantly different from zero

### The Formula

```
t = d̄ / (s_d / √n)

Where:
  d̄   = mean of the differences
  s_d  = standard deviation of the differences
  n    = number of pairs
```

### The Hypotheses

- **H₀:** μ_d = 0 (no change on average)
- **H₁:** μ_d ≠ 0 (there is a change)

### Why Paired > Independent for Repeated Measures

| Aspect | Independent t-test | Paired t-test |
|--------|-------------------|---------------|
| **Compares** | Two group averages | Within-subject differences |
| **Controls for** | Nothing | Individual variability |
| **Power** | Lower (more noise) | Higher (less noise) |
| **Use when** | Different subjects | Same subjects, two time points |

By removing between-subject variability, the paired t-test detects smaller effects with the same sample size.

---

## Why Should a Data Analyst Care?

Because before/after comparisons are everywhere in business:

- Did the new website design improve session duration?
- Did the training program increase sales?
- Did the price change affect purchase volume?

Using an independent t-test on paired data wastes statistical power. Using a paired t-test on unpaired data violates assumptions. Choosing correctly is the difference between finding a real effect and missing it.

---

## When to Use It

- **Before/after studies** — same customers, employees, stores measured twice
- **Matched designs** — paired subjects (same demographics, same region)
- **Crossover studies** — each subject experiences both treatments

---

## Common Beginner Mistake

Treating paired data as independent. If 50 employees are measured before and after training, you have 50 pairs — not 100 independent observations. Using an independent t-test inflates the denominator and reduces your ability to detect real changes.

---

## Real-World Example

A SaaS company redesigns its onboarding flow and tracks task completion time for 40 users who experienced both the old and new flows:

| User | Old Flow (min) | New Flow (min) | Difference |
|------|---------------|----------------|------------|
| 1 | 12.3 | 9.1 | -3.2 |
| 2 | 15.7 | 14.2 | -1.5 |
| 3 | 8.9 | 9.4 | +0.5 |
| ... | ... | ... | ... |
| **Mean** | **11.8** | **9.6** | **-2.2** |

**Paired t-test results:**
- t = -4.12, df = 39, p < 0.001
- 95% CI for mean difference: [-3.3, -1.1] minutes
- Cohen's d = 0.65 (medium-large effect)

**Business interpretation:** The new onboarding flow reduces completion time by 2.2 minutes on average (p < 0.001, medium-large effect). The CI tells us the true improvement is between 1.1 and 3.3 minutes. This justifies rolling out the new flow.

---

## 🔑 Key Takeaway

> When the same subjects are measured twice, use a paired t-test. It's more powerful because it removes individual differences and focuses on the change. Before/after questions demand paired analysis.

---

## See It Applied

→ [Is this campaign actually working?](../../applied/notebooks/07-is-campaign-working.ipynb) — Measuring campaign lift

---

[← Day 62: Independent t-Test](day-62-independent-t-test.md) · [Next: Day 64 – One-Way ANOVA →](day-64-one-way-anova.md)
