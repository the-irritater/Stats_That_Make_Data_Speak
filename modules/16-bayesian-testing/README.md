# Module 16: Bayesian A/B Testing & Decision Making

*Traditional A/B testing forces you to make decisions based on p-values and sample sizes. Bayesian A/B testing allows you to ask: "What is the probability that Variant B is better, and how much money do we risk losing if we choose it?"*

---

## Before You Begin

Before starting this module, you should have a solid understanding of:
- **Experimental Design (Module 12):** Randomization, A/B testing, metrics, and power.
- **Bayesian Fundamentals (Module 15):** Prior, likelihood, posterior, and Beta-Binomial updates.

---

## Why It Matters

In business experimentation, decisions must be made quickly. Frequentist A/B testing is rigid—it suffers from peeking bias, requires fixed sample sizes, and outputs abstract p-values that executives struggle to interpret. Bayesian experimentation framework allows continuous monitoring, direct probability statements (e.g., "94% chance Variant B is best"), and calculates the exact financial risk (Expected Loss) of any rollout decision.

---

## Learning Path

| Day | Topic | Key Question |
|-----|-------|-------------|
| 131 | [Why Frequentist A/B Testing Fails in Business](day-131-why-frequentist-ab-fails.md) | Why do p-values, sample size limits, and peeking bias slow down product changes? |
| 132 | [The Bayesian A/B Testing Framework](day-132-bayesian-ab-framework.md) | How do we frame comparisons with posterior distributions? |
| 133 | [Probability of Being Best](day-133-probability-of-being-best.md) | How do we calculate the direct probability that Variant B beats Control? |
| 134 | [Expected Loss & Risk Metrics](day-134-expected-loss.md) | How do we quantify the revenue we risk losing by rolling out Variant B? |
| 135 | [Bayesian Decision Theory](day-135-bayesian-decision-theory.md) | How do we use utility functions to make decisions under uncertainty? |
| 136 | [Multi-Armed Bandits for Online Learning](day-136-multi-armed-bandits.md) | How do we dynamically route traffic to maximize revenue during a test? |
| 137 | [Thompson Sampling](day-137-thompson-sampling.md) | How does probability matching balance exploration and exploitation? |
| 138 | [Peeking in Bayesian A/B Tests](day-138-peeking-in-bayesian-ab.md) | Why is continuous monitoring statistically safe under a Bayesian model? |
| 139 | [Case Study: E-commerce Bayesian A/B Test](day-139-bayesian-ab-case-study.md) | How do we run, analyze, and make decisions on a real conversion experiment? |
| 140 | [Module Recap](day-140-bayesian-ab-recap.md) | What is our unified Bayesian experimentation framework? |

---

[← Module 15: Bayesian Statistics Fundamentals](../15-bayesian-fundamentals/) · [Next: Module 17 – Multivariate Statistics & Dimensionality →](../17-multivariate-stats/)
