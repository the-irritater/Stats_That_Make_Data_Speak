# Day 112: North Star Metrics

*If your company has ten main metrics, it has none. A North Star Metric is the single point of alignment that connects user value to business revenue.*

---

## Learning Objective

Understand the concept of a North Star Metric (NSM), analyze how it balances customer value and business monetization, and map supporting input metrics to a North Star framework.

---

## The Problem This Solves

The engineering team wants to speed up page loads. The product team wants to launch new features. The sales team wants to close enterprise deals. The finance team wants to cut costs. 

Each department optimizes for their own local metrics, leading to disjointed products and conflicting strategies. A North Star Metric aligns all departments around a single focal point.

---

## The Concept

### What is a North Star Metric?

The **North Star Metric** is the key measure of product usage that best predicts sustainable business growth. It must capture three things:

```
                  ┌──────────────────────┐
                  │  North Star Metric   │
                  └──────────┬───────────┘
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
     [ Value to User ]  [ Revenue Link ]  [ Measurability ]
     Does the customer  Does growth in    Is it easily
     get real utility?  this metric       calculated
                        generate cash?    from databases?
```

### Mappings of Leading Companies

| Company | North Star Metric | User Value | Business Value (Revenue Link) |
|---------|-------------------|------------|--------------------------------|
| **Spotify** | Time spent listening to music | Entertainment, discoverability | Retention, premium subscription conversions |
| **Airbnb** | Nights booked | Finding lodging easily | Service fees from hosts and guests |
| **Slack** | Daily active users sending messages | Team communication productivity | Conversion to paid enterprise tiers |
| **Zoom** | Meeting minutes hosted | Seamless video collaboration | Expansion of host licensing agreements |

### The North Star Metric Framework

You cannot manage a business on one metric alone. The North Star is supported by **input metrics** that drive it:

```
                           [ North Star Metric ]
                                    ▲
      ┌─────────────────────────────┼─────────────────────────────┐
      │                             │                             │
[ Breadth ]                    [ Depth ]                     [ Frequency ]
How many active users          How engaged are they          How often do they
interact with the product?     per session?                  return to the product?
Example: Weekly active users   Example: Avg minutes/session  Example: Days active/week
```

---

## Why Should a Data Analyst Care?

Because analysts are often asked: *"What should our team focus on next quarter?"* Instead of pulling random data requests, you can use the North Star framework to organize the analysis: *"If our North Star is nights booked, and our breadth is stable, our biggest opportunity is frequency. Let's analyze why repeat bookings are dropping."* This establishes you as a strategic partner, not just a query writer.

---

## Common Beginner Mistake

Choosing a purely financial metric (like "Revenue" or "Stock Price") as the North Star. Revenue is a lagging indicator of business value, but it does **not** measure user value. If you optimize for revenue directly, you might double prices tomorrow — increasing short-term revenue while destroying user value and long-term retention. The North Star must measure *usage value*.

---

## Real-World Example

A health and fitness app selects its North Star Metric:
- **Candidate A:** "Total app downloads." (Vanity. Doesn't measure usage or value).
- **Candidate B:** "Monthly subscription revenue." (Financial. Lagging indicator, doesn't capture user health).
- **Candidate C:** "Number of users completing at least 3 workouts a week." (North Star. Captures user value (health results), predicts subscription retention, and is highly measurable).

**Decision:** Select Candidate C. The marketing, product, and engineering teams will coordinate their experiments to drive this metric.

---

## 🔑 Key Takeaway

> A North Star Metric bridges user value and business revenue. It coordinates company-wide efforts into three main inputs: Breadth (reach), Depth (engagement), and Frequency (retention).

---

[← Day 111: What Makes a Good KPI?](day-111-what-makes-a-good-kpi.md) · [Next: Day 113 – Cohort Analysis →](day-113-cohort-analysis.md)
