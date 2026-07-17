# Day 66: Post-Hoc Tests

*ANOVA says "there's a difference." Post-hoc tests say "here's where."*

---

## Learning Objective

Understand why post-hoc tests are necessary after a significant ANOVA result, learn the most common methods (Tukey HSD, Bonferroni), and know how to interpret pairwise comparisons.

---

## The Problem This Solves

Your one-way ANOVA comparing 4 stores returned F = 8.42, p < 0.001. Great — there's a significant difference somewhere. But *which* stores differ from which? ANOVA doesn't tell you. You need post-hoc (Latin for "after this") tests to identify the specific pairwise differences.

---

## The Concept

### Why Not Just Run t-Tests?

With 4 groups, you'd need 6 pairwise t-tests. Each has a 5% false positive rate. Together:

```
P(at least one false positive) = 1 - (0.95)^6 = 0.265 → 26.5%
```

Post-hoc tests adjust for this **multiple comparisons problem**, keeping the overall error rate at 5%.

### Common Post-Hoc Methods

| Method | How It Adjusts | Best For |
|--------|---------------|----------|
| **Tukey HSD** | Compares all pairs simultaneously | Equal or near-equal group sizes |
| **Bonferroni** | Divides α by number of comparisons | Few planned comparisons |
| **Scheffé** | Most conservative adjustment | Complex contrasts |
| **Games-Howell** | Doesn't assume equal variances | Unequal group sizes or variances |

### Tukey HSD (Most Common)

Tukey's Honestly Significant Difference tests every pairwise comparison while controlling the family-wise error rate.

For each pair of groups:
```
HSD = (X̄ᵢ - X̄ⱼ) / √(MSW / n)

Compare against critical value from the Studentized Range distribution.
```

Output: a table of all pairwise comparisons with adjusted p-values.

### Bonferroni Correction (Simplest)

```
Adjusted α = α / number of comparisons

With 4 groups (6 comparisons):
  Original α = 0.05
  Bonferroni α = 0.05 / 6 = 0.0083

Any pairwise p-value must be below 0.0083 to be significant.
```

---

## Why Should a Data Analyst Care?

Because the business question is never "is there a difference somewhere?" — it's "which store should we investigate?" or "which channel should we invest in?" Post-hoc tests translate a statistical finding into an actionable answer. Without them, ANOVA results are incomplete.

---

## When to Use It

- **After a significant ANOVA** — never before (no need to investigate pairwise if the overall test is non-significant)
- **When you have 3+ groups** — with only 2 groups, the t-test already identifies the difference
- **For exploratory comparisons** — use Tukey HSD (tests all pairs). For pre-planned comparisons — use Bonferroni

---

## Common Beginner Mistake

Running post-hoc tests after a non-significant ANOVA. If the overall F-test says p = 0.35, there is no evidence of differences — don't go fishing for them with pairwise tests. Another mistake: using Bonferroni when you have many groups. With 10 groups (45 pairs), the adjusted α = 0.001 becomes so strict that real differences are missed. Use Tukey for many groups.

---

## Real-World Example

Following up on the satisfaction survey from Day 64 (4 channels):

**Tukey HSD Results:**

| Comparison | Mean Diff | Adjusted p | Significant? |
|-----------|-----------|-----------|-------------|
| Chat vs Phone | +4.3 | 0.012 | ✅ Yes |
| Chat vs Email | +6.7 | < 0.001 | ✅ Yes |
| In-App vs Phone | +4.9 | 0.004 | ✅ Yes |
| In-App vs Email | +7.3 | < 0.001 | ✅ Yes |
| Chat vs In-App | -0.6 | 0.982 | ❌ No |
| Phone vs Email | +2.4 | 0.287 | ❌ No |

**Business interpretation:** Chat and In-App are significantly better than Phone and Email, but not different from each other. Phone and Email are not different from each other. The recommendation: invest in Chat and In-App support; investigate why Email and Phone lag behind.

---

## 🔑 Key Takeaway

> ANOVA tells you a difference exists. Post-hoc tests tell you where it is. Without both, you have a finding without direction. Always pair a significant ANOVA with the right post-hoc comparison.

---

## See It Applied

→ [Is this campaign actually working?](../../applied/notebooks/07-is-campaign-working.ipynb) — Multiple comparison corrections with Bonferroni

---

[← Day 65: Two-Way ANOVA](day-65-two-way-anova.md) · [Next: Day 67 – Chi-Square Test of Independence →](day-67-chi-square-independence.md)
