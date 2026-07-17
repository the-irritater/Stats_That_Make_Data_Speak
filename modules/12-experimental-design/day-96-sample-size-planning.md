# Day 96: Sample Size Planning

*If you don't collect enough data, your experiment is just a coin flip. If you collect too much, you've wasted time and money.*

---

## Learning Objective

Understand how statistical power, significance level, baseline conversion rate, and Minimum Detectable Effect (MDE) mathematically determine the sample size required for an A/B test.

---

## The Problem This Solves

A product manager asks: *"How long do we need to run this A/B test?"* 

If you guess "two weeks," you might stop the test with 2,000 users when you actually needed 20,000 to detect the target lift. You report "no significant difference" and kill a winning feature. Or, you keep running a test for months when you had enough statistical power on day 10, delaying production rollouts.

---

## The Concept

### The 4 Variables of Sample Size

Calculating required sample size requires fixing four variables:

| Variable | What It Is | Standard Choice | Impact on Sample Size |
|----------|------------|-----------------|-----------------------|
| **Significance Level (α)** | Probability of Type I Error (False Positive) | `0.05` (5%) | Lower α (e.g. 1%) → **Larger sample** |
| **Statistical Power (1 - β)** | Probability of catching a real effect | `0.80` (80%) | Higher power (e.g. 90%) → **Larger sample** |
| **Baseline Rate (p)** | Current performance of the control group | Determined by history | Extreme rates (near 0% or 100%) → **Smaller sample** |
| **Minimum Detectable Effect (MDE)** | The smallest lift the business cares about | Business decision | Smaller MDE (detecting tiny changes) → **Exponentially larger sample** |

### The Power Curve Relationship

```
Required Sample Size (n)
  ▲
  │        ╱
  │      ╱
  │    ╱   ← As MDE shrinks, the sample size
  │  ╱       requirements balloon exponentially.
  │╱
  └─────────────────────────────►
   Large MDE   →   Small MDE
```

### The Analytical Formula (for Proportions)

For a two-sided two-sample proportion test with equal allocation:

```
n = [ (Z_α/2 + Z_β)² * (p₁(1-p₁) + p₂(1-p₂)) ] / (p₁ - p₂)²

Where:
  Z_α/2 = Z-score for significance (1.96 for 95% confidence)
  Z_β   = Z-score for power (0.84 for 80% power)
  p₁    = baseline conversion rate
  p₂    = treatment conversion rate (p₁ + MDE)
```

---

## Why Should a Data Analyst Care?

Because running underpowered tests is the most common resource leak in data departments. Underpowered tests generate p-values > 0.05 even when features work. You end up telling teams their work has no impact when you simply didn't collect enough data to prove it.

---

## Common Beginner Mistake

Treating MDE as the lift you *hope* to get, rather than the smallest lift that makes the feature economically viable. If a feature costs $10,000 to maintain, you might set the MDE to the lift required to break even on that cost. Setting the MDE too low (e.g., 0.1% lift) forces you to run experiments for months to detect a change that doesn't cover its own maintenance cost.

---

## Real-World Example

An e-commerce site wants to test a checkout page layout:
- **Baseline Conversion (p):** 5.0%
- **Target Lift (relative):** 10% lift (absolute MDE = 0.5%, target p₂ = 5.5%)
- **α (Significance):** 0.05
- **Power (1 - β):** 0.80

Using a sample size calculator:
- **Required sample size:** **~31,000 users per group** (62,000 total users).
- **Traffic context:** If the site gets 2,000 visitors/day, the test must run for **31 days**.

If the team wants to detect a smaller relative lift of 5% (absolute MDE = 0.25%):
- **Required sample size:** **~122,000 users per group** (244,000 total).
- The test would have to run for **122 days**. The business must decide if a 5% lift is worth 4 months of waiting.

---

## 🔑 Key Takeaway

> Sample size planning is a mathematical contract. You cannot detect small improvements without large samples. Always calculate requirements before writing a single line of testing code.

---

[← Day 95: A/B Testing Design](day-95-ab-testing-design.md) · [Next: Day 97 – Power Analysis & Minimum Detectable Effect (MDE) →](day-97-power-analysis-mde.md)
