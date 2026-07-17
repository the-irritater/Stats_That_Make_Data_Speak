# Day 147: MANOVA

*ANOVA compares one outcome across groups. MANOVA compares a vector of multiple outcomes across groups, controlling for their correlation.*

---

## Learning Objective

Understand Multivariate Analysis of Variance (MANOVA), identify when it is superior to multiple ANOVAs, and interpret Wilks' Lambda and Pillai's Trace.

---

## The Problem This Solves

You want to compare customer behavior across three subscription plans (Basic, Pro, Premium). You track:
1. `monthly_spend` ($)
2. `support_tickets` (count)
3. `logins_per_month` (count)

If you run three separate ANOVAs, your overall Type I error rate (false positive rate) is inflated. Furthermore, you miss the fact that spend and logins are correlated. MANOVA tests whether the *combination* of all three outcome variables differs across plans in a single step.

---

## The Concept

### What is MANOVA?

MANOVA stands for **Multivariate Analysis of Variance**. It is the extension of ANOVA for situations with one or more categorical predictors and **two or more continuous outcome variables**.

- **ANOVA Null Hypothesis:** Group means are equal: `μ₁ = μ₂ = μ₃`.
- **MANOVA Null Hypothesis:** Group mean **vectors** are equal: `[μ_11, μ_12] = [μ_21, μ_22] = ...`

```
ANOVA:   Compare group means on a 1D line:
         Group A: ──●──  Group B: ──●──

MANOVA:  Compare group centroids in a 2D/3D space:
         Group A Centroid: (X̄_A, Ȳ_A)  vs.  Group B Centroid: (X̄_B, Ȳ_B)
```

### The Multivariate Test Statistics

Unlike ANOVA's F-test, MANOVA decomposes the Total Sum of Squares and Cross-Products matrix (SSCP) into Hypothesis (H) and Error (E) matrices. We evaluate this using four common statistics:

| Statistic | What It Measures | When to Use |
|-----------|-----------------|-------------|
| **Pillai's Trace** | Proportion of variance explained by the model. | Most robust to violations of assumptions (standard choice). |
| **Wilks' Lambda (λ)** | Proportion of variance *unexplained* (lower is better). | Classic, widely reported metric. |
| **Hotelling's Trace** | Variance ratio of H to E. | Used when comparing exactly two groups. |
| **Roy's Largest Root** | Upper bound of variance explained on the first dimension. | Most powerful if differences are highly concentrated on one dimension. |

### Follow-up Pipeline

If the MANOVA test is **significant** (e.g. Pillai's Trace p < 0.05):
1. You have permission to investigate further.
2. Run follow-up univariate ANOVAs on each outcome.
3. Apply Bonferroni adjustments to those ANOVAs to control error rates.

---

## Why Should a Data Analyst Care?

Because running multiple t-tests or ANOVAs on highly correlated metrics is a mark of statistical immaturity. If you evaluate a multi-variant product change on three correlated outcomes (e.g., clicks, scrolls, views), MANOVA is the correct, rigorous gatekeeper test to run before claiming any individual metric succeeded.

---

## Common Beginner Mistake

Running MANOVA when outcomes are completely uncorrelated. If your dependent variables are unrelated, MANOVA loses statistical power compared to running separate ANOVAs. Only use MANOVA when your outcome variables have moderate correlation (correlation between 0.3 and 0.8).

---

## Real-World Example

A SaaS company compares user engagement across three customer segments (Small, Mid-Market, Enterprise):
- **Outcomes (Dependent variables):** Monthly usage hours, active user seats.

**MANOVA Results:**
- Pillai's Trace = 0.18, F(4, 988) = 24.3, **p < 0.001**.
- **Interpretation:** The combination of usage hours and user seats differs significantly across segments.

**Follow-up ANOVAs (with Bonferroni adjustment, α = 0.025):**
- Usage hours: F(2, 494) = 18.2, **p < 0.001** (Significant ✅)
- User seats: F(2, 494) = 2.1, **p = 0.120** (Not significant ❌)

**Business Decision:** The segments differ significantly in monthly usage hours, but do not differ in the number of user seats they activate. Focus account management efforts on driving active usage hours rather than seat expansion in Mid-Market.

---

## 🔑 Key Takeaway

> MANOVA compares group centroids across multiple correlated outcome variables in a single test, protecting against false positive inflation. If the multivariate test is significant, run adjusted follow-up ANOVAs to identify specific outcomes.

---

[← Day 146: Exploratory vs. Confirmatory Factor Analysis](day-146-efa-vs-cfa.md) · [Next: Day 148 – Canonical Correlation Analysis (CCA) →](day-148-canonical-correlation.md)
