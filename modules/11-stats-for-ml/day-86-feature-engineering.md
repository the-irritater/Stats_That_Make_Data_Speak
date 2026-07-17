# Day 86: Feature Engineering

*The best algorithm in the world cannot learn from bad inputs. Feature engineering is how you give it something worth learning.*

---

## Learning Objective

Understand feature engineering as the process of creating better model inputs, learn the most common techniques, and know why it matters more than algorithm choice.

---

## The Problem This Solves

Raw data rarely comes in a form models can learn from effectively. Dates are strings. Categories are text. Important signals are hidden inside existing columns. Feature engineering transforms raw data into inputs that make patterns obvious to the model.

---

## The Concept

### Common Techniques

| Technique | What It Does | Example |
|-----------|-------------|---------|
| **Encoding** | Converts categories to numbers | "Red", "Blue" → one-hot encoding |
| **Binning** | Groups continuous values into ranges | Age → "18-25", "26-35", "36-50" |
| **Log Transform** | Compresses skewed distributions | Income ($1K–$1M) → log(Income) |
| **Interaction Features** | Captures combined effects | `price_per_unit = price / quantity` |
| **Date Extraction** | Pulls signals from timestamps | Order date → day_of_week, is_weekend |
| **Aggregations** | Summarizes related records | Customer → avg_order_value, total_orders |
| **Rolling Statistics** | Captures trends over time | 7-day rolling average of sales |

### Scaling

| Method | Formula | When to Use |
|--------|---------|-------------|
| **Standardization** | (x - mean) / std | Linear models, regularization, distance-based algorithms |
| **Min-Max** | (x - min) / (max - min) | When you need values in [0, 1] |
| **No scaling** | Raw values | Tree-based models (don't need scaling) |

### The Connection to Statistics

| Statistical Concept | Feature Engineering Application |
|--------------------|---------------------------------|
| Log transformation (Day 39) | Fixing skewness in predictors |
| Dummy variables (Day 73) | Encoding categorical features |
| Interaction effects (Day 74) | Creating interaction features |
| Standardization (Day 7) | Z-score scaling for regularization |
| RFM analysis (Notebook 06) | Engineering recency, frequency, monetary features |

You've already been doing feature engineering — ML just gives it a name and makes it systematic.

---

## Why Should a Data Analyst Care?

Feature engineering is where domain knowledge meets modeling. No algorithm can know that "days since last purchase" matters more than "customer ID." You create that feature. Studies consistently show that feature engineering has more impact on model performance than algorithm selection.

---

## Common Beginner Mistake

Creating too many features without thinking. Adding 50 polynomial interactions creates noise, not signal. Create features with a hypothesis about *why* they should matter. Also: forgetting to scale features before algorithms that need it (linear models, KNN) while unnecessarily scaling for tree-based models.

---

## Real-World Example

An analyst predicts customer churn. Raw data: `customer_id`, `order_date`, `order_amount`, `product_category`.

Engineered features:
- `days_since_last_order` — recency signal
- `avg_order_value` — spending pattern
- `order_count_last_90_days` — engagement level
- `unique_categories_purchased` — breadth of interest
- `is_weekend_shopper` — behavioral pattern

These 5 engineered features outperform the 4 raw columns because they capture *behavior*, not just transactions.

---

## 🔑 Key Takeaway

> Algorithms learn from features. Better features → better models. The analyst who understands the business creates better features than the engineer who only understands the algorithm.

---

## See It Applied

→ [What actually drives sales?](../../applied/notebooks/03-what-drives-sales.ipynb) — Feature-level correlation analysis
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — RFM features engineered from raw transactions

---

[← Day 85: Bias–Variance Tradeoff](day-85-bias-variance-tradeoff.md) · [Next: Day 87 – Decision Trees →](day-87-decision-trees.md)
