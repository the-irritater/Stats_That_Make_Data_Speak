# Day 136: Multi-Armed Bandits for Online Learning

*An A/B test is like taking half your traffic and sending them to a broken page for weeks. A bandit algorithm is like slowly rerouting traffic away from the loser as soon as it starts to fail.*

---

## Learning Objective

Understand the Multi-Armed Bandit (MAB) framework as an alternative to static A/B testing, explain the exploration vs. exploitation dilemma, and identify business scenarios where bandits are superior to standard experiments.

---

## The Problem This Solves

You run a holiday sales campaign comparing 3 banner ads. Ad A converts at 5%, Ad B at 8%, and Ad C at 2%. 
- **Under standard A/B testing:** You allocate 33.3% of traffic to each banner and keep the test running for 2 weeks to hit sample size goals. For 14 days, you waste 33% of your traffic on the terrible Ad C, costing the business thousands of dollars in lost revenue.
- **Under a bandit framework:** The algorithm dynamically routes traffic away from Ad C and toward Ad B in real-time, preserving sales during the experiment.

---

## The Concept

### The Multi-Armed Bandit Analogy

The name comes from a slot machine (a "one-armed bandit"). Imagine standing in front of `K` slot machines, each with a different, unknown payout probability. How do you pull the levers to maximize your total winnings?

```
               [ User Traffic arrives ]
                          │
             Multi-Armed Bandit Algorithm
             (Exploration vs. Exploitation)
             ╱            │             ╲
            ▼             ▼              ▼
       [ Lever A ]   [ Lever B ]    [ Lever C ]
         (10% traffic) (80% traffic)  (10% traffic)
```

### The Exploration vs. Exploitation Dilemma

Every decision step forces a choice:

- **Exploration:** Allocate traffic to lesser-known variants to collect information (learn which machine is best).
- **Exploitation:** Allocate traffic to the current leader to maximize conversions (cash in on current knowledge).

### Bandits vs. A/B Testing

| Dimension | Standard A/B Testing | Multi-Armed Bandits |
|-----------|----------------------|---------------------|
| **Goal** | Find statistical significance / learn parameters | Maximize total revenue/conversions during test |
| **Allocation** | Static (e.g. 50/50 split throughout) | Dynamic (shifts toward the leader in real-time) |
| **Duration** | Fixed (calculated in advance) | Continuous / Online learning |
| **Opportunity Cost** | High (sends traffic to losers) | Low (automatically limits exposure to losers) |
| **Best For** | Strategic choices (pricing, checkout flows) | Short-lived campaigns (news headlines, holiday ads) |

---

## Why Should a Data Analyst Care?

Because optimizing traffic allocation is a core analytics task. If you suggest a static 2-week A/B test for a high-traffic, time-sensitive event (like a Black Friday homepage banner), the marketing director will reject it due to the opportunity cost. Suggesting a bandit algorithm achieves optimization and learning simultaneously.

---

## Common Beginner Mistake

Using bandits for long-term strategic learning. Bandits optimize for conversion, not parameter certainty. If you want to know the *exact* effect size of a feature (e.g. to write a scientific report), a bandit is a bad choice because it quickly stops sending traffic to the losing variant, leaving you with very high uncertainty (wide credible intervals) for that variant.

---

## Real-World Example

A news website tests three headlines for a breaking story:
- **Headline A:** Standard summary.
- **Headline B:** Clickbait angle.
- **Headline C:** Quote-focused.

Because news traffic spikes for only 6 hours, a static A/B test is useless (by the time you confirm a winner, the news cycle is over). 

The site uses a bandit algorithm. Within 30 minutes, the algorithm detects Headline B is generating 3x more clicks than C. By hour 2, the algorithm is routing 90% of traffic to B and only 5% to A and C. The site maximizes page views while the story is hot.

---

## 🔑 Key Takeaway

> Multi-Armed Bandits resolve the exploration-exploitation dilemma by dynamically routing traffic to the leading variant. Use them for short-lived, high-opportunity-cost experiments where maximizing conversion is more important than statistical precision.

---

[← Day 135: Bayesian Decision Theory](day-135-bayesian-decision-theory.md) · [Next: Day 137 – Thompson Sampling →](day-137-thompson-sampling.md)
