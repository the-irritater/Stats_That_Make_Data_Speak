# Day 114: Funnel Analysis

*Optimizing a business is about finding where the leaks are. A funnel analysis shows you exactly which step of the customer journey is losing the most users.*

---

## Learning Objective

Design and execute a conversion funnel analysis, calculate step-to-step drop-offs, and prioritize product interventions based on impact potential.

---

## The Problem This Solves

Your e-commerce sales are down. The product team wants to completely redesign the homepage. The engineering team wants to rebuild the checkout API. The marketing team wants to run a new discount. 

Instead of arguing, you run a funnel analysis. You find that homepage traffic and cart-addition rates are stable, but 85% of users drop off between entering shipping info and paying. The checkout page is the problem. You save the company from redesigning a homepage that wasn't broken.

---

## The Concept

### What is a Funnel Analysis?

A funnel analysis tracks the sequence of steps a user takes to complete a goal (conversion), measuring how many users drop out at each step.

### The Conversion Steps

```
  [ Step 1: Homepage Visit ] ──► 10,000 users (100%)
            │
            ▼
  [ Step 2: Product View ]   ──►  4,000 users (40% conversion / 60% drop-off)
            │
            ▼
  [ Step 3: Add to Cart ]    ──►  1,200 users (30% step-to-step / 12% overall)
            │
            ▼
  [ Step 4: Checkout Start ] ──►    600 users (50% step-to-step / 6% overall)
            │
            ▼
  [ Step 5: Purchase ]       ──►    120 users (20% step-to-step / 1.2% overall)
```

### Key Metrics to Calculate

For each step `i` (where step 1 is baseline):

- **Overall Conversion Rate:** `Users_i / Users_1 * 100` (e.g., 1.2% overall purchase rate).
- **Step-to-Step Conversion Rate:** `Users_i / Users_(i-1) * 100` (e.g., 20% checkout-to-purchase rate).
- **Drop-off Rate:** `100 - Step-to-Step Conversion Rate` (e.g., 80% drop-off at checkout).

---

## Why Should a Data Analyst Care?

Because funnels are the core framework for Conversion Rate Optimization (CRO). When product managers want to increase conversion, they need you to identify the biggest bottlenecks. Funnel analysis isolates where the friction is, transforming product decisions from "what should we build?" to "which leak should we patch?"

---

## Common Beginner Mistake

Failing to define a temporal window for the funnel. If a user visits the homepage in January and purchases a product in December, does that count as a conversion? 

Usually, no. You must define a **funnel window** (e.g., "completed all steps within 24 hours of step 1") to ensure you are measuring cohesive user journeys.

---

## Real-World Example

A subscription service reviews its signup funnel:

| Step | Users | Step-to-Step Conv. | Step-to-Step Drop-off |
|------|-------|--------------------|-----------------------|
| 1. Landing Page | 50,000 | 100% | 0% |
| 2. Free Account Create | 15,000 | 30% | 70% |
| 3. Complete Profile | 13,500 | 90% | 10% |
| 4. Subscription Purchase | 675 | 5% | 95% |

**Analysis:**
- The drop-off between Landing Page and Free Account is large (70%), but expected for landing pages.
- The drop-off between Profile and Purchase is massive (95%). Once users complete their profile, they don't buy the paid subscription.
- **The Decision:** Prioritize pricing tier adjustments, paywall visibility, or target email campaigns immediately after profile completion. Do not optimize the profile completion step (it already converts at 90%).

---

## 🔑 Key Takeaway

> Funnel analysis maps the user journey step-by-step. Focus your optimization efforts on the step with the highest relative drop-off (friction) that has a high volume of users passing through.

---

[← Day 113: Cohort Analysis](day-113-cohort-analysis.md) · [Next: Day 115 – Customer Segmentation →](day-115-customer-segmentation.md)
