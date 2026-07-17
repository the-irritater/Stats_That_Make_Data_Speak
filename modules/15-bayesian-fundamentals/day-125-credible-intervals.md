# Day 125: Posterior Estimation & Credible Intervals

*A confidence interval tells you about the interval, not the parameter. A credible interval tells you exactly what you want to know: the probability that the parameter lies within that range.*

---

## Learning Objective

Calculate and interpret Bayesian Credible Intervals (Highest Density Intervals vs. Equal-Tailed Intervals), and understand how they differ conceptually from Frequentist Confidence Intervals.

---

## The Problem This Solves

You present a 95% Confidence Interval for a conversion rate: `[4.2%, 6.8%]`. 

The product manager asks: *"Does this mean there is a 95% probability that our true conversion rate is between 4.2% and 6.8%?"*

In frequentist statistics, the answer is **no**. (The true parameter is fixed; only the interval is random). You must give a convoluted explanation about "95% of repeated samples..." 

A Bayesian Credible Interval allows you to say **yes** — there is a 95% probability the rate is in that range.

---

## The Concept

### Credible Interval (Bayesian)

A credible interval is a range of values within the posterior distribution that contains a specified proportion of the probability. Because parameters are random variables in Bayesian statistics, we can make direct probability statements about them.

There are two main types of credible intervals:

| Interval Type | How It is Built | Best For |
|---------------|-----------------|----------|
| **Equal-Tailed Interval (ETI)** | Cuts off equal probabilities at both tails (e.g. 2.5% on left, 2.5% on right for 95% interval). | Symmetric distributions (Normal, symmetric Beta). Easy to calculate. |
| **Highest Density Interval (HDI)** | The narrowest interval containing the specified probability. Every point inside the interval has higher density than points outside. | Skewed distributions (e.g. Beta prior to observing many trials). |

```
Symmetric (ETI = HDI):                  Skewed (HDI is narrower/preferred):

       ETI / HDI                             HDI
       ┌───────┐                          ┌───────┐
      ╱    │    ╲                        ╱    │    ╲
    _╱     │     ╲_                     ╱     │     ╲_
  ─'               `─                 ─'              `─
  0       0.5       1                 0      0.2       1
```

### Credible vs. Confidence Intervals

| Dimension | Confidence Interval (Frequentist) | Credible Interval (Bayesian) |
|-----------|-----------------------------------|------------------------------|
| **Parameter Status** | Fixed, unknown constant. | Random variable with a distribution. |
| **Meaning of "95%"** | "If we run this test 100 times, 95 of the generated intervals will contain the true parameter." | "There is a 95% probability that the true parameter lies within this specific interval." |
| **Depends On** | The hypothetical sample space of repeated trials. | The current observed data + prior assumptions. |

---

## Why Should a Data Analyst Care?

Because business stakeholders think like Bayesians. They don't understand long-run frequentist properties; they want to make decisions about the *current* campaign: *"What is the probability that our conversion rate is above 5%?"* Bayesian credible intervals allow you to answer this question directly and intuitively.

---

## Common Beginner Mistake

Giving the Bayesian interpretation to a frequentist confidence interval. This is the most common mistake in data science. If you use `scipy` or `statsmodels` to output an OLS confidence interval, do **not** say "there is a 95% probability the parameter is in this range." If you want that statement, you must fit a Bayesian model and output a credible interval.

---

## Real-World Example

An analyst fits a Beta-Binomial model to checkout conversions and gets a posterior distribution of `Beta(25, 475)`. They calculate a 95% Credible Interval (ETI):

- **95% Credible Interval:** `[3.2%, 7.1%]`
- **Mean Estimate:** `25 / 500 = 5.0%`

**Executive Summary:**
"Based on our experiment data and prior conversions, the estimated conversion rate is 5.0%. There is a 95% probability that the true conversion rate lies between 3.2% and 7.1%."

This is clear, correct, and directly actionable.

---

## 🔑 Key Takeaway

> Credible intervals represent direct probability statements about a parameter: "there is a 95% chance the parameter is in this range." Use Highest Density Intervals (HDI) for skewed distributions to find the narrowest range of likely values.

---

[← Day 124: The Beta-Binomial Model](day-124-beta-binomial-model.md) · [Next: Day 126 – Bayesian Updating →](day-126-bayesian-updating.md)
