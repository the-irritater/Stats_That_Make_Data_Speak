# Day 65: Two-Way ANOVA

*One factor tells you part of the story. Two factors tell you if they interact — and that's where the real insight hides.*

---

## Learning Objective

Understand two-way ANOVA as a method for analyzing two factors simultaneously, learn what interaction effects are, and interpret main effects vs interaction effects in business contexts.

---

## The Problem This Solves

You know that customer satisfaction differs by support channel (Day 64). But does it also depend on the customer's subscription tier? And — critically — does the effect of channel *depend on* the tier? Two-way ANOVA tests two factors and their interaction in a single analysis.

---

## The Concept

### What It Tests

Two-way ANOVA tests three hypotheses simultaneously:

| Hypothesis | Question |
|-----------|----------|
| **Main Effect A** | Does Factor A (e.g., channel) affect the outcome? |
| **Main Effect B** | Does Factor B (e.g., tier) affect the outcome? |
| **Interaction (A × B)** | Does the effect of A depend on B? |

### Main Effects vs Interaction

```
Main Effects Only (No Interaction):     Interaction Present:

Score                                   Score
  │    Premium ────────                   │    Premium ──────╲
  │                                       │                   ╲
  │    Basic ──────────                   │    Basic ──────────╳
  │                                       │
  └──────────────────                     └──────────────────
    Phone    Chat                           Phone    Chat

Lines are parallel → no interaction       Lines cross → interaction!
```

When lines are parallel, each factor has an independent effect. When lines cross (or diverge), the factors interact — the effect of one depends on the level of the other.

### The ANOVA Table

```
Source          | SS    | df  | MS    | F     | p
────────────────┼───────┼─────┼───────┼───────┼──────
Factor A        | SSₐ   | a-1 | MSₐ   | Fₐ    | pₐ
Factor B        | SSᵦ   | b-1 | MSᵦ   | Fᵦ    | pᵦ
Interaction A×B | SSₐᵦ  | (a-1)(b-1) | MSₐᵦ | Fₐᵦ | pₐᵦ
Residual        | SSᵣ   | N-ab| MSᵣ   |       |
────────────────┼───────┼─────┼───────┼───────┼──────
Total           | SSₜ   | N-1 |       |       |
```

### Interpretation Priority

1. **Check the interaction first.** If significant, main effects are misleading on their own.
2. If no interaction → interpret main effects independently.
3. If interaction exists → describe the pattern (e.g., "Chat works better for Premium but not Basic").

---

## Why Should a Data Analyst Care?

Because real business problems have multiple factors. A campaign's effect might depend on the customer segment. A product's rating might depend on both the store and the season. Analyzing one factor at a time misses interactions — and interactions are often the most actionable insights.

---

## When to Use It

- **Two categorical factors**, one continuous outcome
- **You suspect the effect of one factor depends on the other**
- **Factorial experiment designs** — testing combinations of conditions (e.g., pricing × channel)

---

## Common Beginner Mistake

Ignoring a significant interaction and only reporting main effects. If channel and tier interact, saying "Chat is better overall" is misleading — it might only be better for one tier. Always check the interaction term first. If it's significant, break down the analysis by groups.

---

## Real-World Example

A retail company tests two factors on customer satisfaction:
- **Factor A:** Support Channel (Phone, Chat)
- **Factor B:** Subscription Tier (Basic, Premium)

| Channel | Basic (Mean) | Premium (Mean) |
|---------|-------------|---------------|
| Phone | 68 | 75 |
| Chat | 72 | 82 |

**Two-Way ANOVA results:**

| Source | F | p | η² |
|--------|---|---|---|
| Channel | 12.4 | 0.001 | 0.04 |
| Tier | 28.7 | < 0.001 | 0.09 |
| Channel × Tier | 4.8 | 0.029 | 0.02 |

**Business interpretation:** There is a significant interaction (p = 0.029). Chat improves satisfaction more for Premium customers (+10 points) than for Basic customers (+4 points). The recommendation: prioritize chat support for Premium tier, where the impact is greatest.

---

## 🔑 Key Takeaway

> Two-way ANOVA reveals not just *if* factors matter, but *how they combine*. The interaction effect is often the most valuable finding — it tells you where to focus your resources for maximum impact.

---

[← Day 64: One-Way ANOVA](day-64-one-way-anova.md) · [Next: Day 66 – Post-Hoc Tests →](day-66-post-hoc-tests.md)
