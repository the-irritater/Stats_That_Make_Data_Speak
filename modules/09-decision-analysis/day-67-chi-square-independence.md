# Day 67: Chi-Square Test of Independence

*When your outcome is a category — not a number — you need a different test entirely.*

---

## Learning Objective

Apply the Chi-Square test of independence to determine whether two categorical variables are associated, interpret contingency tables, and report results with effect sizes.

---

## The Problem This Solves

Your marketing team segments customers by gender and tracks which product category they buy most. Does product preference depend on gender? You can't use a t-test or ANOVA — both variables are categorical. The Chi-Square test of independence determines whether two categorical variables are related.

---

## The Concept

### When to Use It

- **Both variables are categorical** (e.g., gender × product choice, region × churn status)
- You want to know if they are **associated** or **independent**

### The Hypotheses

- **H₀:** The two variables are independent (no association)
- **H₁:** The two variables are not independent (there is an association)

### How It Works

1. Build a **contingency table** of observed frequencies
2. Calculate **expected frequencies** under independence
3. Compare observed vs expected using the Chi-Square statistic

### The Formula

```
χ² = Σ (Oᵢ - Eᵢ)² / Eᵢ

Expected frequency: E = (Row Total × Column Total) / Grand Total
```

### Effect Size: Cramér's V

The p-value tells you IF there's an association. Cramér's V tells you HOW STRONG:

```
Cramér's V = √(χ² / (n × (min(r, c) - 1)))

Small:  V = 0.1
Medium: V = 0.3
Large:  V = 0.5
```

### Assumptions

| Assumption | Requirement |
|-----------|------------|
| **Independent observations** | Each subject counted once |
| **Expected frequencies ≥ 5** | In at least 80% of cells |
| **Adequate sample size** | Small samples → use Fisher's exact test |

---

## Why Should a Data Analyst Care?

Because many business outcomes are categorical: bought vs didn't buy, churned vs retained, clicked vs ignored, chose product A vs B vs C. When both the predictor and outcome are categories, Chi-Square is the standard tool. It powers every categorical A/B test analysis.

---

## When to Use It

- **A/B test with categorical outcome** — conversion (yes/no) by group (A/B)
- **Market research** — product preference by demographic
- **Churn analysis** — churn status by customer segment
- **Quality control** — defect type by production line

---

## Common Beginner Mistake

Interpreting a significant Chi-Square as a large effect. With large samples, even tiny associations become significant. Always report Cramér's V alongside the p-value. A V = 0.04 with p < 0.001 means the association exists but is practically meaningless.

---

## Real-World Example

A retailer tests whether product category preference differs by gender:

**Observed Frequencies:**

| | Electronics | Clothing | Home | Total |
|--|------------|----------|------|-------|
| **Male** | 120 | 80 | 60 | 260 |
| **Female** | 70 | 140 | 90 | 300 |
| **Total** | 190 | 220 | 150 | 560 |

**Expected Frequencies (under independence):**

| | Electronics | Clothing | Home |
|--|------------|----------|------|
| **Male** | 88.2 | 102.1 | 69.6 |
| **Female** | 101.8 | 117.9 | 80.4 |

**Results:**
- χ²(2) = 28.3, p < 0.001
- Cramér's V = 0.225 (small-medium effect)

**Business interpretation:** Product preference is significantly associated with gender (p < 0.001). Males over-index on Electronics (120 observed vs 88 expected); Females over-index on Clothing (140 vs 118 expected). Effect is small-medium (V = 0.225). This justifies targeted email campaigns but should not drive major inventory decisions.

---

## 🔑 Key Takeaway

> The Chi-Square test answers: "Are these two categories related?" It's the t-test equivalent for categorical data. Always pair the p-value with Cramér's V to know whether the relationship is strong enough to act on.

---

## See It Applied

→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Chi-Square test for retention analysis
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — Chi-Square test of RFM segment vs retention

---

[← Day 66: Post-Hoc Tests](day-66-post-hoc-tests.md) · [Next: Day 68 – Effect Size & Statistical Power →](day-68-effect-size-power.md)
