# Day 148: Canonical Correlation Analysis (CCA)

*Correlation measures the relationship between two variables. Multiple regression measures one variable against many. Canonical Correlation Analysis measures the relationship between one set of variables and another set.*

---

## Learning Objective

Understand Canonical Correlation Analysis (CCA) as a multivariate technique, define canonical variates and canonical correlations, and identify business problems that demand CCA.

---

## The Problem This Solves

You run a customer satisfaction research study. You have:
- **Set 1 (Customer Needs):** Price sensitivity, quality demands, delivery speed rating.
- **Set 2 (Satisfaction Metrics):** CSAT score, net promoter score (NPS), repeat purchase intent.

How do you measure the relationship between these two sets? You could run 9 separate correlation tests, but you'd miss the structural patterns. CCA constructs synthetic variables (variates) from both sets that maximize the correlation between the two sets.

---

## The Concept

### What is CCA?

Canonical Correlation Analysis (CCA) is a multivariate statistical method used to identify and quantify the relationship between **two sets of variables** (Set X and Set Y).

It finds linear combinations of the variables in Set X (called the **X-canonical variate**) and Set Y (called the **Y-canonical variate**) that have the maximum correlation with each other.

```
 Set X (Independent Set)                     Set Y (Dependent Set)
  [ Price Rating ] ──┐                         ┌──► [ CSAT Score ]
  [ Quality      ] ──┼─► [ X-Variate ] ◄─────► ┼──► [ NPS        ]
  [ Speed        ] ──┘   (Maximize Correlation)└──► [ Repeat     ]
```

### The Canonical Variate Equations

For sets `X` and `Y`:

```
U_1 = a_1*X_1 + a_2*X_2 + ... + a_p*X_p
V_1 = b_1*Y_1 + b_2*Y_2 + ... + b_q*Y_q

Goal: Find weights (a, b) to maximize: Correlation(U_1, V_1)
```

The maximized correlation between `U_1` and `V_1` is the **canonical correlation coefficient (R_c)**. 

If you have multiple independent relationships, CCA can extract multiple orthogonal pairs of variates (up to `min(p, q)`).

---

## Why Should a Data Analyst Care?

Because business problems are rarely single-input, single-output. Marketing campaigns have multiple activities (ads, events, emails) that drive multiple outcomes (clicks, leads, brand mentions). CCA is the standard statistical tool to analyze these set-to-set relationships, letting you summarize complex interactions into a few key pathways.

---

## When to Use It

- **Set-to-set relationship analysis** — marketing inputs vs. brand outcomes
- **Psychometrics and HR** - employee skill sets vs. performance metrics
- **Finance** - macroeconomic indicators vs. portfolio sector returns
- **Dimensionality reduction** - finding shared dimensions between two databases

---

## Common Beginner Mistake

Using CCA when a single-outcome multiple regression is sufficient. If you only care about predicting one variable (e.g. CSAT score) from a set of inputs, stick with multiple regression. CCA is only necessary when you have multiple outcomes (Ys) that you want to model as a cohesive group.

---

## Real-World Example

A fitness center analyzes the relationship between exercise behavior and physical health:
- **Set X (Exercise):** Weight training hours, cardio hours, stretching hours.
- **Set Y (Health):** Body fat percentage, resting heart rate, grip strength.

**CCA Results:**
- First Canonical Correlation (R_c1) = **0.78** (p < 0.001).
- **X-Variate 1 Loadings:** Heavy on weight training and cardio.
- **Y-Variate 1 Loadings:** Heavy on lower body fat and lower heart rate.

**Business Interpretation:** There is a strong relationship (0.78) between the exercise set and the health outcome set. The primary pathway connects active training (weight/cardio) with cardiovascular and body composition metrics. Stretching hours and grip strength had low loadings on this first canonical pathway.

---

## 🔑 Key Takeaway

> Canonical Correlation Analysis measures the relationship between two sets of variables by creating synthetic linear combinations (variates) that maximize the correlation between the sets. It is the set-to-set equivalent of Pearson's correlation.

---

[← Day 147: MANOVA](day-147-manova.md) · [Next: Day 149 – Case Study: Customer Experience Index →](day-149-multivariate-case-study.md)
