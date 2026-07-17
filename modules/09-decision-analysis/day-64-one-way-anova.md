# Day 64: One-Way ANOVA

*The t-test compares two groups. ANOVA compares three, four, or forty — without inflating your error rate.*

---

## Learning Objective

Understand one-way ANOVA as the extension of the t-test for comparing means across multiple groups, interpret the F-statistic, and know why running multiple t-tests is wrong.

---

## The Problem This Solves

You manage 4 retail stores and want to know if average daily sales differ across them. You could run 6 separate t-tests (A vs B, A vs C, A vs D, B vs C, B vs D, C vs D). But each test has a 5% chance of a false positive. Six tests → ~26% chance of at least one false positive. That's unacceptable.

ANOVA tests all groups simultaneously with a single test, keeping the error rate at 5%.

---

## The Concept

### What ANOVA Tests

- **H₀:** μ₁ = μ₂ = μ₃ = ... = μₖ (all group means are equal)
- **H₁:** At least one group mean is different

### How It Works

ANOVA compares two sources of variation:

| Source | What It Measures |
|--------|-----------------|
| **Between-group variance** | How much group means differ from the overall mean |
| **Within-group variance** | How much individual values vary within each group |

### The F-Statistic

```
F = Between-group variance / Within-group variance
  = MSB / MSW

Where:
  MSB = Sum of Squares Between / (k - 1)
  MSW = Sum of Squares Within / (N - k)
  k   = number of groups
  N   = total sample size
```

- **F ≈ 1:** Groups are similar (between-group variation ≈ within-group variation)
- **F >> 1:** Groups are different (between-group variation >> within-group variation)

### Assumptions

| Assumption | What It Means | How to Check |
|-----------|--------------|-------------|
| **Independence** | Observations are unrelated | Study design |
| **Normality** | Each group's data is roughly normal | Shapiro-Wilk test, Q-Q plots |
| **Homogeneity of variance** | Groups have similar spread | Levene's test |

### Effect Size: Eta-Squared (η²)

```
η² = SS_between / SS_total

Small:  η² = 0.01
Medium: η² = 0.06
Large:  η² = 0.14
```

---

## Why Should a Data Analyst Care?

Because multi-group comparisons are everywhere: comparing marketing channels, product lines, regions, customer segments, or time periods. ANOVA is the standard tool for this — and knowing when to use it (and when ANOVA alone is not enough) separates rigorous analysis from cherry-picked comparisons.

---

## When to Use It

- **3+ independent groups** with a continuous outcome
- **Testing overall difference** before diving into pairwise comparisons
- **Any time you'd be tempted to run multiple t-tests**

---

## Common Beginner Mistake

Running ANOVA and stopping at "p < 0.05." ANOVA only tells you that *at least one* group is different — it doesn't tell you *which one*. You need post-hoc tests (Day 66) to identify the specific differences. Also: reporting only the p-value without η² leaves stakeholders unable to judge the practical importance.

---

## Real-World Example

A company compares customer satisfaction scores (1–100) across 4 support channels:

| Channel | n | Mean Score | Std Dev |
|---------|---|-----------|---------|
| Phone | 120 | 74.2 | 12.1 |
| Chat | 135 | 78.5 | 11.8 |
| Email | 110 | 71.8 | 14.3 |
| In-App | 95 | 79.1 | 10.9 |

**ANOVA results:**
- F(3, 456) = 8.42, p < 0.001
- η² = 0.052 (small-medium effect)

**Business interpretation:** There is a statistically significant difference in satisfaction across channels (p < 0.001). However, the effect size is small-medium (η² = 0.052), meaning channel explains about 5% of satisfaction variance. Next step: run post-hoc tests to identify which channels differ from each other.

---

## 🔑 Key Takeaway

> ANOVA answers: "Is there a difference somewhere among these groups?" — not "where is the difference." It's the gateway test. A significant result means you have permission to look deeper with post-hoc comparisons.

---

## See It Applied

→ [Restaurant Tipping Behavior](../../applied/case-studies/restaurant-tipping-behavior/) — Comparing across meal categories
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — Segment performance comparisons

---

[← Day 63: Paired t-Test](day-63-paired-t-test.md) · [Next: Day 65 – Two-Way ANOVA →](day-65-two-way-anova.md)
