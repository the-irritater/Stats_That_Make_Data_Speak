# Day 131: Why Frequentist A/B Testing Fails in Business

*Frequentist A/B testing was designed for agricultural fields in the 1920s. Modern digital businesses need speed, not crop cycles.*

---

## Learning Objective

Understand the structural constraints of frequentist A/B testing in a business context, identify the risks of peeking bias, and explain why p-values fail to support business utility decisions.

---

## The Problem This Solves

You launch a conversion A/B test. The product manager checks the dashboard every morning. On day 3, they see a p-value of 0.04. They shout: *"We have a winner! Stop the test and roll it out!"* 

If you stop the test, you commit a critical error. In frequentist statistics, checking the p-value repeatedly (peeking) inflates the false positive rate from 5% to over 30%. Frequentist testing requires you to wait until a pre-calculated sample size is reached, forcing the business to run slow, rigid tests.

---

## The Concept

### The Core Failure Points of Frequentist A/B Testing

```
  1. The Peeking Penalty (False positive inflation from checking data early)
                  ↓
  2. The Fixed Sample Size Trap (Must wait weeks for n, even if treatment is losing horribly)
                  ↓
  3. The p-Value Delusion (p = 0.03 doesn't tell you the probability that B is better)
```

#### 1. Peeking Bias (False Positive Inflation)
In frequentist testing, the significance threshold (α = 0.05) assumes you will run the statistical test **exactly once** at the end. If you check (peek) 10 times during the experiment and stop if p < 0.05:

```
Number of Peeks | True False Positive Rate (actual α)
────────────────┼─────────────────────────────────────
1 (Standard)    | 5.0%
5               | 14.2%
10              | 19.3%
100             | 32.4%
```

You end up deploying "winners" that are actually random noise.

#### 2. The Fixed Sample Size Trap
To avoid peeking bias, you must calculate a target sample size (e.g. 50,000 users) and keep the test running until that size is met. If Variant B is broken and dropping revenue by 40%, you *still* must keep running the test on thousands of users to maintain statistical validity. This is economically irrational.

#### 3. Misinterpretation of p-Values
A p-value is the probability of observing this data *if the null hypothesis is true*: `P(Data | H₀)`. 
Business leaders want to know the probability *that the treatment is better*: `P(H₁ | Data)`. 
These are not the same. A p-value cannot answer the business question directly.

---

## Why Should a Data Analyst Care?

Because technology companies need to iterate quickly. If you tell a product team they must wait 4 weeks to complete a test because of frequentist math, they will bypass you and launch without tests. Bayesian A/B testing allows you to peek safely, stop tests early, and frame results in terms of probability and revenue risk.

---

## Common Beginner Mistake

Stopping an A/B test early because the p-value crossed 0.05 on day 2. Early results have high variance. If you stop the test early, you are selecting for a transient noise spike. This is called the **early stopping fallacy**.

---

## Real-World Example

A retail site runs a frequentist A/B test on checkout flows:
- **Target sample size:** 20,000 visitors per group (duration: 20 days).
- **Day 5:** Control has 200 conversions, Treatment has 280. p = 0.012.
- **The Dilemma:** If they stop now, they risk a false positive due to peeking. If they wait 15 more days, they waste conversions on a clearly superior checkout flow.

Under frequentist rules, they must wait. Under Bayesian rules, they can evaluate the posterior expected loss today and stop the test safely.

---

## 🔑 Key Takeaway

> Frequentist A/B testing is mathematically rigid: it penalizes peeking, demands fixed sample sizes, and outputs p-values that don't measure the probability of success. Businesses need flexible, risk-based frameworks.

---

[← Module 16 README](README.md) · [Next: Day 132 – The Bayesian A/B Testing Framework →](day-132-bayesian-ab-framework.md)
