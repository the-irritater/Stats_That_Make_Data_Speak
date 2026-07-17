# Day 75: Multicollinearity

*When predictors are too similar, the model can't tell them apart — and neither can you.*

---

## Learning Objective

Understand multicollinearity as a regression problem, diagnose it using VIF, and know the practical strategies for handling it.

---

## The Problem This Solves

You include both `total_pages_viewed` and `session_duration` in a regression predicting purchase amount. Both are significant individually, but when included together, neither is significant — and one even flips sign. What happened? These two predictors are so correlated that the model can't separate their individual effects. That's multicollinearity.

---

## The Concept

### What Is Multicollinearity?

Multicollinearity occurs when two or more predictors are highly correlated with each other. The model struggles to determine which predictor is responsible for the effect.

### What It Does (and Doesn't Do)

| Aspect | Effect |
|--------|--------|
| **Predictions** | Usually unaffected — the model still predicts well |
| **Coefficients** | Unstable — large standard errors, sign changes |
| **p-values** | Inflated — real effects appear non-significant |
| **Interpretation** | Unreliable — can't isolate individual predictor effects |
| **R²** | Usually unaffected |

### Detecting It: Variance Inflation Factor (VIF)

VIF measures how much the variance of a coefficient is inflated due to collinearity with other predictors.

```
VIF(Xⱼ) = 1 / (1 - R²ⱼ)

Where R²ⱼ = R-squared from regressing Xⱼ on all other predictors
```

| VIF Value | Interpretation |
|-----------|---------------|
| VIF = 1 | No collinearity |
| VIF = 1–5 | Moderate (usually acceptable) |
| VIF = 5–10 | High (investigate) |
| VIF > 10 | Severe (action needed) |

### Solutions

| Strategy | When to Use | Trade-off |
|----------|------------|-----------|
| **Drop one predictor** | Two predictors measure the same thing | Lose some information |
| **Combine predictors** | Create an index (e.g., average of correlated items) | Reduces dimensionality |
| **Ridge regression** | Need all predictors, want stable coefficients | Coefficients are biased but stable |
| **Increase sample size** | Moderate collinearity | Doesn't help severe cases |
| **Accept it** | Prediction is the goal, not interpretation | Coefficients are unreliable but predictions are fine |

---

## Why Should a Data Analyst Care?

Because multicollinearity is one of the most common problems in real-world regression. Business data is full of correlated predictors: marketing spend and brand awareness, price and quality tier, education and experience. If you don't check for it, you'll report misleading coefficients — and stakeholders will make wrong decisions based on them.

---

## When to Check

- **Always** when running multiple regression — VIF should be a standard diagnostic
- **When coefficients seem surprising** — unexpected signs or non-significance for known important predictors
- **When adding new predictors** — each addition can introduce collinearity
- **When coefficients are unstable** — small changes in data cause large coefficient changes

---

## Common Beginner Mistake

Panicking when VIF is above 1. Some collinearity is normal and harmless. VIF = 3 means coefficients have 3× the variance they would without collinearity — but they're still usable. Only act when VIF > 5–10 or when coefficients become uninterpretable. Also: ignoring multicollinearity because R² looks fine. R² doesn't detect it.

---

## Real-World Example

An e-commerce model predicting order value:

| Predictor | β | p-value | VIF |
|-----------|---|---------|-----|
| Pages Viewed | +3.48 | < 0.001 | 7.26 |
| Session Duration (min) | +0.82 | 0.312 | 6.89 |
| Items in Cart | +12.30 | < 0.001 | 1.45 |
| Is Returning Customer | +5.60 | 0.008 | 1.12 |

**Diagnosis:** Pages Viewed and Session Duration have high VIF (>5). They're correlated (r = 0.81) — customers who view more pages naturally spend more time.

**Decision:** Drop Session Duration (VIF = 6.89). Pages Viewed captures the engagement signal more directly. After dropping:

| Predictor | β | p-value | VIF |
|-----------|---|---------|-----|
| Pages Viewed | +4.12 | < 0.001 | 1.18 |
| Items in Cart | +12.45 | < 0.001 | 1.42 |
| Is Returning Customer | +5.72 | 0.006 | 1.10 |

Coefficients are now stable and interpretable.

---

## 🔑 Key Takeaway

> Multicollinearity doesn't break predictions — it breaks interpretation. If you need to explain *why* a model works (and in business, you always do), check VIF and address high collinearity before presenting coefficients to stakeholders.

---

## See It Applied

→ [Signature Project: Customer Analytics](../../applied/signature-project/) — VIF = 7.26 caveat documented in results
→ [Restaurant Tipping Behavior](../../applied/case-studies/restaurant-tipping-behavior/) — VIF diagnostics in regression

---

[← Day 74: Interaction Effects](day-74-interaction-effects.md) · [Next: Day 76 – Model Selection →](day-76-model-selection.md)
