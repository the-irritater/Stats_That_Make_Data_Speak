# Day 93: Randomized Controlled Experiments

*Random assignment is the ultimate statistical eraser. It wipes away all confounding variables — seen and unseen.*

---

## Learning Objective

Understand why random assignment is the gold standard of causal inference, explain how it creates identical treatment and control groups, and know the structural elements of a Randomized Controlled Trial (RCT).

---

## The Problem This Solves

You want to measure the effect of a new user onboarding flow. If you let users choose whether to use the new flow, high-intent users will opt in and low-intent users will opt out. Confounding strikes again.

How do you guarantee that the groups you compare are identical in every way except for the onboarding flow? You use random assignment.

---

## The Concept

### The Power of Random Assignment

When you randomly assign participants to either the **Treatment** group (new flow) or **Control** group (old flow), every individual has an equal chance of landing in either group.

```
                  [ Eligible Users ]
                          │
                  Random Assignment
                  (e.g., Coin Flip)
                   ╱             ╲
                  ▼               ▼
            [ Treatment ]     [ Control ]
```

This simple act guarantees that:
- Observable variables (age, device type, country) are distributed equally between groups.
- **Unobservable variables** (intent, mood, tech-savviness) are also distributed equally.

Because the groups are statistically identical, any difference in the outcome (conversion rate) must be caused by the treatment. The back-door path is physically blocked.

### Key Elements of a Controlled Experiment

| Element | Description | Why It Matters |
|---------|-------------|----------------|
| **Unit of Randomization** | What is assigned (user ID, session ID, cookie) | Prevents user contamination across groups |
| **Control Group** | The baseline group receiving the standard experience | Establishes the counterfactual (what would have happened) |
| **Treatment Group** | The group receiving the new experience | Measures the intervention's impact |
| **Blinding** | Users (and ideally analysts) don't know their group | Prevents behavioral changes due to expectations |

---

## Why Should a Data Analyst Care?

Because RCTs (A/B tests) are the most powerful tool in tech and business. Companies like Amazon, Netflix, and Google run thousands of experiments simultaneously. If you want to prove a product change works, you do not write a complex regression model — you launch an A/B test.

---

## Common Beginner Mistake

Confusing **random selection** with **random assignment**:

- **Random Selection:** Drawing a random sample from a population (ensures generalizability).
- **Random Assignment:** Sorting a sample into treatment and control groups (ensures causality).

To prove a treatment causes an effect, you must have random assignment.

---

## Real-World Example

A subscription business tests a new landing page design:

```
Observational Approach (Let users view what they want):
- Self-selected New Page conversion: 14.5%
- Self-selected Old Page conversion: 10.2%
- Result: +4.3% lift (highly confounded by tech-savviness of users clicking new links)

Experimental Approach (Randomly assign at server level):
- Group A (Control - Old Page): 11.2%
- Group B (Treatment - New Page): 11.5%
- Result: +0.3% lift (statistically non-significant)
```

**Business Decision:** Reject the redesign. The apparent 4.3% lift was a selection bias illusion. The true causal lift is near zero.

---

## 🔑 Key Takeaway

> Random assignment balances both seen and unseen confounders across your groups. It makes the treatment the only systematic difference, turning observational associations into robust causal proof.

---

[← Day 92: Confounding Variables](day-92-confounding-variables.md) · [Next: Day 94 – Observational Studies →](day-94-observational-studies.md)
