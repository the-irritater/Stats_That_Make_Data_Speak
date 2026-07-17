# Day 100: Module Recap & Experimental Framework

*10 days. One framework: prove cause, control bias, design metrics, make the call.*

---

## Learning Objective

Consolidate everything from Module 12 into a repeatable experimental design framework you can apply to any business problem.

---

## What We Covered (Day 91–100)

| Day | Topic | Core Insight |
|-----|-------|-------------|
| 91 | Correlation vs Causation | Associations describe; causal interventions change |
| 92 | Confounding Variables | Confounders introduce selection bias — block them using controls |
| 93 | Randomized Controlled Experiments | Random assignment balances all variables, isolating the cause |
| 94 | Observational Studies | Natural experiments (DiD, RDD) mimic randomization |
| 95 | A/B Testing Design | Prevent contamination by choosing correct randomization units |
| 96 | Sample Size Planning | Power, MDE, and significance level mathematically lock sample size |
| 97 | Power Analysis & MDE | MDE measures your test's sensitivity; low power causes false negatives |
| 98 | Multiple Testing Problem | Running many tests inflates error rates; adjust with Bonferroni or FDR |
| 99 | Business Case Study | Balancing primary and guardrail metrics to make strategic decisions |

---

## The Causal Decision Tree

```
Do you want to evaluate the impact of an intervention?
│
├── Can you randomly assign the treatment?
│   │
│   ├── YES → Randomized Experiment (A/B Test)
│   │   ├── Choose unit of randomization (User ID, Device, Cookie)
│   │   ├── Determine Primary and Guardrail metrics
│   │   ├── Set target MDE and run Power Analysis for Sample Size
│   │   ├── Check for multiple comparisons (Adjust α via Bonferroni/BH)
│   │   └── Evaluate: Did Treatment cause a significant shift?
│   │
│   └── NO → Observational Study (Use Natural Experiment methods)
│       ├── Do you have historical pre/post data for treatment and control?
│       │   └── YES → Difference-in-Differences (verify Parallel Trends)
│       ├── Is there an arbitrary rule/cutoff defining who gets treatment?
│       │   └── YES → Regression Discontinuity Design (compare near cutoff)
│       └── Is there an external instrument affecting treatment?
│           └── YES → Instrumental Variables
│
└── ALWAYS REPORT: Effect size (lift) + Confidence Intervals (not just p-values)
```

---

## The Analyst's Experiment Checklist

Before approving any product or marketing test, verify these 6 points:

- [ ] **Hypothesis:** What are we testing, and why do we expect a change?
- [ ] **Randomization Unit:** Does this unit prevent user contamination?
- [ ] **Sample Size & Duration:** Has the test run long enough to reach target sample size (avoiding peeking bias)?
- [ ] **Primary Metric:** Is it sensitive enough to capture the change?
- [ ] **Guardrail Metrics:** What business metrics are we protecting?
- [ ] **Multiple Comparison Plan:** Are we adjusting α if testing multiple variants?

---

## How Module 12 Connects to What's Next

| This Module (Causal Inference) | Next Module (Time Series & Forecasting) |
|---------------------------------|-----------------------------------------|
| Focuses on comparisons across groups | Focuses on patterns over time |
| Randomized control groups block time-confounding | Focuses on predicting future values using history |
| Assumes independent observations | Expects time-dependent observations (autocorrelation) |
| Measures historical impact | Forecasts future metrics (sales, demand) |

Module 12 asked: *"Did our change cause the lift?"*
Module 13 asks: *"Given historical trends, seasonality, and noise, what will this metric be next month?"*

---

## 🔑 Key Takeaway

> Data analytics is not just about writing SQL queries or training models; it's about decision science. Experimental design gives you the mathematical framework to tell stakeholders: "This change caused this impact." That is the language of business value.

---

[← Day 99: Business Experiment Case Study](day-99-experiment-case-study.md) · [Back to Module 12](README.md)
