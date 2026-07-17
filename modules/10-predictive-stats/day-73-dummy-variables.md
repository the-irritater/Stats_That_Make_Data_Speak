# Day 73: Dummy Variables

*Categories are not numbers. But regression needs numbers. Dummy variables are the bridge.*

---

## Learning Objective

Understand how to encode categorical variables as dummy (indicator) variables for regression, interpret their coefficients, and avoid the dummy variable trap.

---

## The Problem This Solves

You want to include "region" (North, South, East, West) in your regression model. But regression requires numerical inputs. You can't assign North = 1, South = 2, East = 3, West = 4 — that implies South is "twice" North, which is meaningless. Dummy variables convert categories into a set of binary (0/1) indicators that regression can use correctly.

---

## The Concept

### How Dummy Encoding Works

For a variable with k categories, create k - 1 dummy variables. One category becomes the **reference group** (coded as all zeros).

| Region | is_South | is_East | is_West |
|--------|----------|---------|---------|
| North | 0 | 0 | 0 |
| South | 1 | 0 | 0 |
| East | 0 | 1 | 0 |
| West | 0 | 0 | 1 |

**North** is the reference group (represented when all dummies = 0).

### Interpreting Coefficients

```
Y = β₀ + β₁(is_South) + β₂(is_East) + β₃(is_West) + ε
```

| Coefficient | Meaning |
|------------|---------|
| β₀ | Mean Y for the **reference group** (North) |
| β₁ | Difference in mean Y: South **minus** North |
| β₂ | Difference in mean Y: East **minus** North |
| β₃ | Difference in mean Y: West **minus** North |

Each dummy coefficient is a **comparison to the reference group**.

### The Dummy Variable Trap

If you include all k dummies (instead of k - 1), the model has **perfect multicollinearity** — the dummies perfectly predict each other (they always sum to 1). This causes the regression to fail.

```
WRONG: Include all 4 dummies → multicollinearity
RIGHT: Include 3 dummies + one reference group
```

### Choosing the Reference Group

The reference group changes the coefficients but not the model's predictions. Choose the reference that makes interpretation easiest:

- **Largest group** — most stable baseline
- **Control group** — natural comparison point
- **Business baseline** — "before" condition, standard plan, or main region

---

## Why Should a Data Analyst Care?

Because most real-world datasets contain categorical variables: department, product category, region, gender, subscription tier. Without dummy variables, you can't include them in regression. With them, you can quantify exactly how each category differs from the baseline — and test whether those differences are significant.

---

## When to Use It

- **Including categories in regression** — any non-numeric predictor
- **A/B testing with covariates** — treatment group as a dummy variable
- **Seasonal effects** — month or quarter as dummy variables
- **Comparing segments** — customer tier, product line, channel

---

## Common Beginner Mistake

Using label encoding (North = 1, South = 2, ...) instead of dummy variables. This tells the model that South is "one unit more" than North, which implies an ordering and equal spacing that doesn't exist. Always use dummy encoding for nominal (unordered) categories. Ordinal categories *might* use integer encoding — but only if the spacing is meaningful.

---

## Real-World Example

Predicting employee salary ($K) using years of experience and department:

| Predictor | β | p-value | Interpretation |
|-----------|---|---------|---------------|
| Intercept | 42.0 | < 0.001 | Baseline salary for Engineering (reference) with 0 years |
| Years Experience | 3.8 | < 0.001 | +$3,800/year of experience |
| is_Marketing | -5.2 | 0.003 | Marketing earns $5,200 less than Engineering |
| is_Sales | +2.1 | 0.184 | Sales vs Engineering: not significantly different |
| is_HR | -8.4 | < 0.001 | HR earns $8,400 less than Engineering |

**Business insight:** After controlling for experience, Engineering and Sales have similar salaries. Marketing and HR earn significantly less. This might warrant a compensation review.

---

## 🔑 Key Takeaway

> Dummy variables let you include categories in regression by creating binary indicators. Each coefficient measures the difference between that category and the reference group. Use k - 1 dummies to avoid the trap, and choose your reference group wisely.

---

## See It Applied

→ [Restaurant Tipping Behavior](../../applied/case-studies/restaurant-tipping-behavior/) — Day of week as a categorical predictor
→ [Signature Project: Customer Analytics](../../applied/signature-project/) — Segment-level regression analysis

---

[← Day 72: Multiple Linear Regression](day-72-multiple-linear-regression.md) · [Next: Day 74 – Interaction Effects →](day-74-interaction-effects.md)
