# Day 115: Customer Segmentation

*If you treat all customers the same, you will waste marketing budget on deal-seekers and ignore your champions.*

---

## Learning Objective

Understand customer segmentation, implement the RFM (Recency, Frequency, Monetary) framework, and translate segments into targeted business campaigns.

---

## The Problem This Solves

You want to run a discount campaign to increase sales. If you email a 20% discount coupon to everyone, you will cannibalize margins on your best customers (who would have bought anyway) and spam customers who have already churned, leading to high unsubscribe rates. 

Segmentation groups customers by behavior so you can send the right offer to the right group.

---

## The Concept

### The RFM Framework

The most robust behavioral segmentation model for transactional businesses:

| Dimension | Definition | Business Question | Coded Score |
|-----------|------------|-------------------|-------------|
| **Recency (R)** | Days since last purchase | "How recently did they buy?" | `1` (cold) to `5` (hot) |
| **Frequency (F)** | Total number of purchases | "How often do they buy?" | `1` (one-off) to `5` (frequent) |
| **Monetary (M)** | Total value of purchases | "How much cash have they spent?"| `1` (low value) to `5` (high value) |

Each customer receives a composite RFM score (e.g., `555` = High Recency, High Frequency, High Monetary).

### Common Customer Segments

By grouping similar RFM scores, we define actionable business segments:

| Segment | RFM Score Profile | Description | Business Action |
|---------|-------------------|-------------|-----------------|
| **Champions** | `555`, `554`, `545` | Recent, frequent, and high spenders. | Don't discount. Reward with early access and VIP perks. |
| **Loyal Customers** | `454`, `444`, `344` | High frequency, buy regularly. | Cross-sell related products. |
| **At Risk / Churn Risk** | `224`, `215`, `125` | High value in the past, but haven't bought in a long time. | Send a personalized "we miss you" offer with a high discount. |
| **New Customers** | `511`, `512` | Bought very recently, but only once. | Send welcome guides and post-purchase onboarding emails. |

---

## Why Should a Data Analyst Care?

Because customer segmentation is the foundation of digital marketing. CMOs need to know: *"Who are our best buyers, and how do we reactivate lost ones?"* By running an RFM segmentation, you provide a clean list of customer groups that can be directly synced to CRM tools (HubSpot, Salesforce) for automated campaigns.

---

## Common Beginner Mistake

Creating too many segments. If you divide customers into 50 different micro-segments, the marketing team won't have the bandwidth to design 50 different campaigns. Keep your segments actionable — typically 3 to 6 major groups are enough to drive business value.

---

## Real-World Example

An analyst segments an e-commerce database of 10,000 customers:

- **Segment A (Champions - 15%):** R: 4.8, F: 4.5, M: $250.
- **Segment B (At Risk - 25%):** R: 1.2, F: 3.2, M: $180.
- **Segment C (Low-Value - 60%):** R: 2.1, F: 1.1, M: $22.

**Marketing Campaign Strategy:**
1. **Champions:** Sync to Facebook to build a "Lookalike Audience" to find similar high-value users.
2. **At Risk:** Send an automated email offering 20% off their next purchase to prevent permanent churn.
3. **Low-Value:** Set up low-cost retargeting; do not offer deep margin discounts.

---

## 🔑 Key Takeaway

> Customer segmentation groups buyers by behavior. Use the RFM framework to isolate Champions (high value, high activity) from At-Risk users, allowing marketing teams to optimize margins and retarget effectively.

---

## See It Applied

→ [Who are our best buyers?](../../applied/notebooks/06-who-are-best-buyers.ipynb) — Implementing RFM segmentation in Pandas
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — Customer segmentation profiling

---

[← Day 114: Funnel Analysis](day-114-funnel-analysis.md) · [Next: Day 116 – Dashboard Storytelling →](day-116-dashboard-storytelling.md)
