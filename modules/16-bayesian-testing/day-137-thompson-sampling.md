# Day 137: Thompson Sampling

*Thompson Sampling is the mathematical bridge that routes traffic in proportion to the probability that a variant is the winner.*

---

## Learning Objective

Understand Thompson Sampling (posterior matching) as a Bayesian bandit algorithm, explain how it balances exploration and exploitation, and implement its basic logic.

---

## The Problem This Solves

You want to run a bandit algorithm to optimize ad traffic. If you use a greedy algorithm (always route traffic to the current leader), you will get stuck in local optima (e.g., routing 100% of traffic to a variant that got lucky on the first 5 visits, ignoring other variants that might be better). 

Thompson Sampling solves this by routing traffic in proportion to the *probability* that a variant is the best, allowing uncertain variants to explore until they are proven inferior.

---

## The Concept

### The Core Idea: Posterior Matching

Thompson Sampling is an elegant Bayesian heuristic: **allocate the next visitor to a variant with a probability equal to the probability that the variant is the best.**

### The Algorithm Loop

Instead of complex mathematics, Thompson Sampling runs a simple sampling loop for every incoming visitor:

```
For each user arrival:
  1. Draw a random sample θ_A from the posterior distribution of Control: Beta(α_A, β_A).
  2. Draw a random sample θ_B from the posterior distribution of Variant B: Beta(α_B, β_B).
  3. Draw a random sample θ_C from the posterior distribution of Variant C: Beta(α_C, β_C).
  
  4. Compare the draws: Assign the user to the variant with the largest drawn value.
  
  5. Observe the outcome (Conversion = 1 or 0).
  6. Update that variant's posterior parameters (α = α + conversion,  β = β + (1 - conversion)).
```

### Why it balances Exploration and Exploitation

- **Exploitation:** The leading variant has a narrower posterior centered at a higher value. Its draws will be consistently high, so it gets the majority of the traffic.
- **Exploration:** A new or highly uncertain variant has a very wide posterior. Even if its mean is lower, its wide distribution means it still occasionally generates a very high draw, earning some traffic. As it gets traffic, its posterior narrows. If it is actually worse, the draws drop, and traffic naturally fades away.

```
Posteriors:                                     Thompson Sampling Draws:
Control (Narrow): Beta(400, 9600)  ──► Draw ──►  θ_A = 0.041
Variant B (Wide):   Beta(4, 96)    ──► Draw ──►  θ_B = 0.052  (Wins traffic! Explore)
```

---

## Why Should a Data Analyst Care?

Because Thompson Sampling is the state-of-the-art algorithm for reinforcement learning and personalization engines. It is used by Netflix to auto-select movie artwork for individual users, and by Spotify to recommend songs. Understanding it completes your transition from classical experimenter to AI engineer.

---

## When to Use It

- **Dynamic personalization** — selecting content, layout, or artwork in real-time
- **Ad networks** — maximizing click-through rates across campaigns
- **E-commerce checkout optimizations** — routing traffic dynamically during high-stakes sales events

---

## Common Beginner Mistake

Forgetting to reset or adjust posteriors when product features change. If you update the landing page design, the historical parameters are no longer valid. The bandit will continue to exploit the old winner because its posterior is highly certain. You must reset the beta shape parameters (e.g. back to `Beta(1, 1)`) to trigger a new exploration phase.

---

## Real-World Example

An online store tests three email subject lines using Thompson Sampling:
- **Prior:** `Beta(1, 1)` for all three.

**Process:**
- **Day 1:** Traffic is split roughly 33/33/33 because all distributions are wide (pure exploration).
- **Day 3:** Subject Line B has 50 clicks in 500 emails (10% CTR). Subject Line C has 10 clicks in 500 emails (2% CTR).
- **Day 4:** Subject Line B's posterior is shifted higher and is narrower. In the Thompson Sampling loops, B wins the draw 90% of the time. The algorithm routes 90% of emails to B, 8% to A, and 2% to C.
- **Outcome:** The campaign maximizes clicks automatically, saving the marketing team from manual adjustment.

---

## 🔑 Key Takeaway

> Thompson Sampling routes traffic dynamically by drawing random samples from each variant's posterior distribution. It matches allocation to the probability of success, providing a self-correcting balance between exploration and exploitation.

---

[← Day 136: Multi-Armed Bandits for Online Learning](day-136-multi-armed-bandits.md) · [Next: Day 138 – Peeking in Bayesian A/B Tests →](day-138-peeking-in-bayesian-ab.md)
