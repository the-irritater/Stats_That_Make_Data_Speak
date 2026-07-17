# Day 108: Business Forecasting

*A forecast is not a magic crystal ball. It is a decision support tool that balances the cost of holding inventory against the cost of losing a sale.*

---

## Learning Objective

Apply time series forecasting to three classic business problems: sales forecasting, demand planning, and inventory control, and understand how to set safety stock levels using forecast error distribution.

---

## The Problem This Solves

You forecast next week's demand for a product to be 1,000 units. If you stock exactly 1,000 units, you will run out of stock 50% of the time (because the forecast is the mean of a distribution). 

How do you calculate how many *extra* units (safety stock) to keep in the warehouse to guarantee you don't run out of stock 95% of the time? You use the distribution of your forecast error.

---

## The Concept

### The Three Pillars of Business Forecasting

```
  Sales Forecasting (Revenue)   →   Demand Planning (Volume)   →   Inventory Control (Stock)
  "How much cash will we make?"      "How many units will sell?"     "When and how much to order?"
```

### Safety Stock & Forecast Error

If your forecast errors are normally distributed with a mean of zero and standard deviation `RMSE`:

```
Safety Stock = Z * RMSE * sqrt(Lead Time)

Where:
  Z         = Z-score corresponding to the desired Service Level (e.g. 1.64 for 95%)
  RMSE      = Root Mean Squared Error of the forecasting model
  Lead Time = Number of days it takes for a new order to arrive at the warehouse
```

This formula shows that:
1. **Better forecasts (lower RMSE)** directly reduce the amount of capital locked up in safety stock.
2. **Longer supplier lead times** require exponentially more safety stock.

### Common Business Applications

| Application | Primary Metric | Target Time Horizon | Key User |
|-------------|----------------|---------------------|----------|
| **Revenue Planning** | Sales ($) | Quarterly / Annual | CFO / Finance |
| **Workforce Scheduling** | Support Ticket Volume | Hourly / Weekly | Operations Manager |
| **Supply Chain** | Product Demand (Units) | Monthly | Warehouse Manager |

---

## Why Should a Data Analyst Care?

Because reducing inventory costs is one of the easiest ways to prove direct ROI as an analyst. If you can improve demand forecast accuracy by 5%, you can save a retail company hundreds of thousands of dollars in warehouse holding costs and write-offs.

---

## Common Beginner Mistake

Generating a point forecast and assuming the job is done. A forecast of "1,000 units" is incomplete without a **confidence interval**. Operations teams need to know the worst-case and best-case scenarios to plan capacity. Always report the forecast with its prediction intervals.

---

## Real-World Example

A warehouse planner manages a popular product:
- **Supplier Lead Time:** 4 days
- **Daily Demand Forecast:** 100 units/day
- **Model RMSE:** 15 units/day
- **Target Service Level:** 95% (Z = 1.64)

**Calculations:**
- **Base Demand during Lead Time:** `4 days * 100 units = 400 units`
- **Safety Stock:** `1.64 * 15 * sqrt(4) = 1.64 * 15 * 2 = 49.2` (round to 50 units)
- **Reorder Point:** `Base Demand (400) + Safety Stock (50) = 450 units`

**Decision:** When stock drops to 450 units, place a new order. The 50 units of safety stock protect the business against spikes in demand or supplier delays, ensuring a 95% service level.

---

## 🔑 Key Takeaway

> Business forecasting connects statistical models to operational decisions. By using forecast RMSE to calculate safety stock, you translate model accuracy directly into reduced inventory holding costs.

---

[← Day 107: Forecast Accuracy](day-107-forecast-accuracy.md) · [Next: Day 109 – Retail Forecast Case Study →](day-109-forecast-case-study.md)
