# Day 123: Understanding Priors

*A prior is not a guess. It is a mathematical summary of your current state of knowledge before you look at new data.*

---

## Learning Objective

Distinguish between informative, uninformative (flat), and conjugate priors, and understand how prior selection influences posterior estimations.

---

## The Problem This Solves

You want to run a conversion experiment. If you tell stakeholders, *"I think the conversion rate is between 2% and 4%,"* they might accuse you of bias. 

How do you express your prior assumptions mathematically and transparently so that the model can be audited? You define a **prior probability distribution** that maps your uncertainty.

---

## The Concept

### Types of Priors

Depending on your confidence and data history, you choose one of three priors:

#### 1. Uninformative (Flat / Weakly Informative) Priors
Used when you have no prior information or want the data to speak entirely for itself.
*Example:* A uniform distribution `Uniform(0, 1)` stating that any conversion rate from 0% to 100% is equally likely.
*Effect:* The posterior is driven entirely by the likelihood of the new data.

#### 2. Informative Priors
Used when you have historical data, benchmarks, or physical constraints.
*Example:* A Normal distribution centered at 5% with a small standard deviation.
*Effect:* Restricts the posterior, preventing extreme shifts unless the new dataset is massive.

#### 3. Conjugate Priors
A mathematical shortcut. A prior is **conjugate** to the likelihood if the resulting posterior distribution belongs to the *same probability family* as the prior.

| Likelihood (Data Type) | Conjugate Prior | Posterior Distribution |
|------------------------|-----------------|------------------------|
| **Binomial** (Success/Failure) | **Beta** | **Beta** |
| **Poisson** (Counts over time) | **Gamma** | **Gamma** |
| **Normal** (Continuous) | **Normal** | **Normal** |

Using conjugate priors allows you to calculate the posterior using simple addition rather than complex integrals.

```
Prior Distribution (Beta)  +  Likelihood (Binomial)  =  Posterior Distribution (Beta)
(Analytical solution — no complex simulation needed)
```

---

## Why Should a Data Analyst Care?

Because choosing the right prior prevents your models from outputting impossible results. If you build a model to predict retail demand without a prior, a small sample size might forecast negative demand. An informative prior (stating that demand must be >0) prevents this.

---

## Common Beginner Mistake

Believing that informative priors are "unscientific" because they introduce subjectivity. 

Every statistical model contains subjective assumptions (e.g., assuming a normal distribution or a linear trend). A prior is simply an explicit, transparent assumption. If you have historical data, ignoring it by using an uninformative prior is actually less scientific than incorporating it.

---

## Real-World Example

A subscription business tests a checkout flow:
- **Baseline historical rate:** 4.0%
- **Informative Prior:** Beta(4, 96) — equivalent to having observed 4 conversions in 100 visits.
- **Uninformative Prior:** Beta(1, 1) — equivalent to any rate from 0% to 100% being equally likely.

If you run a test with 50 visits and 0 conversions:
- **Using Uninformative Prior:** Estimated conversion drops to **1.9%**.
- **Using Informative Prior:** Estimated conversion drops slightly to **2.7%**.

The informative prior prevented the model from overreacting to a tiny sample of 50 users.

---

## 🔑 Key Takeaway

> Priors represent your baseline knowledge. Uninformative priors let the data dominate. Informative priors prevent overreactions to small samples. Conjugate priors (like Beta for Binomial data) make calculations fast and simple.

---

[← Day 122: Bayes' Theorem in Action](day-122-bayes-theorem-distribution.md) · [Next: Day 124 – The Beta-Binomial Model →](day-124-beta-binomial-model-analysis.md)
