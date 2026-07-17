# Day 101: What Makes Time Series Different?

*In a time series, history doesn't just repeat itself — it correlates with itself.*

---

## Learning Objective

Understand how time series data differs from cross-sectional data, learn the concept of autocorrelation, and explain the classic additive and multiplicative decomposition models (Trend, Seasonality, Noise).

---

## The Problem This Solves

You want to predict sales for next month. You fit a standard linear regression model using features like price and advertising. The model assumes every row is an independent observation. 

But your data is weekly sales. If sales were high last week (due to a viral post), they are likely to remain high this week as the wave settles. This temporal dependency is called **autocorrelation**. Ignoring it violates regression assumptions and makes your forecast intervals dangerously narrow and overconfident.

---

## The Concept

### Cross-Sectional vs. Time Series Data

- **Cross-Sectional Data:** Multiple subjects observed at a single point in time (e.g., customer metrics last month).
- **Time Series Data:** A single subject observed repeatedly at regular intervals over time (e.g., daily active users over 365 days).

### Classical Decomposition Model

We model a time series variable `Y_t` as a combination of three distinct components:

1. **Trend (T_t):** The long-term upward or downward direction of the data over years.
2. **Seasonality (S_t):** Repeating, predictable patterns that occur over fixed intervals (e.g., high retail sales every December, high website traffic every Monday).
3. **Noise (I_t / Random):** Unpredictable, random variations (white noise) that cannot be explained by trend or seasonality.

#### The Mathematical Composites

Depending on how the components interact, we model the series as:

- **Additive Model:** `Y_t = T_t + S_t + Noise_t`
  - *Use when:* The size of the seasonal variation stays constant regardless of the level of the trend.
- **Multiplicative Model:** `Y_t = T_t × S_t × Noise_t`
  - *Use when:* The seasonal variation scales with the trend (e.g., as the business grows, holiday peaks get taller).

```
Additive (Constant Spread):           Multiplicative (Expanding Spread):

  Value                                 Value
    ▲         /\                          ▲         /\
    │   /\   /  \   /\                    │   /\   /  \   /\
    │  /  \ /    \ /  \                   │  /  \ /    \ /  \
    │ /    V      V    \                  │ /    V      V    \  /\
    └─────────────────────►               │/                  \/  \
             Time                         └─────────────────────────►
                                                   Time
```

---

## Why Should a Data Analyst Care?

Because time is the context of every business metric. If you report a 10% sales drop in January compared to December without mentioning that January always drops by 15% due to post-holiday seasonal effects, you will cause panic. Understanding time series decomposition allows you to report **seasonally adjusted** figures.

---

## Common Beginner Mistake

Applying standard linear regression directly to highly autocorrelated time series data without checking the Durbin-Watson statistic or residuals. This leads to **spurious regression** — finding highly significant p-values for relationships that are purely co-trending over time.

---

## Real-World Example

A subscription streaming company analyzes monthly signups:
- **Baseline Trend:** Growing steadily at +5,000 users/month.
- **Seasonality:** Signups spike in winter (December/January) when people are indoors, and drop in summer (July/August).
- **Noise:** A sudden spike in March due to a celebrity mentioning a show.

If the analyst reports a signup drop in July, they must check if the drop is larger or smaller than the typical summer seasonal factor. If the drop is smaller than usual, the business is actually performing *better* than expected once adjusted for seasonality.

---

## 🔑 Key Takeaway

> Time series data violates the independence assumption of classical statistics. To analyze it, we decompose the series into Trend (long-term direction), Seasonality (repeating cycles), and Noise (random variation).

---

[← Module 13 README](README.md) · [Next: Day 102 – Trend →](day-102-trend.md)
