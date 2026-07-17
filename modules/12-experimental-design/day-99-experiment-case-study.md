# Day 99: Business Experiment Case Study

*One pricing strategy. Three variations. 50,000 customers. This is how you run and report a multi-variant business test.*

---

## Learning Objective

Integrate experimental design concepts — metrics, sample size, multiple testing adjustments, and decision-making — into a single, end-to-end business case study.

---

## The Problem

An online education platform offers a monthly subscription. The marketing team wants to test whether adding a "Premium support" addon option at checkout increases average revenue per user (ARPU) without hurting subscription conversion rates.

They design a three-arm experiment:
- **Control (A):** Standard checkout flow (no addon).
- **Variant 1 (B):** Addon offered as an opt-in checkbox (+$10/month).
- **Variant 2 (C):** Addon pre-checked by default (+$10/month, opt-out).

---

## The Design Phase

### 1. Metric Scorecard
- **Primary Metric:** Average Revenue Per User (ARPU) — continuous.
- **Guardrail Metric 1:** Subscription Conversion Rate (must not drop by >0.5% absolute).
- **Guardrail Metric 2:** 30-day Refund Request Rate (must not increase by >1.0% absolute).

### 2. Sample Size Planning
- **Baseline ARPU:** $20.00 (Standard deviation: $15.00)
- **Target MDE:** $0.50 (We want to detect a 2.5% revenue change)
- **Power:** 80% (β = 0.20)
- **Significance Level (α):** 0.05

Using a three-group sample size calculator, they need **~15,500 users per group** (46,500 total). The test runs for 16 days to hit the target traffic.

---

## The Execution & Data

After 16 days, the dataset contains:

| Group | Users (n) | Conversion Rate | ARPU (Mean ± SD) | Refund Rate |
|-------|-----------|-----------------|------------------|-------------|
| **Control (A)** | 15,620 | 12.4% | $20.12 ± $14.80 | 1.1% |
| **Opt-in (B)** | 15,580 | 12.3% | $20.85 ± $15.60 | 1.3% |
| **Opt-out (C)** | 15,650 | 11.6% | $21.90 ± $17.20 | 4.8% |

---

## The Analysis

Because we have two treatment groups compared to one control, we face a multiple testing problem (2 comparisons). 

### 1. Primary Metric: ARPU (One-Way ANOVA + Tukey HSD)
An ANOVA test on ARPU shows a significant difference somewhere: `F(2, 46847) = 54.2, p < 0.001`.

Tukey HSD Post-Hoc results:
- **Opt-in (B) vs Control (A):** Mean Diff: +$0.73, **Adjusted p = 0.003** (Significant ✅)
- **Opt-out (C) vs Control (A):** Mean Diff: +$1.78, **Adjusted p < 0.001** (Significant ✅)
- **Opt-out (C) vs Opt-in (B):** Mean Diff: +$1.05, **Adjusted p < 0.001** (Significant ✅)

### 2. Guardrail 1: Conversion Rate (Chi-Square with Bonferroni)
Since we run 2 pairwise comparisons, our Bonferroni adjusted α is `0.05 / 2 = 0.025`.

- **Opt-in (B) vs Control (A):** Difference: -0.1%, χ²(1) = 0.18, **p = 0.671** (Not significant — Guardrail stands ✅)
- **Opt-out (C) vs Control (A):** Difference: -0.8%, χ²(1) = 5.82, **p = 0.016** (Significant at adjusted α — **Guardrail violated!** ❌)

### 3. Guardrail 2: Refund Rate (Chi-Square with Bonferroni)
Adjusted α = 0.025.

- **Opt-in (B) vs Control (A):** Difference: +0.2%, p = 0.312 (Not significant — Guardrail stands ✅)
- **Opt-out (C) vs Control (A):** Difference: +3.7%, **p < 0.001** (Significant — **Guardrail violated!** ❌)

---

## Business Decision

- **Opt-out (C)** drove the highest ARPU (+$1.78). However, it violated both guardrail metrics: checkout conversion dropped by 0.8% (likely due to friction from pre-checking a paid addon), and refund requests surged to 4.8% (frustrated users realizing they were charged for an addon they didn't want).
- **Opt-in (B)** drove a significant ARPU increase (+$0.73) without any negative impact on subscription conversion or refunds.

**Recommendation:** Roll out **Variant 1 (Opt-in checkbox)**. Do not implement the pre-checked opt-out flow, as the short-term ARPU gain is wiped out by customer dissatisfaction, higher refund rates, and checkout dropoffs.

---

## 🔑 Key Takeaway

> Never evaluate business experiments on a single revenue metric. A treatment can maximize revenue while destroying conversion rates and brand trust. Always build guardrail metrics into your experiment scorecard.

---

[← Day 98: Multiple Testing Problem](day-98-multiple-testing.md) · [Next: Day 100 – Module Recap & Experimental Framework →](day-100-causal-recaps.md)
