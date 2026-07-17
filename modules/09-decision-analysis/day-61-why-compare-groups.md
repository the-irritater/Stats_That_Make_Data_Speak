# Day 61: Why Compare Groups?

*Every business decision is a comparison. Statistics just makes it honest.*

---

## Learning Objective

Understand why group comparisons are the foundation of data-driven decision making, and learn the framework for choosing the right comparison method.

---

## The Problem This Solves

Your manager asks: *"Did the new checkout flow improve conversion rates?"*

You have data from the old flow and the new flow. The new flow shows 14.2% conversion vs. 12.8% for the old. Is that a real improvement, or just random variation?

Without statistical comparison, you're guessing. With it, you can answer confidently — and quantify how confident you are.

---

## The Concept

Almost every business question is a comparison in disguise:

| Business Question | Statistical Comparison |
|------------------|----------------------|
| Did the campaign work? | Before vs After (paired groups) |
| Which store performs best? | Store A vs B vs C vs D (multiple groups) |
| Do men and women buy differently? | Group 1 vs Group 2 (independent groups) |
| Is the new pricing better? | Control vs Treatment (A/B test) |

### The Decision Tree

The right test depends on three things:

```
What type of data is the outcome?
│
├── Continuous (revenue, time, score)
│   │
│   ├── How many groups?
│   │   ├── 2 groups → t-test (Day 62–63)
│   │   └── 3+ groups → ANOVA (Day 64–65)
│   │
│   └── Are groups independent or paired?
│       ├── Independent → Independent t-test
│       └── Paired → Paired t-test
│
└── Categorical (yes/no, product choice, segment)
    └── Chi-Square test (Day 67)
```

### What Makes a Comparison Valid?

| Requirement | Why It Matters |
|------------|---------------|
| **Random sampling** | Biased samples produce biased comparisons |
| **Sufficient sample size** | Small samples cannot detect real differences |
| **Clear hypothesis** | Define what "different" means *before* looking at data |
| **Appropriate test** | Wrong test → wrong conclusion |

---

## Why Should a Data Analyst Care?

Because stakeholders don't ask for p-values — they ask: *"Is this working?"* Every time you answer that question with data, you're performing a group comparison. The methods in this module are the most commonly used statistical tools in business analytics, marketing, product management, and operations.

---

## When to Use Group Comparisons

- **A/B testing** — did the treatment outperform the control?
- **Performance reviews** — which region, team, or product line is performing differently?
- **Before/after analysis** — did the intervention change the outcome?
- **Segmentation validation** — do customer segments behave differently?

---

## Common Beginner Mistake

Comparing group averages without testing significance. "Group A averaged $42, Group B averaged $45 — B is better!" Maybe. Or maybe that $3 difference is well within random noise. Without a test, you cannot tell. And without effect size, even a significant difference might be too small to act on.

---

## Real-World Example

A retail chain operates 4 stores. Monthly revenue per store:

| Store | Avg Monthly Revenue |
|-------|-------------------|
| Downtown | $142,000 |
| Mall | $138,000 |
| Suburb | $125,000 |
| Airport | $151,000 |

Is Airport really outperforming? Or is this just monthly variation? You need a statistical test (ANOVA) to answer that — and post-hoc tests to identify *which* stores differ. This module teaches you how.

---

## 🔑 Key Takeaway

> Every business decision is a comparison. Statistics gives you the tools to make that comparison rigorous — so your decisions are based on evidence, not gut feeling.

---

## See It Applied

→ [Is this campaign actually working?](../../applied/notebooks/07-is-campaign-working.ipynb) — A/B test comparison in practice
→ [Restaurant Tipping Behavior](../../applied/case-studies/restaurant-tipping-behavior/) — Lunch vs Dinner comparison

---

[← Day 60: Practical Statistics Recap](../08-applied-methods/day-60-practical-statistics-recap.md) · [Next: Day 62 – Independent t-Test →](day-62-independent-t-test.md)
