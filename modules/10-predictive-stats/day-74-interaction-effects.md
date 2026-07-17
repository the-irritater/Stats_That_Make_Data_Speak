# Day 74: Interaction Effects

*Sometimes the effect of one variable depends on another. That's not noise — that's an interaction.*

---

## Learning Objective

Understand interaction effects in regression, know when to include them, and interpret interaction coefficients correctly.

---

## The Problem This Solves

Your model shows that experience increases salary by $3,800/year and that marketing employees earn $5,200 less than engineering. But what if the pay gap *widens* with experience — engineering gets bigger raises? A main effects model misses this. An interaction term captures it.

---

## The Concept

### What Is an Interaction?

An interaction occurs when the effect of one predictor on Y **depends on the level of another predictor**.

### The Model

```
Without interaction:
Y = β₀ + β₁X₁ + β₂X₂ + ε

With interaction:
Y = β₀ + β₁X₁ + β₂X₂ + β₃(X₁ × X₂) + ε
```

The interaction term β₃(X₁ × X₂) captures how the slope of X₁ changes across values of X₂.

### Interpreting Interaction Coefficients

```
Y = 40 + 4.0(Experience) - 5.0(is_Marketing) - 1.5(Experience × is_Marketing)

For Engineering (is_Marketing = 0):
  Y = 40 + 4.0(Experience)
  → Slope = 4.0 per year

For Marketing (is_Marketing = 1):
  Y = 40 + 4.0(Experience) - 5.0 - 1.5(Experience)
  Y = 35 + 2.5(Experience)
  → Slope = 2.5 per year
```

**Interpretation:** Engineering salaries grow by $4,000/year. Marketing salaries grow by only $2,500/year. The gap widens with experience.

### Visualizing Interactions

```
Salary                              Salary
  │      Engineering ──────╱          │      Engineering ─────
  │                      ╱            │
  │      Marketing ────╱              │      Marketing ─────
  │                  ╱                │
  └───────────────────                └───────────────────
    Experience                          Experience

  Non-parallel lines → interaction      Parallel lines → no interaction
```

### Types of Interactions

| Type | Variables | Example |
|------|----------|---------|
| **Continuous × Continuous** | X₁ × X₂ | Does ad effectiveness depend on price? |
| **Continuous × Categorical** | X × D | Does experience affect salary differently by department? |
| **Categorical × Categorical** | D₁ × D₂ | Does the channel effect depend on the tier? (Same as Two-Way ANOVA!) |

---

## Why Should a Data Analyst Care?

Because main effects models assume all predictors act independently — and in business, they rarely do. Price sensitivity depends on income level. Marketing effectiveness depends on the channel. Training impact depends on job role. Interactions reveal *where* an effect is strongest, which is exactly what stakeholders need for targeted decisions.

---

## When to Include Interactions

- **When you suspect the effect varies** — "Does this work differently for different segments?"
- **When Two-Way ANOVA showed an interaction** — the regression version of interaction effects
- **When domain knowledge suggests it** — marketing spend × seasonality, price × competitor count
- **Not by default** — adding all possible interactions leads to overfitting. Be selective.

---

## Common Beginner Mistake

Including an interaction without the main effects. The model `Y = β₀ + β₃(X₁ × X₂)` is almost always wrong because it forces the individual effects of X₁ and X₂ to be zero. Always include both main effects when you include their interaction — this is called the **hierarchy principle**.

---

## Real-World Example

Predicting customer satisfaction (1–100) from resolution time (hours) and support channel:

| Predictor | β | p-value |
|-----------|---|---------|
| Intercept | 85.0 | < 0.001 |
| Resolution Time (hours) | -3.2 | < 0.001 |
| is_Email (vs Chat) | -8.0 | 0.002 |
| Resolution Time × is_Email | -1.8 | 0.015 |

**For Chat:** Satisfaction = 85 - 3.2 × Hours → Each hour costs 3.2 points
**For Email:** Satisfaction = 77 - 5.0 × Hours → Each hour costs 5.0 points

**Business insight:** Slow resolution hurts more on email than chat. A 4-hour email resolution loses 20 satisfaction points; the same delay on chat loses 12.8. Priority: reduce email resolution times first.

---

## 🔑 Key Takeaway

> Interaction effects reveal that the effect of one variable depends on another. Non-parallel slopes in a plot signal an interaction. Including them makes your model more realistic — but only add interactions you have a reason to suspect.

---

[← Day 73: Dummy Variables](day-73-dummy-variables.md) · [Next: Day 75 – Multicollinearity →](day-75-multicollinearity.md)
