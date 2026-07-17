# Day 113: Cohort Analysis

*If you don't look at cohorts, you will confuse acquisition growth with user loyalty.*

---

## Learning Objective

Understand cohort analysis, build retention curves, and construct a cohort retention matrix to analyze customer health over time.

---

## The Problem This Solves

Your active user count is growing 20% month-over-month. You declare a massive success. 

What you missed: the growth is driven entirely by cheap paid ads bringing in new users who churn within 7 days. Your core product is a leaky bucket. If the ad budget stops, active users will collapse. Cohort analysis exposes this by tracking user groups over time, independent of acquisition spikes.

---

## The Concept

### What is a Cohort?

A cohort is a group of users who share a common characteristic and start date.

- **Acquisition Cohort:** Users who signed up in the same month (e.g., the "Jan 2026 Cohort").
- **Behavioral Cohort:** Users who performed a specific action (e.g., the "Used Search Bar Cohort").

### The Cohort Retention Matrix

We track the percentage of each cohort that returns in subsequent periods:

```
Cohort | Size  | Month 0 | Month 1 | Month 2 | Month 3 | Month 4 | Month 5
───────┼───────┼─────────┼─────────┼─────────┼─────────┼─────────┼────────
Jan 26 | 1,000 | 100%    | 40%     | 30%     | 25%     | 24%     | 24%  ← Retains (curve flattens)
Feb 26 | 1,200 | 100%    | 35%     | 22%     | 18%     | 15%     | 12%  ← Churns (leaky bucket)
Mar 26 | 1,500 | 100%    | 45%     | 38%     | 35%     | 34%     | 34%  ← Product improvement!
```

- **Reading horizontally (Rows):** Shows how a single cohort behaves over time (retention curve).
- **Reading vertically (Columns):** Shows how different cohorts compare at the same age (e.g., comparing Month 1 retention across cohorts).
- **Reading diagonally:** Shows performance during the same calendar month.

### Retention Curves: Flattening vs. Decaying

```
Retention (%)
 100 █
  80 █
  60 █▄
  40 █▀▄     ◄─── Flattening Curve (Sustainable product - holds users)
  20 █  ▀▄▄
   0 █     ▀▀▄▄▄▄ ◄─── Decaying Curve (Leaky bucket - users eventually all leave)
     └───────────────────►
      0  1  2  3  4 (Months)
```

For a business to survive, the retention curve **must flatten**. If it decays to 0%, the business will eventually fail once acquisition channels dry up.

---

## Why Should a Data Analyst Care?

Because cohort analysis is the default methodology for evaluating **product-market fit**. Venture capitalists and executives use cohort tables to value businesses. If you can build and interpret a cohort matrix, you can immediately identify whether a business's growth is healthy and sustainable.

---

## Common Beginner Mistake

Averaging retention rates across all users. If you calculate "overall 30-day retention is 30%," you miss the fact that older cohorts are at 10% while newer cohorts (who experienced the updated app) are at 60%. Aggregation hides the very trends you need to find. Always slice retention by cohort.

---

## Real-World Example

A mobile app analyst builds a retention matrix after launching a new user interface in March:

- **January Cohort:** Month 1 Retention = **30%**
- **February Cohort:** Month 1 Retention = **32%**
- **March Cohort (New UI):** Month 1 Retention = **48%**

**Business Insight:** The new UI launched in March drove a 16% absolute lift in Month 1 retention compared to January. This is clear evidence of product improvement. The analyst presents this row-by-row comparison to the product VP to justify rolling out the UI to all users.

---

## 🔑 Key Takeaway

> Cohort analysis tracks user groups over time to isolate retention from acquisition. A flattening retention curve indicates product-market fit; a decaying curve indicates a leaky bucket.

---

[← Day 112: North Star Metrics](day-112-north-star-metrics.md) · [Next: Day 114 – Funnel Analysis →](day-114-funnel-analysis.md)
