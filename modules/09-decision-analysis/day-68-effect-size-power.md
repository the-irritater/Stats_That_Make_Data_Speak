# Day 68: Effect Size & Statistical Power

*A significant result tells you a difference exists. Effect size tells you if it matters. Power tells you if you could have found it.*

---

## Learning Objective

Understand effect size and statistical power as essential complements to p-values, learn how to calculate sample size requirements, and know why underpowered studies waste resources.

---

## The Problem This Solves

Two scenarios that look identical on the surface:

1. **Study A:** p = 0.04, n = 10,000, Cohen's d = 0.04 → statistically significant but trivially small
2. **Study B:** p = 0.08, n = 30, Cohen's d = 0.65 → not significant but potentially large and important

Without effect size, you'd trust Study A and dismiss Study B. With it, you'd realize Study A found a meaningless difference and Study B probably missed a real one due to insufficient sample size.

---

## The Concept

### Effect Size (Recap + Expansion)

**How large is the difference?** — independent of sample size.

| Measure | Used With | Small | Medium | Large |
|---------|----------|-------|--------|-------|
| **Cohen's d** | t-tests (mean differences) | 0.2 | 0.5 | 0.8 |
| **η² (Eta-squared)** | ANOVA (variance explained) | 0.01 | 0.06 | 0.14 |
| **Cramér's V** | Chi-Square (categorical association) | 0.1 | 0.3 | 0.5 |
| **r (Pearson)** | Correlation | 0.1 | 0.3 | 0.5 |
| **Cohen's h** | Proportion differences | 0.2 | 0.5 | 0.8 |

### Statistical Power

**The probability that your test will detect a real effect if one exists.**

```
Power = P(Reject H₀ | H₁ is true) = 1 - β

Where β = P(Type II Error) = probability of missing a real effect
```

- **Standard target: Power ≥ 0.80** (80% chance of detecting a real effect)
- Power < 0.80 → the study is underpowered → likely to miss real effects

### The Four Connected Elements

These four are mathematically linked — fix any three, and the fourth is determined:

| Element | What It Is | Effect on Power |
|---------|-----------|----------------|
| **Sample size (n)** | Number of observations | ↑ n → ↑ Power |
| **Effect size (d)** | Magnitude of the real difference | ↑ d → ↑ Power |
| **Significance level (α)** | Threshold for p-value (usually 0.05) | ↑ α → ↑ Power |
| **Power (1 - β)** | Probability of detecting the effect | — |

### Sample Size Calculation

Before running a study, calculate the minimum sample size needed:

```
Given: desired Power = 0.80, α = 0.05, expected d = 0.5

For independent t-test: n ≈ 64 per group
For ANOVA (4 groups):   n ≈ 45 per group
```

---

## Why Should a Data Analyst Care?

Because underpowered analyses are the most common waste of resources in business analytics. If you run an A/B test with too few users, you'll likely get p > 0.05 even if the treatment works. You'll conclude "no effect" when the real conclusion should be "we didn't have enough data to tell." Power analysis *before* the experiment prevents this.

---

## When to Use It

- **Before any experiment** — calculate required sample size
- **When interpreting non-significant results** — was the study powered to detect the expected effect?
- **When a significant result seems trivially small** — check effect size before acting
- **Budget planning** — how many users/days does this experiment need?

---

## Common Beginner Mistake

Running an A/B test for "one week" without power analysis. If the expected lift is 2% and you need 10,000 users per group to detect it at 80% power, stopping at 500 users means you had only ~12% power. The test was doomed before it started. Another mistake: celebrating a "significant" result without checking effect size — it might be too small to matter.

---

## Real-World Example

A product team wants to test a new checkout flow. Expected improvement: 3% conversion lift (from 10% to 13%).

**Power analysis:**
- Effect size (Cohen's h): 0.09 (small)
- Desired power: 0.80
- α: 0.05
- **Required sample: ~1,950 per group**

The team currently gets 200 visitors/day. They need to run the test for at least **20 days** (3,900 total visitors / 200 per day). Running for 5 days would give only ~35% power — barely better than a coin flip for detecting the effect.

---

## 🔑 Key Takeaway

> Effect size answers: "How big is the difference?" Power answers: "Could we have found it?" Together with the p-value, they form the three pillars of honest statistical analysis. Report all three, or you're telling an incomplete story.

---

## See It Applied

→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Cramér's V effect size reporting
→ [Is this campaign actually working?](../../applied/notebooks/07-is-campaign-working.ipynb) — Cohen's d and dual-endpoint power

---

[← Day 67: Chi-Square Test of Independence](day-67-chi-square-independence.md) · [Next: Day 69 – Business Case Study →](day-69-business-case-study.md)
