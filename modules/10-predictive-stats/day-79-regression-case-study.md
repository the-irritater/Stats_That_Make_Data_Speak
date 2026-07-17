# Day 79: Regression Case Study — House Price Prediction

*One dataset. One question. Every regression technique from this module, applied start to finish.*

---

## Learning Objective

Walk through a complete regression analysis pipeline — from data preparation to model selection to interpretation — using house price prediction as the business problem.

---

## The Problem

A real estate company wants to understand what drives house prices and build a model to estimate property values for new listings.

**Business questions:**
1. Which features most influence house prices?
2. Can we predict price accurately enough for listing recommendations?
3. Are there interaction effects (e.g., does location modify the effect of size)?

---

## The Analysis Pipeline

### Step 1: Understand the Data

| Variable | Type | Description |
|----------|------|-------------|
| `price` | Continuous ($K) | Target variable |
| `sqft` | Continuous | Living area in square feet |
| `bedrooms` | Discrete | Number of bedrooms |
| `bathrooms` | Discrete | Number of bathrooms |
| `age` | Continuous | Years since construction |
| `neighborhood` | Categorical | Downtown, Suburb, Rural |
| `has_garage` | Binary | 0/1 |
| `lot_size` | Continuous | Lot area in acres |
| n = 500 houses |

### Step 2: Simple Regression — Start Simple

**Model 1:** price ~ sqft

```
price = 45.2 + 0.152 × sqft
R² = 0.54, Adj R² = 0.54
```

Each additional square foot → $152 increase in price. Size alone explains 54% of price variation. Good start, but we can do better.

### Step 3: Multiple Regression — Add Predictors

**Model 2:** price ~ sqft + bedrooms + bathrooms + age + lot_size + has_garage

| Predictor | β | p-value | VIF |
|-----------|---|---------|-----|
| sqft | 0.128 | < 0.001 | 3.42 |
| bedrooms | -8.5 | 0.072 | 2.85 |
| bathrooms | 22.4 | < 0.001 | 2.31 |
| age | -1.8 | < 0.001 | 1.15 |
| lot_size | 18.3 | 0.002 | 1.28 |
| has_garage | 15.7 | 0.008 | 1.09 |

R² = 0.72, Adj R² = 0.71

**Key insight:** Bedrooms has a *negative* coefficient when controlling for sqft — because for a fixed size, more bedrooms means smaller rooms (quality signal). This is Simpson's paradox in action.

### Step 4: Add Categorical Predictors — Dummy Variables

**Model 3:** Add neighborhood (reference = Rural)

| Predictor | β | p-value |
|-----------|---|---------|
| (all previous) | ... | ... |
| is_Downtown | +85.3 | < 0.001 |
| is_Suburb | +32.1 | < 0.001 |

R² = 0.81, Adj R² = 0.80

Downtown houses command $85K more than equivalent Rural houses. Location matters enormously.

### Step 5: Test for Interactions

**Model 4:** Add sqft × neighborhood interaction

| Predictor | β | p-value |
|-----------|---|---------|
| sqft | 0.095 | < 0.001 |
| is_Downtown | -12.4 | 0.512 |
| sqft × is_Downtown | 0.068 | 0.003 |
| sqft × is_Suburb | 0.025 | 0.145 |

R² = 0.83, Adj R² = 0.82

**Interpretation:** The value of an extra square foot depends on location. Downtown: $95 + $68 = $163/sqft. Suburb: $95 + $25 = $120/sqft. Rural: $95/sqft. Size matters more in expensive neighborhoods.

### Step 6: Model Selection

| Model | Predictors | Adj R² | AIC | BIC |
|-------|-----------|--------|-----|-----|
| 1. Simple | 1 | 0.54 | 5820 | 5828 |
| 2. Multiple | 6 | 0.71 | 5542 | 5571 |
| 3. + Dummies | 8 | 0.80 | 5380 | 5418 |
| 4. + Interaction | 10 | 0.82 | 5345 | 5393 |
| 5. Lasso-selected | 7 | 0.81 | 5352 | 5382 |

**Decision:** Model 5 (Lasso-selected) offers the best BIC with strong Adj R². Lasso dropped bedrooms, the Suburb interaction, and lot_size — keeping the model lean and interpretable.

### Step 7: Final Model Validation

Train-test split (80/20):
- **Train RMSE:** $38,200
- **Test RMSE:** $41,500
- **Test R²:** 0.79

The model generalizes well — test performance is close to training.

---

## Business Recommendations

1. **Location is the strongest driver** — Downtown premium is ~$85K over Rural
2. **Size matters more in premium areas** — invest in larger properties Downtown
3. **Age depresses value** — each year → $1,800 lower price; renovation opportunities
4. **Garage adds ~$16K** — cost-effective renovation for houses without one
5. **Bedroom count is misleading** — more bedrooms in the same sqft signals lower quality

---

## 🔑 Key Takeaway

> A complete regression analysis is iterative: start simple, add complexity with purpose, diagnose problems, select the best model, and validate on holdout data. The final model should be accurate, interpretable, and defensible.

---

## See It Applied

→ [Predicting customer spend](../../applied/notebooks/04-predicting-customer-spend.ipynb) — Similar pipeline with e-commerce data
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — Full regression with HC3-robust inference

---

[← Day 78: Logistic Regression](day-78-logistic-regression.md) · [Next: Day 80 – Module Recap →](day-80-predictive-stats-recap.md)
