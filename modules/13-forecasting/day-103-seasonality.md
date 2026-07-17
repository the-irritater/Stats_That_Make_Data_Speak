# Day 103: Seasonality

*If your sales spike every Friday, that's not a breakthrough — it's just the weekend.*

---

## Learning Objective

Understand seasonality as a repeating pattern in time series data, identify seasonal periods (weekly, yearly), and learn how to deseasonalize a series to reveal the true underlying trend.

---

## The Problem This Solves

You review Q4 sales performance. E-commerce sales grew by 40% compared to Q3. You recommend doubling the marketing budget because the current strategy is working incredibly well. 

What you missed: Q4 contains Black Friday and holiday shopping. E-commerce sales *always* grow by 40–50% in Q4. Your strategy didn't cause the lift; the calendar did. Deseasonalizing the data lets you see if Q4 performed better or worse than the historical holiday average.

---

## The Concept

### What is Seasonality?

Seasonality consists of periodic fluctuations that repeat at regular, predictable intervals less than a year.

### Seasonal Periods (S)

The number of observations in a complete seasonal cycle:

| Data Frequency | Seasonal Cycle | Period Length (S) |
|----------------|----------------|-------------------|
| Daily | Weekly | `7` (pattern repeats every Monday) |
| Hourly | Daily | `24` (pattern repeats every midnight) |
| Monthly | Yearly | `12` (pattern repeats every December) |
| Quarterly | Yearly | `4` (pattern repeats every Q4) |

### How to Remove Seasonality (Deseasonalization)

To compare month-over-month performance fairly, we calculate **Seasonally Adjusted** values.

#### Additive Model Adjustment
```
Seasonally Adjusted Y_t = Y_t - S_t
```

#### Multiplicative Model Adjustment (Most Common)
```
Seasonally Adjusted Y_t = Y_t / S_t
```

Where `S_t` is the **Seasonal Index** for that period. An index of `1.25` for December means December sales are typically 25% higher than the average month. An index of `0.85` for January means January is typically 15% lower.

---

## Why Should a Data Analyst Care?

Because reporting raw metrics over time leads to poor business decisions. If you report weekly user signups, the Monday peaks and Sunday troughs create visual noise that hides long-term trends. Deseasonalizing (or looking at a 7-day rolling average) removes this calendar noise.

---

## Common Beginner Mistake

Confusing **seasonality** with **cycles**:
- **Seasonality:** Repeating patterns with a fixed, known period (e.g., winter coat sales in December).
- **Cyclical Patterns:** Fluctuations without a fixed period, often driven by economic cycles (e.g., housing booms every 5–8 years). 

Standard forecasting models handle seasonality easily, but struggle with economic cycles.

---

## Real-World Example

A subscription business reviews monthly churn rates:

```
Month | Churn (Raw) | Historical Seasonal Index | Seasonally Adjusted Churn
──────┼─────────────┼───────────────────────────┼──────────────────────────
Nov   | 2.8%        | 0.95                      | 2.8% / 0.95 = 2.95%
Dec   | 3.4%        | 1.20 (holiday cancellations)| 3.4% / 1.20 = 2.83%
Jan   | 2.9%        | 1.00                      | 2.9% / 1.00 = 2.90%
```

**Interpretation:**
Looking at raw churn, December looks like a disaster (3.4% vs 2.8% in Nov). But after adjusting for seasonality, December's adjusted churn (2.83%) was actually the *lowest* in the quarter. The holiday churn spike was smaller than usual. The retention campaigns in December worked.

---

## 🔑 Key Takeaway

> Seasonality is calendar-driven noise. To evaluate the true health of a business, calculate seasonal indices and divide (or subtract) them from your raw metrics to generate seasonally adjusted trends.

---

[← Day 102: Trend](day-102-trend.md) · [Next: Day 104 – Moving Average →](day-104-moving-average.md)
