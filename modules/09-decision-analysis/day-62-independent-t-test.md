# Day 62: Independent t-Test (Revisited)

*You learned the t-test on Day 23. Now use it to make real business decisions.*

---

## Learning Objective

Deepen your understanding of the independent samples t-test by applying it to a business comparison, interpreting results beyond the p-value, and knowing when to use Welch's correction.

---

## The Problem This Solves

Two customer groups — online vs offline — have different average order values. You need to determine whether that difference is statistically significant before recommending a strategy change. The independent t-test compares the means of two unrelated groups.

---

## The Concept

### When to Use It

- You have **two independent groups** (they don't overlap)
- Your outcome variable is **continuous** (revenue, time, score)
- You want to know if the group means are **significantly different**

### The Hypotheses

- **H₀:** μ₁ = μ₂ (no difference between group means)
- **H₁:** μ₁ ≠ μ₂ (group means are different)

### The Formula

```
t = (X̄₁ - X̄₂) / √(s₁²/n₁ + s₂²/n₂)

Where:
  X̄₁, X̄₂  = sample means
  s₁², s₂² = sample variances
  n₁, n₂   = sample sizes
```

### Student's t vs Welch's t

| Aspect | Student's t-test | Welch's t-test |
|--------|-----------------|----------------|
| **Assumes equal variances?** | Yes | No |
| **Degrees of freedom** | n₁ + n₂ - 2 | Adjusted (Welch-Satterthwaite) |
| **When to use** | Variances are similar | Default — always safe |
| **Recommendation** | Use only when Levene's test confirms equal variance | **Use this by default** |

### Beyond the p-Value

Always report three things:

1. **p-value** — Is the difference statistically significant?
2. **Confidence interval** — What is the plausible range of the true difference?
3. **Cohen's d** — How large is the effect?

```
Cohen's d = (X̄₁ - X̄₂) / s_pooled

Small:  d = 0.2
Medium: d = 0.5
Large:  d = 0.8
```

---

## Why Should a Data Analyst Care?

Because the t-test is the workhorse of A/B testing. Every time a product team asks "did this feature improve engagement?" or a marketing team asks "did this campaign increase spend?", the answer starts with a two-sample comparison. Knowing when to use it — and when it fails — separates confident analysis from guesswork.

---

## When to Use It

- **A/B tests** — comparing treatment vs control
- **Segment comparisons** — online vs offline, male vs female, new vs returning
- **Pre/post with different subjects** — last year's customers vs this year's

---

## Common Beginner Mistake

Using Student's t-test without checking equal variance assumption. If group variances are very different (one group is 3× more variable), Student's t-test gives misleading p-values. Welch's t-test handles this automatically — use it by default.

---

## Real-World Example

An e-commerce company compares average order value between online and offline customers:

| Group | n | Mean | Std Dev |
|-------|---|------|---------|
| Online | 250 | $68.40 | $22.10 |
| Offline | 180 | $74.20 | $28.50 |

**Welch's t-test results:**
- t = -2.34, df = 332, p = 0.020
- 95% CI for difference: [-$10.68, -$0.92]
- Cohen's d = 0.23 (small effect)

**Business interpretation:** The difference is statistically significant (p = 0.020), but the effect size is small (d = 0.23). Offline customers spend about $5.80 more on average. This difference is real but may not justify major strategic changes — the CI suggests the true difference is between $1 and $11.

---

## 🔑 Key Takeaway

> The independent t-test answers: "Are these two groups really different?" But the p-value alone is not enough — always pair it with a confidence interval and effect size to determine whether the difference is large enough to act on.

---

## See It Applied

→ [Restaurant Tipping Behavior](../../applied/case-studies/restaurant-tipping-behavior/) — Welch's t-test comparing lunch vs dinner tips
→ [Is this campaign actually working?](../../applied/notebooks/07-is-campaign-working.ipynb) — Two-group spend comparison

---

[← Day 61: Why Compare Groups?](day-61-why-compare-groups.md) · [Next: Day 63 – Paired t-Test →](day-63-paired-t-test.md)
