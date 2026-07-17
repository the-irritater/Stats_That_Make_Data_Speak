# Day 109: Retail Forecast Case Study

*One retail store. Three years of daily transactions. This is how you build, evaluate, and choose a demand forecasting pipeline.*

---

## Learning Objective

Walk through a complete time series forecasting project — from data decomposition to model selection to operational stock decisions — on a realistic retail dataset.

---

## The Problem

A grocery retailer wants to forecast weekly demand for organic milk to optimize supplier ordering.

**Business targets:**
1. Forecast demand for the next 4 weeks.
2. Maintain a 99% service level (no out-of-stock events) for milk.
3. Choose the simplest model that meets accuracy requirements.

---

## The Analysis Pipeline

### Step 1: Decompose the Historical Data (Day 101)

An analyst reviews 3 years (156 weeks) of weekly sales data:
- **Trend:** Growing steadily at +15 units/week.
- **Seasonality:** Weekly spikes during holidays (Thanksgiving, Christmas) and drop-offs in summer.
- **Noise:** Standard variation.
- **Model choice:** Multiplicative model, as seasonal spikes increase in height as baseline sales grow.

### Step 2: Establish the Validation Split (Day 107)

```
156 Weeks of Data
├── Training Set: Weeks 1–144 (approx. 92%) → Fit models
└── Testing Set:  Weeks 145–156 (12 weeks)  → Evaluate models
```

### Step 3: Compare Candidate Models

The analyst fits three models on the training set and evaluates them on the 12-week test set:

| Model | Test MAE (Units) | Test MAPE (%) | Test RMSE (Units) | Key Characteristic |
|-------|------------------|---------------|-------------------|--------------------|
| **1. Simple 4-Week SMA** | 42 | 8.5% | 51 | Ignores trend and seasonality |
| **2. Holt-Winters (Triple ES)** | 18 | 3.6% | 22 | Captures trend and seasonality |
| **3. ARIMA(1, 1, 1)** | 22 | 4.4% | 27 | Captures autocorrelation, trend adjusted |

### Step 4: Model Selection

**Decision:** The **Holt-Winters** model wins. It achieves the lowest MAPE (3.6%) and RMSE (22 units) because it explicitly models the strong seasonal holiday spikes present in the 12-week test window (November–December).

```
Sales
  ▲
  │              Actuals:  ●───●───●───●
  │              HW:       ●- -●- -●- -● (MAPE 3.6%)
  │              SMA:      o- -o- -o- -o (MAPE 8.5% - lags behind peaks)
  └───────────────────────────────────────►
                         Test Weeks (145-156)
```

### Step 5: Operational Application (Day 108)

Using the winning Holt-Winters model to plan the next order:
- **Forecast for Next Week:** 500 units
- **Model RMSE:** 22 units
- **Desired Service Level:** 99% (Z = 2.33)
- **Supplier Lead Time:** 1 week (Lead Time = 1)

**Safety Stock Calculation:**
```
Safety Stock = Z * RMSE * sqrt(Lead Time)
             = 2.33 * 22 * sqrt(1)
             = 51.26 (round to 52 units)
```

**Reorder Point:**
- `Expected Demand (500) + Safety Stock (52) = 552 units`

---

## Business Impact & Recommendation

1. **Deploy the Holt-Winters model** to generate weekly milk forecasts.
2. **Order 552 units** when stock reaches the reorder point to guarantee a 99% service level.
3. **Save capital:** Moving from the heuristic 4-week SMA model to Holt-Winters reduces the RMSE from 51 to 22. This drops the required safety stock from 119 units to 52 units, **saving 56% in holding costs** while maintaining the same 99% service level.

---

## 🔑 Key Takeaway

> Better forecasting models aren't just academic achievements; they have direct balance sheet impact. Lowering forecast error (RMSE) directly reduces safety stock requirements, freeing up cash for the business.

---

[← Day 108: Business Forecasting](day-108-business-forecasting.md) · [Next: Day 110 – Time Series Recap →](day-110-time-series-recap.md)
