# Day 146: Exploratory vs. Confirmatory Factor Analysis

*Exploratory Factor Analysis is a fishing trip; Confirmatory Factor Analysis is a test of your theoretical roadmap.*

---

## Learning Objective

Distinguish between Exploratory Factor Analysis (EFA) and Confirmatory Factor Analysis (CFA), and identify when to apply each to validate metrics structures.

---

## The Problem This Solves

You design a new customer feedback survey. You *intend* for 3 questions to measure "Usability" and 3 questions to measure "Value." 

If you run an Exploratory Factor Analysis, the algorithm will group the questions based purely on data correlations — which might group them differently than you planned. If you run a Confirmatory Factor Analysis, you define your planned mapping explicitly and test if the actual data fits your theory.

---

## The Concept

### The Core Difference

| Dimension | Exploratory Factor Analysis (EFA) | Confirmatory Factor Analysis (CFA) |
|-----------|----------------------------------|-----------------------------------|
| **Goal** | Discover underlying structure/patterns in data. | Confirm a pre-specified theoretical model. |
| **Approach** | Data-driven. Let the data group the variables. | Theory-driven. You define the groups. |
| **Cross-loadings** | Every variable loads on every factor (we search for the strongest). | Variables are restricted to load *only* on their assigned factor. |
| **Stage of Research** | Early stage: exploratory or scale development. | Late stage: testing a validated scale on new data. |
| **Software Engine** | Principal Axis Factoring / Maximum Likelihood. | Structural Equation Modeling (SEM) covariance fitting. |

### The Visual Structure

```
EFA (All paths open):                      CFA (Restricted paths):

  [ Factor 1 ] ──┬──► [ X₁ ]                 [ Factor 1: Usability ] ──► [ X₁ ]
                 ├──► [ X₂ ]                                         ──► [ X₂ ]
  [ Factor 2 ] ──┼──► [ X₃ ]                 
                 └──► [ X₄ ]                 [ Factor 2: Value ]     ──► [ X₃ ]
                                                                     ──► [ X₄ ]
  (Algorithm searches for best loads)        (You restrict other paths to zero)
```

### CFA Fit Indices

To determine if the data supports your theoretical structure in CFA, we check fit statistics:
- **RMSEA (Root Mean Square Error of Approximation):** Want **< 0.06**. (Measures badness of fit).
- **CFI (Comparative Fit Index):** Want **> 0.95**. (Measures goodness of fit).
- **TLI (Tucker-Lewis Index):** Want **> 0.95**. (Measures goodness of fit).

If fit indices are poor, your theoretical mapping is rejected by the data. The questions did not measure what you thought they did.

---

## Why Should a Data Analyst Care?

Because customer-facing businesses rely on questionnaires and feedback loops. If you want to build a "Brand Health Index" or an "NPS Satisfaction Score" that executives trust, you must validate that the survey questions are statistically reliable. EFA allows you to explore the questions, and CFA confirms the index is mathematically valid.

---

## Common Beginner Mistake

Running CFA on the same dataset used for EFA. If you run EFA to discover that questions 1, 3, and 5 group together, and then run CFA on the *same data* to confirm that group, your test is circular and invalid. You must run EFA on a split sample (e.g. 50% of the data), refine the model, and then run CFA on the remaining 50% (holdout sample) to confirm.

---

## Real-World Example

A product analyst validates an app review index:
- **Theory:** 6 questions measure two latent factors: `Utility` (q1-q3) and `Design` (q4-q6).
- **CFA Test Execution:**
  - Define the path: `Utility → q1, q2, q3` and `Design → q4, q5, q6`. Set cross-loadings to zero.
  - **Results:** CFI = 0.98, TLI = 0.97, RMSEA = 0.03.
- **Business Interpretation:** The fit indices are excellent. The data strongly supports the theoretical construct. The analyst is cleared to aggregate `q1-q3` into a single "Utility Score" and `q4-q6` into a "Design Score" for the product roadmap dashboard.

---

## 🔑 Key Takeaway

> EFA discovers structure when you don't have a plan; CFA tests whether your theoretical structure fits the data. Always split your sample when moving from exploration to confirmation to avoid circular validation.

---

[← Day 145: Factor Analysis](day-145-factor-analysis.md) · [Next: Day 147 – MANOVA →](day-147-manova.md)
