# Day 111: What Makes a Good KPI?

*A vanity metric makes you feel good. A KPI makes you make decisions.*

---

## Learning Objective

Distinguish between vanity metrics and Key Performance Indicators (KPIs), understand the difference between leading and lagging indicators, and design actionable metrics using the SMART framework.

---

## The Problem This Solves

A startup team tracks "Registered Users." The number goes up every day. They celebrate. 

But behind the scenes, 80% of those registered users log in once and never return. The startup runs out of cash. "Registered Users" was a vanity metric. If they had tracked "Weekly Active Users" (a KPI), they would have recognized their retention crisis months earlier and adjusted their strategy.

---

## The Concept

### Vanity vs. Actionable Metrics (KPIs)

| Metric Type | Definition | Example | Business Risk |
|-------------|------------|---------|---------------|
| **Vanity Metric** | A metric that always increases or looks good on paper, but does not correlate with business success. | Total Page Views, App Downloads, Registered Users | Gives false confidence; hides product failures |
| **Actionable Metric (KPI)** | A metric that directly connects to business decisions and reveals user value. | Conversion Rate, 30-day Retention, Customer Acquisition Cost (CAC) | Drives product changes and financial resource allocation |

### Leading vs. Lagging Indicators

To steer a business, you need two types of metrics:

```
  Leading Indicator (Input / Predictive)    →    Lagging Indicator (Output / Outcome)
  "Are we doing the work today?"                 "Did we hit our business goals?"
  Example: Number of sales calls placed          Example: Quarterly revenue closed
  Easy to influence; hard to measure value       Hard to influence directly; easy to measure
```

### Designing SMART KPIs

A good KPI must be:
- **S**pecific: Target a clear area of the product or business (e.g., checkout conversion).
- **M**easurable: Quantifiable using data columns.
- **A**ctionable: If the metric drops, it triggers a clear business response.
- **R**elevant: Aligned with the company's high-level goals.
- **T**ime-bound: Measured over a fixed period (daily, weekly, monthly).

---

## Why Should a Data Analyst Care?

Because analysts are the designers of dashboards. If you build dashboards loaded with vanity metrics, stakeholders will stop looking at them. If you design dashboards built around SMART, actionable KPIs that pair leading and lagging indicators, those dashboards will drive every weekly executive meeting.

---

## Common Beginner Mistake

Creating complex, composite metrics that nobody understands. "User Engagement Score = 0.4*Clicks + 0.3*Scrolls + 0.3*Shares." 

If this score drops from 72 to 65, the product manager has no idea what to fix. Keep KPIs simple, raw, and directly tied to a specific user action.

---

## Real-World Example

A SaaS company reviews its dashboard metrics:

- **Metric A:** "Total registered accounts." (Vanity. It only goes up. It doesn't tell us if users are active).
- **Metric B:** "Monthly Recurring Revenue (MRR)." (Lagging KPI. Excellent for finance, but too slow to guide daily product changes).
- **Metric C:** "Percentage of new users who create a project within 48 hours." (Leading KPI. Highly actionable. If this drops, the onboarding flow is broken. Improving this metric today predicts higher MRR next quarter).

**Action:** Structure the dashboard to showcase Metric C as the main product driver, with Metric B as the lagging financial confirmation.

---

## 🔑 Key Takeaway

> Vanity metrics look good in press releases. KPIs drive decisions. Always pair leading indicators (daily inputs) with lagging indicators (financial outcomes) to build dashboards that steering committees can act on.

---

[← Module 14 README](README.md) · [Next: Day 112 – North Star Metrics →](day-112-north-star-metrics.md)
