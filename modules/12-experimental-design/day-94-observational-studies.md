# Day 94: Observational Studies

*Sometimes you cannot experiment. That doesn't mean you can't be rigorous.*

---

## Learning Objective

Understand when observational studies must be used instead of experiments, and learn three natural experiment methodologies: Difference-in-Differences, Regression Discontinuity, and Instrumental Variables.

---

## The Problem This Solves

You want to measure the impact of a price change or a state-level policy. You cannot run a randomized A/B test because you cannot charge two different prices to the same demographic without public backlash, or randomly assign people to states. You must use historical data where the business or nature made the changes for you.

---

## The Concept

An **observational study** is an analysis where the investigator does not control the assignment of treatment (no random assignment). 

Because confounders exist, we look for **natural experiments** where outside forces mimic random assignment:

### 1. Difference-in-Differences (DiD)

Compares the change over time in a treatment group to the change over time in a control group.

```
Outcome
  │                Treatment Post (Actual) ────●
  │               ╱                           
  │              ╱  Difference-                 
  │             ╱   in-Differences              
  │            ╱                                
  │  Control  ●────────────────────────────────● Control Post
  │   Pre    ╱                                  
  │         ╱ ─────────────────────────────────● Counterfactual
  │        ╱  Parallel Trends Assumption       (If treatment had no effect)
  │  Treat●
  │   Pre
  └───────────────────────────────────────────────
               Pre                          Post
```

- **Core Assumption:** **Parallel Trends** — Treatment and control groups would have followed the same trend in the absence of treatment.
- **Formula:** `DiD = (Treat_Post - Treat_Pre) - (Control_Post - Control_Pre)`

### 2. Regression Discontinuity Design (RDD)

Exploits arbitrary thresholds (e.g., credit score > 680 gets loan approval, age >= 21).

- **Core Idea:** People just below the threshold (679) are statistically identical to those just above it (681). Any difference in their outcomes can be attributed to the treatment (getting the loan).

### 3. Instrumental Variables (IV)

Uses a variable (the "instrument") that affects treatment assignment but has no direct effect on the outcome except through the treatment.

---

## Why Should a Data Analyst Care?

Because RCTs are expensive, slow, and sometimes unethical or illegal. If you only know how to analyze A/B tests, you cannot support long-term strategic decisions like mergers, retail expansion, pricing models, or policy shifts.

---

## Common Beginner Mistake

Assuming a simple pre/post comparison proves impact. "We launched the feature in UK, and sales rose 10% next month." Did sales rise because of your feature, or because of a holiday season? Without a parallel control group (e.g., France, where the feature didn't launch), pre/post comparisons are highly biased.

---

## Real-World Example

A restaurant chain tests a new digital kiosk in London. They use Manchester as a control group:

| City | Pre-Launch Revenue | Post-Launch Revenue | Revenue Change |
|------|--------------------|---------------------|----------------|
| London (Treatment) | £150,000 | £175,000 | +£25,000 |
| Manchester (Control) | £120,000 | £130,000 | +£10,000 |

**DiD Calculation:**
- `DiD = (175,000 - 150,000) - (130,000 - 120,000)`
- `DiD = 25,000 - 10,000 = £15,000`

**Business Interpretation:** While London's revenue grew by £25,000, we estimate £10,000 of that was due to macro-market trends (seen in Manchester). The true causal lift of the digital kiosk was £15,000.

---

## 🔑 Key Takeaway

> When randomized experiments are impossible, look for natural experiments. Difference-in-Differences and Regression Discontinuity filter out background trends and local confounding, allowing causal estimates from observational data.

---

[← Day 93: Randomized Controlled Experiments](day-93-randomized-experiments.md) · [Next: Day 95 – A/B Testing Design →](day-95-ab-testing-design.md)
