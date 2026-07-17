# Day 104: Moving Average

*A moving average acts like a pair of noise-canceling headphones for your charts. It quietens the daily chatter so you can hear the music.*

---

## Learning Objective

Understand how moving averages smooth time series data, calculate simple and centered moving averages, and know how they are used as a baseline forecasting method.

---

## The Problem This Solves

Your website traffic chart looks like a saw blade: huge spikes on weekdays, massive drops on weekends, and random spikes when a post gets shared. The CEO looks at it and asks: *"Are we growing or shrinking?"* 

The daily fluctuations (noise) are so loud that you cannot see the trend. A moving average smooths out this noise.

---

## The Concept

### What is a Moving Average?

A moving average (rolling average) calculates the mean of a variable within a sliding window of time.

### Simple Moving Average (SMA) - Causal/Lagging

Used for forecasting. Calculates the average of the last `k` periods:

```
SMA_t = (Y_t + Y_(t-1) + ... + Y_(t-k+1)) / k
```

### Centered Moving Average (CMA) - Two-Sided

Used for historical analysis/decomposition. Calculates the average of the window centered around the target day:

```
CMA_t = (Y_(t-1) + Y_t + Y_(t+1)) / 3
```

### Window Size (k) and the Tradeoff

The choice of window size `k` determines the smooth-vs-responsiveness balance:

```
Raw Data  →  [ 7-Day SMA ]  →  [ 30-Day SMA ]
(Noisy)      (Responsive)      (Ultra-Smooth, but lags changes)
```

- **Symmetric Windows:** To smooth out weekly seasonality (S = 7), use a 7-day window. To smooth out yearly seasonality from monthly data (S = 12), use a 12-month window.

### The Lag Effect

Because a causal moving average relies on past data, it introduces **lag**. If sales suddenly surge on Monday, a 30-day moving average won't show the full surge until weeks later.

---

## Why Should a Data Analyst Care?

Because moving averages are the most common dashboard metric. When you see a "7-day rolling average" or "30-day active users" on a chart, that's a moving average. It is the default tool for tracking KPIs without getting distracted by day-of-week seasonality.

---

## Common Beginner Mistake

Using a centered moving average for forecasting. Centered moving averages require future data (`Y_(t+1)`). Since you cannot see the future on the current day, you cannot calculate a centered moving average for today to predict tomorrow. Only use simple (backward-looking) moving averages for forecasting.

---

## Real-World Example

A retail analyst tracks daily transactions:

```
Day | Transactions | 3-Day SMA (Causal) | 3-Day CMA (Centered)
────┼──────────────┼────────────────────┼──────────────────────
1   | 120          | —                  | —
2   | 150          | —                  | (120+150+110)/3 = 126.7
3   | 110          | (120+150+110)/3=126.7| (150+110+160)/3 = 140.0
4   | 160          | (150+110+160)/3=140.0| (110+160+130)/3 = 133.3
5   | 130          | (110+160+130)/3=133.3| —
```

**Business usage:** The 3-Day SMA on Day 4 (140.0) is the forecast for Day 5. The CMA is used to chart historical trends without daily spikes.

---

## 🔑 Key Takeaway

> Moving averages smooth out short-term fluctuations to reveal long-term trends. Choose a window size that matches your seasonal period (7 days for weekly, 12 months for yearly) to eliminate seasonal noise completely.

---

[← Day 103: Seasonality](day-103-seasonality.md) · [Next: Day 105 – Exponential Smoothing →](day-105-exponential-smoothing.md)
