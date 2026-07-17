# Day 107: Forecast Accuracy

*If you don't evaluate your forecasts on holdout data, you aren't forecasting — you're backcasting.*

---

## Learning Objective

Evaluate forecast models using Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), and Root Mean Squared Error (RMSE), and understand how time series validation differs from standard train/test splits.

---

## The Problem This Solves

You build a forecasting model. It fits your historical data perfectly (high R²). You use it to predict next month's sales. It's off by 50%. 

Why? Because you evaluated the model on the same data used to train it. To measure real-world performance, you must test the forecast on a **future holdout window** that the model has never seen.

---

## The Concept

### Time Series Validation (Time-Based Split)

In standard ML, we shuffle data randomly before splitting. In time series, you **cannot shuffle** — doing so would leak future information into the past. You must split chronologically:

```
Full Chronological Series
├── Training Period (Past) (80%) → Fit the model
└── Testing Period (Future) (20%) → Evaluate the forecast
```

### The Three Core Accuracy Metrics

```
Let y_t = Actual value at time t,  ŷ_t = Forecasted value at time t
Error: e_t = y_t - ŷ_t
```

| Metric | Formula | What It Measures | When to Use |
|--------|---------|-----------------|-------------|
| **MAE** | `mean(|e_t|)` | Average absolute error in scale units | When error cost scales linearly (a $10 error is twice as bad as $5) |
| **RMSE** | `sqrt(mean(e_t²))` | Penalizes larger errors more heavily | When large errors are disproportionately costly |
| **MAPE** | `mean(|e_t| / y_t) * 100` | Average error as a percentage of the actual value | To compare performance across products with different scales (e.g., low vs. high volume) |

### The Scale Dependency Issue

- **MAE & RMSE** are scale-dependent. An RMSE of 500 is tiny if average sales are 1,000,000, but massive if average sales are 1,000.
- **MAPE** is scale-independent, but fails if actual values are zero or near-zero (division by zero).

---

## Why Should a Data Analyst Care?

Because business managers don't care about the math behind ARIMA; they care about the error rate: *"How far off are we typically?"* If you can state: *"Our model predicts sales with a MAPE of 8.5%, meaning we are typically within 8.5% of the true value,"* you are speaking the language of business risk management.

---

## Common Beginner Mistake

Evaluating time-series forecasts using standard cross-validation. Standard K-fold CV shuffles the rows. If the model uses "yesterday's sales" to predict "today's sales," shuffling means the model trains on tomorrow's sales to predict today's. This is massive **data leakage** and produces artificially perfect metrics that collapse in production.

---

## Real-World Example

An analyst compares two forecasting models for monthly signups over a 6-month holdout test set:

| Month | Actual | Model 1 Forecast | Model 1 Absolute Error | Model 2 Forecast | Model 2 Absolute Error |
|-------|--------|------------------|------------------------|------------------|------------------------|
| Jul | 1,000 | 950 | 50 | 1,100 | 100 |
| Aug | 1,200 | 1,150 | 50 | 1,100 | 100 |
| Sep | 1,100 | 1,050 | 50 | 1,100 | 10 |
| **Mean**| **1,100**| **—** | **MAE = 50** | **—** | **MAE = 70** |

- **Model 1 (MAE = 50, MAPE = 4.6%):** Consistent, small errors.
- **Model 2 (MAE = 70, MAPE = 6.4%):** Predicts a flat mean (1,100). Misses the seasonal peaks but stays safe.

**Decision:** Model 1 is superior because it tracks the variation, yielding lower absolute and percentage errors.

---

## 🔑 Key Takeaway

> Never evaluate forecasts using shuffled data. Use a chronological train/test split. Report MAPE for executive context, and RMSE if large forecast errors have severe financial consequences.

---

[← Day 106: ARIMA Concept](day-106-arima-concept.md) · [Next: Day 108 – Business Forecasting →](day-108-business-forecasting.md)
