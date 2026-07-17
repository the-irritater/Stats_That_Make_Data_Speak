# Day 106: ARIMA Concept

*ARIMA is the Swiss Army knife of classical forecasting. It combines past values, past errors, and differencing to model almost any stationary time series.*

---

## Learning Objective

Understand the conceptual building blocks of the ARIMA model — Autoregressive (AR), Integrated (I), and Moving Average (MA) components — and interpret their parameters (p, d, q).

---

## The Problem This Solves

Your time series has complex patterns: it trends upward, drops on weekends, and when a sales spike happens, the effect slowly decays over the next three days. Simple moving averages or exponential smoothing are too simple to capture all these elements together. 

ARIMA provides a unified statistical framework that models these compounding patterns.

---

## The Concept

**ARIMA** stands for **AutoRegressive Integrated Moving Average**. It is defined by three parameters: `ARIMA(p, d, q)`.

```
ARIMA(p, d, q)
  │   │  │
  │   │  └── q: Moving Average (MA) order → lags of forecast errors
  │   └───── d: Integrated (I) order → number of differences to make it stationary
  └───────── p: Autoregressive (AR) order → lags of the dependent variable
```

### The Three Components

#### 1. Autoregressive: AR(p)
The model predicts the current value using a linear combination of its own **past values** (lags).
*Analogy:* "If sales were high for the last `p` days, they will likely be high today."
*Formula:* `Y_t = c + ϕ₁*Y_(t-1) + ... + ϕ_p*Y_(t-p) + ε_t`

#### 2. Integrated: I(d)
The number of times the raw observations are **differenced** to make the time series stationary (remove trends).
*Analogy:* "If the data trends upward, we difference it `d` times until it is flat."
*Example:* `d = 1` means we model `Y_t - Y_(t-1)`.

#### 3. Moving Average: MA(q)
The model predicts the current value based on a linear combination of **past forecast errors** (shocks).
*Analogy:* "If we had an unexpected sales spike yesterday (positive error), some of that shock will carry over today."
*Formula:* `Y_t = c + ε_t + θ₁*ε_(t-1) + ... + θ_q*ε_(t-q)`

### How parameters affect the forecast:
- **ARIMA(1, 0, 0) - Simple AR(1):** Yesterday's value predicts today's. If `ϕ₁ = 0.8`, a spike decays by 20% each day.
- **ARIMA(0, 1, 0) - Random Walk:** Tomorrow's forecast is simply today's value plus random noise.
- **ARIMA(0, 1, 1) - Simple Exponential Smoothing:** Equivalent to SES (Day 105) modeled via differencing and error lags.

---

## Why Should a Data Analyst Care?

Because ARIMA is the industry standard for univariate (single-variable) time series forecasting. Before jumping to deep learning or complex ML models, statisticians always fit an ARIMA baseline. Knowing how to interpret `(p, d, q)` parameters is a mark of statistical maturity.

---

## Common Beginner Mistake

Fitting ARIMA on non-stationary data without differencing (`d = 0`). If your data has a trend and you don't difference it, ARIMA's forecast will quickly collapse to a flat line or drift off to infinity. Always set `d` appropriately (usually 1 or 2) to stabilize the mean.

---

## Real-World Example

A call center analyst models daily inbound support tickets:
- **Model Selected:** `ARIMA(1, 1, 1)`
- **Interpretation:**
  - `d = 1` → We model the *day-over-day change* in tickets (removes long-term growth trend).
  - `p = 1` → The change in tickets today is correlated with the change yesterday.
  - `q = 1` → If we had a sudden spike in tickets yesterday (e.g. system outage error), that shock affects today's volume.

The model captures both the momentum of the trend and the decay rate of sudden operational shocks.

---

## 🔑 Key Takeaway

> ARIMA(p, d, q) builds forecasts from past values (AR), trend removal (I), and past errors (MA). It is a highly flexible, mathematically rigorous baseline for forecasting stationary time series.

---

[← Day 105: Exponential Smoothing](day-105-exponential-smoothing.md) · [Next: Day 107 – Forecast Accuracy →](day-107-forecast-accuracy.md)
