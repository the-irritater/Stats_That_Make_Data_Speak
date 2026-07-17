# Module 13: Time Series & Forecasting

*Data is not just static tables. Real business data flows over time. Learn how to isolate trends, handle seasonality, and forecast future values.*

---

## Before You Begin

Before starting this module, you should have a solid understanding of:
- **Regression (Module 6 & 10):** Independent vs. dependent variables, intercept and slope.
- **Moving Average Concepts:** Simple averages calculated over windows of data.
- **Error Metrics (Module 9 & 11):** MAE, RMSE, and basic model evaluation.

---

## Learning Path

| Day | Topic | Key Question |
|-----|-------|-------------|
| 101 | [What Makes Time Series Different?](day-101-intro-to-time-series.md) | How do trend, seasonality, and noise compose temporal data? |
| 102 | [Trend](day-102-trend.md) | How do we identify, isolate, and model long-term movements? |
| 103 | [Seasonality](day-103-seasonality.md) | How do we capture repeating cycles in business data? |
| 104 | [Moving Average](day-104-moving-average.md) | How do rolling windows smooth noise to reveal the signal? |
| 105 | [Exponential Smoothing](day-105-exponential-smoothing.md) | How do we prioritize recent data for near-term forecasting? |
| 106 | [ARIMA Concept](day-106-arima-concept.md) | What are autoregressive models and how do they work? |
| 107 | [Forecast Accuracy](day-107-forecast-accuracy.md) | How do we evaluate model performance over time? |
| 108 | [Business Forecasting](day-108-business-forecasting.md) | How do we apply forecasting to sales, demand, and inventory? |
| 109 | [Retail Forecast Case Study](day-109-forecast-case-study.md) | How do we build and test a retail sales forecasting pipeline? |
| 110 | [Time Series Recap](day-110-time-series-recap.md) | What is our unified forecasting decision framework? |

---

## The Big Idea

Most datasets you've analyzed so far assume observations are independent. In time series, this assumption breaks down. Today's sales depend heavily on yesterday's sales, last week's sales, and last year's sales. This module teaches you the specific statistical techniques required to handle time-dependent data and forecast what's next.

> The ability to predict next quarter's revenue or next week's inventory demands is a key driver of strategic business value.

---

## See It Applied

→ [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb) — Basic temporal EDA
→ [Analyzing customer spending patterns](../../applied/notebooks/02-customer-spending-patterns.ipynb) — Handling date columns and group aggregations

---

[← Module 12: Experimental Design & Causal Inference](../12-experimental-design/) · [Next: Module 14 – Modern Analytics & Decision Science →](../14-decision-science/)
