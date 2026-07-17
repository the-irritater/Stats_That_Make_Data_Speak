# Day 102: Trend

*A trend is the long-term momentum of your business. But to predict the future, you often need to get rid of it.*

---

## Learning Objective

Understand the difference between deterministic and stochastic trends, learn how to identify trends in time series data, and know how to detrend a series using differencing or regression.

---

## The Problem This Solves

You want to know if a marketing campaign increased website visits. Visits have been growing by 5% month-over-month for three years. If you look at the raw data, visits are higher after the campaign than before. 

But was that because of the campaign, or was it just the continuation of the pre-existing trend? To isolate the campaign's effect, you must first calculate and remove the trend (**detrending**).

---

## The Concept

### Types of Trends

| Trend Type | Definition | Mathematical Form | How to Handle |
|------------|------------|-------------------|---------------|
| **Linear (Deterministic)** | Constant absolute growth over time | `Y_t = β₀ + β₁t + ε_t` | Regress Y on time variable `t` and take residuals |
| **Exponential** | Constant percentage growth over time | `Y_t = β₀ * e^(β₁t) * ε_t` | Take `log(Y_t)` first, then linear regression |
| **Stochastic (Random Walk)** | Random step-by-step drift with no fixed anchor | `Y_t = Y_(t-1) + ε_t` | Take the first difference: `Y_t - Y_(t-1)` |

### Why We Detrend: Stationarity

Most advanced time series models require the data to be **stationary**. 
A stationary series has:
- Constant mean over time (no trend)
- Constant variance over time
- Constant autocorrelation structure

If your series has an upward trend, the mean is changing. It is non-stationary.

```
Non-Stationary (Trend present):        Stationary (Detrended / Diffed):

  Value                                  Value
    ▲         ╱                          ▲      
    │       ╱                            │    /\  /\    /\
    │     ╱                              │  /  \/  \  /  \
    │   ╱                                │/         \/    \
    └─────────────────────►              └─────────────────────►
             Time                                 Time
```

### Detrending Method: Differencing

The most common way to remove a trend is **first-order differencing**:

```
ΔY_t = Y_t - Y_(t-1)
```

Instead of modeling the level of sales, you model the *change* in sales from the previous day. This shifts the mean of the series back to a constant level (usually near zero).

---

## Why Should a Data Analyst Care?

Because business leaders conflate "growth" with "success." If a product line is growing simply because the overall economy or market is expanding (tide raising all boats), the trend hides operational inefficiencies. Detrending lets you analyze the underlying health of the business independent of market momentum.

---

## Common Beginner Mistake

Regressing a non-stationary variable on another non-stationary variable. For example, regressing "US Housing Prices" on "Global Temperature." Both have strong upward trends over the last 50 years. You will get an R² of 0.95 and p < 0.001. This is a **spurious regression**. The correlation is driven entirely by the shared time trend, not a causal link. You must diff both variables before regressing.

---

## Real-World Example

An analyst reviews monthly active users (MAU) for a mobile app:

```
Month | MAU (Actual) | First Difference (Change)
──────┼──────────────┼───────────────────────────
Jan   | 100,000      | —
Feb   | 105,000      | +5,000
Mar   | 109,000      | +4,000
Apr   | 115,000      | +6,000
May   | 120,000      | +5,000
```

By modeling the First Difference (+5K, +4K, +6K, +5K), the analyst works with a stationary series centered around a mean of +$5,000. They can now apply forecasting models without violating assumptions.

---

## 🔑 Key Takeaway

> Trends make data non-stationary and cause spurious correlations. To model and forecast safely, remove linear trends via regression residuals, or stochastic trends via first-order differencing.

---

[← Day 101: What Makes Time Series Different?](day-101-intro-to-time-series.md) · [Next: Day 103 – Seasonality →](day-103-seasonality.md)
