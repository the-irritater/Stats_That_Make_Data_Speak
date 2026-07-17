# Day 95: A/B Testing Design

*A bad design with good statistics is just a rigorous way of finding the wrong answer.*

---

## Learning Objective

Design a business A/B test from scratch, define units of randomization, choose appropriate primary and guardrail metrics, and prevent user-level contamination.

---

## The Problem This Solves

You want to test a new checkout flow. You assign the treatment based on session ID. A user visits on their phone (assigned to Treatment), gets confused, switches to their desktop (assigned to Control), and completes the purchase. 

Your data shows one treatment visit without conversion and one control visit with conversion. The design introduced **contamination (spillover)**, bias, and invalid conclusions.

---

## The Concept

### The 4 Pillars of Experiment Design

```
   1. Randomization Unit (Who gets split?)
               ↓
   2. Target Population (Who is in the test?)
               ↓
   3. Metric Selection (What do we measure?)
               ↓
   4. Allocation Split (How do we divide them?)
```

### 1. The Randomization Unit

The entity assigned to treatment or control.

| Unit | Best For | Risk |
|------|----------|------|
| **User ID (Logged-in)** | Default choice for UX testing | Doesn't track logged-out users |
| **Cookie/Device ID** | Logged-out pages (landing, marketing) | Users clearing cookies, multi-device usage |
| **Session ID** | High-traffic, transactional pages | Contamination across sessions |
| **Cluster/Geography** | Network-effect products (Uber, social networks) | Low sample size, high variance |

### 2. Metric Design

Never evaluate an A/B test on a single metric. Design a scorecard:

- **Primary Metric:** The key driver of the test (e.g., Conversion Rate). Highly sensitive to the change.
- **Secondary Metrics:** Diagnostic metrics explaining *why* the primary changed (e.g., Add-to-cart rate, page load speed).
- **Guardrail Metrics:** Critical business metrics that must *not* be harmed (e.g., Unsubscribe rate, customer support tickets, page latency).

### 3. Avoiding Spillover (Contamination)

Spillover occurs when the behavior of the control group is affected by the treatment.
*Example:* In a two-sided marketplace (e.g., ride-sharing), if you offer bonuses to treatment drivers, they accept more rides, leaving fewer rides for control drivers. This artificially deflates the control group's performance.
*Solution:* Randomize by city (cluster randomization) rather than individual driver.

---

## Why Should a Data Analyst Care?

Because you are the gatekeeper of scientific rigor. Product managers want to launch experiments quickly. If you don't enforce correct randomization units and guardrails, the business will launch changes that lose money while reporting "statistically significant" wins.

---

## Common Beginner Mistake

Changing the allocation split mid-experiment. Starting a test at 10% treatment / 90% control, then shifting it to 50/50 after three days. This mixes cohorts and introduces massive bias because the users assigned in the first three days are systematically different from those assigned later. If you change allocation, you must reset the experiment.

---

## Real-World Example

A SaaS company designs an A/B test for a new checkout page:

- **Unit:** Logged-in User ID (keeps experience consistent across devices).
- **Population:** New signups on paid tiers only (excluding free trial users).
- **Primary Metric:** Conversion from signup to paid subscription (within 14 days).
- **Guardrail Metric:** Refund requests within 30 days (ensures we aren't tricking users into buying).
- **Target Lift:** 2% absolute conversion lift.

**Why this works:** Randomizing by user ID prevents multi-device contamination. The guardrail metric prevents short-term conversion optimization at the expense of long-term retention.

---

## 🔑 Key Takeaway

> Experiment design is about control. Choose the randomization unit that prevents user contamination, and always include business guardrails so you don't optimize one metric while destroying another.

---

[← Day 94: Observational Studies](day-94-observational-studies.md) · [Next: Day 96 – Sample Size Planning →](day-96-sample-size-planning.md)
