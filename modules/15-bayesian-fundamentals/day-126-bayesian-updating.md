# Day 126: Bayesian Updating

*Today's posterior is tomorrow's prior.*

---

## Learning Objective

Understand the recursive nature of Bayesian updating, and execute sequential updates on incoming streams of business data.

---

## The Problem This Solves

You monitor an active A/B test or streaming fraud engine. 
- **Frequentist approach:** You must wait until the end of the experiment to run a single test. If you run multiple tests along the way, you violate assumptions and inflate false positives.
- **Bayesian approach:** You update your probability distribution with every single event. Yesterday's final distribution (posterior) becomes today's baseline (prior). You can stop as soon as you reach decision certainty.

---

## The Concept

### The Recursive Loop

Bayesian updating is sequential. When data arrives in batches (or one by one):

```
  [ Prior 0 ] ──► [ Batch 1 Data ] ──► [ Posterior 1 ]
                                            │
    ┌───────────────────────────────────────┘
    ▼
  [ Prior 1 ] ──► [ Batch 2 Data ] ──► [ Posterior 2 ]
                                            │
    ┌───────────────────────────────────────┘
    ▼
  [ Prior 2 ] ──► [ Batch 3 Data ] ──► [ Posterior 3 ]
```

### The Math: Beta-Binomial Updating

Let's watch this happen over three days:

- **Day 0 Baseline:** We start with an uninformative prior: `Beta(1, 1)`.
- **Day 1 Data:** We observe **10 visitors** and **2 conversions** (k₁=2, n₁=10).
  - `Posterior₁ = Beta(1 + 2, 1 + 8) = Beta(3, 9)`
- **Day 2 Data:** We observe **20 visitors** and **5 conversions** (k₂=5, n₂=20).
  - Using `Posterior₁` as our **new prior**:
  - `Posterior₂ = Beta(3 + 5, 9 + 15) = Beta(8, 24)`
- **Day 3 Data:** We observe **50 visitors** and **12 conversions** (k₃=12, n₃=50).
  - Using `Posterior₂` as our **new prior**:
  - `Posterior₃ = Beta(8 + 12, 24 + 38) = Beta(20, 62)`

### Why the Sequence Doesn't Matter

In Bayesian updating, updating sequentially gives the **exact same result** as updating on all data combined at the end:

- **Total Successes:** `2 + 5 + 12 = 19`
- **Total Failures:** `8 + 15 + 38 = 61`
- **One-step update from Day 0:** `Beta(1 + 19, 1 + 61) = Beta(20, 62)`.

---

## Why Should a Data Analyst Care?

Because businesses operate in streams, not static snapshots. Customer profiles, fraud models, and inventory levels are updated hourly. Bayesian updating allows your models to learn incrementally without reprocessing historical databases from scratch.

---

## When to Use It

- **Streaming data analysis** — fraud detection, spam filters
- **Continuous A/B testing** — updating conversion probabilities daily
- **Operational tracking** — monitoring factory defects or server failures
- **Reactivating cold users** — updating purchase probabilities as behavior decays

---

## Common Beginner Mistake

Using the initial uninformative prior for every batch. If you start each day with `Beta(1, 1)` and only update with that day's data, you throw away all historical knowledge. The posterior from the previous batch must become the prior for the current batch.

---

## Real-World Example

A spam filter evaluates incoming emails for a user:
- **Prior (Initial):** 10% spam base rate.
- **Email 1 arrives:** Contains "Winner" → Posterior spam probability updates to **77%** (Day 122).
- **Email 2 arrives from same sender:** Contains "Cash" → Using the 77% posterior as the **new prior**, the probability updates to **98%**.
- **Action:** Block the sender automatically. The sequential evidence built a highly certain conclusion.

---

## 🔑 Key Takeaway

> Bayesian updating is recursive: today's posterior becomes tomorrow's prior. This allows models to learn incrementally from streaming data without needing to reprocess historical datasets.

---

[← Day 125: Posterior Estimation & Credible Intervals](day-125-credible-intervals.md) · [Next: Day 127 – Bayesian Regression →](day-127-bayesian-regression.md)
