# Day 91: Correlation vs Causation

*Ice cream sales and drowning rates are highly correlated. But stopping the ice cream truck won't save lives.*

---

## Learning Objective

Understand the structural difference between correlation and causation, learn the concepts of joint probability distribution and directed acyclic graphs (DAGs), and identify why association does not imply causation in business data.

---

## The Problem This Solves

You see that customers who use a search bar on an e-commerce store purchase 3× more than those who don't. You conclude that the search bar causes high spend, so you spend $50,000 redesigning it. Spend doesn't change. 

Why? Because the search bar usage was correlated with intent, not the cause of spend. Understanding this distinction prevents massive misallocations of capital.

---

## The Concept

### The Definitions

- **Correlation (Association):** A statistical relationship where two variables change together. Knowing the value of X tells you something about the probability of Y: `P(Y | X) ≠ P(Y)`.
- **Causation:** A physical or structural mechanism where changing the value of X directly changes the value of Y. 

In causal terms, we write this using the **do-calculus** notation:
`P(Y | do(X = x))` represents the distribution of Y when we *force* X to take the value x, overriding its natural causes.

### Directed Acyclic Graphs (DAGs)

We model causal structures using nodes (variables) and directed arrows (causal effects):

```
Common Cause (Confounder):
     [ Temperature ]
       ╱         ╲
      ▼           ▼
[ Ice Cream ]   [ Drowning ]
```
Because Temperature influences both, Ice Cream and Drowning are correlated: `P(Drowning | Ice Cream) > P(Drowning)`.
However, forcing someone to eat ice cream does not make them drown: `P(Drowning | do(Ice Cream)) = P(Drowning)`.

---

## Why Should a Data Analyst Care?

Because businesses run on interventions. When a manager asks: "What will happen if we change the price?", they are asking a causal question (`do(Price)`). If you analyze historical correlation without causal thinking, you will give predictions that break the moment the business changes its strategy.

---

## Common Beginner Mistake

Confusing timeline sequence with causality (the *post hoc ergo propter hoc* fallacy). "We changed our email subject line on Tuesday, and conversions went up on Wednesday, so the subject line caused the lift." 

Without accounting for external factors (payday cycles, competitor outages, day-of-week effects), this conclusion is statistically indefensible.

---

## Real-World Example

A subscription service notices that users who set up "auto-renewal" have a 45% higher retention rate than those who pay manually. 

- **The Naive Action:** Force all users to opt into auto-renewal, expecting a 45% lift in retention.
- **The Causal Reality:** Users who choose auto-renewal are highly committed to the product. Forcing casual users onto auto-renewal leads to billing complaints and cancellations, not retention. Auto-renewal choice is a *signal* of loyalty, not its root *cause*.

---

## 🔑 Key Takeaway

> Correlation lets you predict outcomes in an unchanged system. Causation lets you predict what happens when you intervene to change the system. Never recommend an action based purely on association.

---

[← Module 12 README](README.md) · [Next: Day 92 – Confounding Variables →](day-92-confounding-variables.md)
