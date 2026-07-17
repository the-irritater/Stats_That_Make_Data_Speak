# Day 133: Probability of Being Best

*Don't estimate p-values. Calculate the direct probability that your treatment is winning.*

---

## Learning Objective

Understand how to calculate the Probability of Being Best, perform Monte Carlo simulations to estimate joint posteriors, and explain the results to business stakeholders.

---

## The Problem This Solves

You run an A/B/C test comparing three marketing subject lines. The VP asks: *"Which subject line is most likely to win, and what is the probability that it beats the other two?"* 

Frequentist ANOVA or multiple t-tests cannot answer this directly; they can only reject the null hypothesis of overall equality. The Bayesian framework calculates the exact probability of success for each variant: `P(θ_C > θ_B and θ_C > θ_A)`.

---

## The Concept

### The Definition

The **Probability of Being Best** for Variant B is the probability that its parameter `θ_B` is greater than all other variants `θ_j` in the test:

```
P(B is Best) = P(θ_B > θ_A  and  θ_B > θ_C  and ...)
```

### The Calculation Method: Monte Carlo Simulation

For simple two-sample Beta-Binomial models, a closed-form formula exists. However, for multi-variant tests or complex metrics, we calculate this using **Monte Carlo simulation** (sampling):

```
For iteration i = 1 to N (e.g., 100,000 runs):
  1. Draw a random sample θ_A_i from the Control posterior distribution.
  2. Draw a random sample θ_B_i from Variant B's posterior distribution.
  3. Draw a random sample θ_C_i from Variant C's posterior distribution.
  4. Compare the draws: Find which value is the largest.
  5. Increment the win counter for that variant.

Calculate: P(Variant is Best) = Wins / N
```

This simulation takes less than a second to execute in Python, providing exact probabilities for any number of variants.

```
Posteriors:                                     Monte Carlo Simulation (100K draws):
Control:   Beta(40, 960)    ──► Draw 100K ──►   Control Wins:   5.5%   (P(A is Best))
Variant B: Beta(52, 948)    ──► Draw 100K ──►   Variant B Wins: 94.5%  (P(B is Best) ✅)
```

---

## Why Should a Data Analyst Care?

Because business decisions are competitive. When deciding which feature to roll out, stakeholders need a ranking. Probability of Being Best gives you a clear, prioritized list of variants with their exact likelihood of success. It simplifies reporting for multi-variant tests.

---

## When to Use It

- **Multi-variant tests (A/B/C/D)** — comparing multiple landing pages or email designs
- **Ranking features** — identifying which product changes have the highest likelihood of impact
- **Dynamic asset selection** — auto-selecting the best banner in ad networks

---

## Common Beginner Mistake

Assuming that the variant with the highest mean is automatically a safe choice. If Variant B has a mean of 5.2% based on only 100 visitors, and Control has a mean of 4.8% based on 10,000 visitors, Variant B's distribution is extremely wide. The simulation will show that `P(B is Best)` is low (due to high uncertainty). Do not launch based on high means alone; wait for the probability of success to stabilize.

---

## Real-World Example

A retail company tests three checkout button designs (Control, Red, Green):

- **Control (A):** `Beta(120, 2880)` (Mean = 4.0%)
- **Red (B):** `Beta(145, 2855)` (Mean = 4.8%)
- **Green (C):** `Beta(130, 2870)` (Mean = 4.3%)

**Monte Carlo Simulation Results (100,000 runs):**
- **P(Control is Best):** 0.8%
- **P(Red is Best):** 89.4%
- **P(Green is Best):** 9.8%

**Executive Summary:**
"We are 89.4% certain that the Red button layout is the best design, followed by the Green button at 9.8%. The probability that the standard Control layout is superior is under 1%. We recommend deploying the Red layout."

---

## 🔑 Key Takeaway

> Probability of Being Best ranks multiple variants by their likelihood of winning. By drawing random samples from each posterior distribution using Monte Carlo simulations, we calculate exact success probabilities for any number of variants.

---

[← Day 132: The Bayesian A/B Testing Framework](day-132-bayesian-ab-framework.md) · [Next: Day 134 – Expected Loss & Risk Metrics →](day-134-expected-loss.md)
