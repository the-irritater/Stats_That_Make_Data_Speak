# Day 69: Business Case Study — Customer Satisfaction Analysis

*This is where everything comes together. One dataset. One business question. Every tool from this module.*

---

## Learning Objective

Apply the full statistical decision-making toolkit — t-tests, ANOVA, Chi-Square, effect sizes, and power — to a realistic customer satisfaction analysis from start to finish.

---

## The Problem

A telecom company wants to understand customer satisfaction across service plans and support channels to decide where to invest.

**Business questions:**
1. Is satisfaction different between Basic and Premium customers?
2. Does satisfaction vary across support channels (Phone, Chat, Email)?
3. Does the channel effect depend on the plan type?
4. Is plan type associated with churn status?

---

## The Analysis Pipeline

### Step 1: Understand the Data

| Variable | Type | Values |
|----------|------|--------|
| `satisfaction_score` | Continuous (1–100) | Outcome variable |
| `plan_type` | Categorical | Basic, Premium |
| `support_channel` | Categorical | Phone, Chat, Email |
| `churned` | Binary | Yes, No |
| `n` | — | 600 customers |

### Step 2: Compare Two Groups — Independent t-Test

**Question:** Is satisfaction different between Basic and Premium?

| Plan | n | Mean | Std Dev |
|------|---|------|---------|
| Basic | 320 | 64.2 | 15.8 |
| Premium | 280 | 72.8 | 13.4 |

**Welch's t-test:** t(578) = -7.12, p < 0.001
**Cohen's d:** 0.59 (medium effect)
**95% CI for difference:** [-10.98, -6.22]

**Finding:** Premium customers are significantly more satisfied (medium effect). The true difference is between 6 and 11 points.

### Step 3: Compare Multiple Groups — One-Way ANOVA

**Question:** Does satisfaction vary by support channel?

| Channel | n | Mean | Std Dev |
|---------|---|------|---------|
| Phone | 210 | 65.4 | 16.1 |
| Chat | 195 | 72.1 | 13.2 |
| Email | 195 | 66.8 | 15.5 |

**ANOVA:** F(2, 597) = 11.23, p < 0.001, η² = 0.036

**Tukey HSD Post-Hoc:**

| Comparison | Diff | Adjusted p | Significant? |
|-----------|------|-----------|-------------|
| Chat vs Phone | +6.7 | < 0.001 | ✅ |
| Chat vs Email | +5.3 | 0.002 | ✅ |
| Email vs Phone | +1.4 | 0.574 | ❌ |

**Finding:** Chat outperforms Phone and Email. Phone and Email are similar.

### Step 4: Test for Interaction — Two-Way ANOVA

**Question:** Does the channel effect depend on plan type?

| Source | F | p | η² |
|--------|---|---|---|
| Plan Type | 45.2 | < 0.001 | 0.07 |
| Channel | 10.8 | < 0.001 | 0.04 |
| Plan × Channel | 5.3 | 0.005 | 0.02 |

**Finding:** Significant interaction (p = 0.005). Chat boosts satisfaction more for Basic customers (+9.2 points) than Premium (+3.8 points). Premium customers are already satisfied across channels.

### Step 5: Categorical Association — Chi-Square

**Question:** Is plan type associated with churn?

| | Churned | Retained | Total |
|--|---------|----------|-------|
| Basic | 82 | 238 | 320 |
| Premium | 34 | 246 | 280 |

**Chi-Square:** χ²(1) = 18.7, p < 0.001
**Cramér's V:** 0.177 (small-medium)
**Risk Ratio:** Basic churn rate (25.6%) / Premium churn rate (12.1%) = 2.11

**Finding:** Basic customers churn at more than double the rate of Premium customers.

### Step 6: Power Check

Was this study adequately powered?

| Test | Observed Effect | Power at n = 600 |
|------|----------------|------------------|
| t-test (d = 0.59) | Medium | > 0.99 ✅ |
| ANOVA (η² = 0.036) | Small-medium | 0.95 ✅ |
| Chi-Square (V = 0.177) | Small-medium | 0.98 ✅ |

All tests were well-powered — the sample size was sufficient to detect the observed effects.

---

## Business Recommendations

1. **Invest in Chat support for Basic customers** — it has the largest satisfaction impact where it's needed most (interaction effect)
2. **Investigate Basic plan churn drivers** — 25.6% churn rate vs 12.1% for Premium suggests a retention problem beyond satisfaction
3. **Don't over-invest in channel improvements for Premium** — they're already satisfied regardless of channel
4. **Consider upgrading paths** — if Premium satisfaction drives retention, create incentives for Basic → Premium migration

---

## 🔑 Key Takeaway

> Real analysis is never one test. It's a sequence: understand the data → compare groups → check interactions → test categorical relationships → verify power. Each tool answers a different question. Together, they tell the complete story.

---

## See It Applied

→ [Signature Project: Customer Analytics](../../applied/signature-project/) — Full analytics pipeline with OLS, RFM, and Chi-Square
→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Business decision from statistical evidence

---

[← Day 68: Effect Size & Statistical Power](day-68-effect-size-power.md) · [Next: Day 70 – Module Recap + Decision Framework →](day-70-decision-framework-recap.md)
