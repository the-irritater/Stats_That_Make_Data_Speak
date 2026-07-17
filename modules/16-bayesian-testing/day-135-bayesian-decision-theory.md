# Day 135: Bayesian Decision Theory

*Statistics tells you what the data says. Decision theory tells you what to do with it.*

---

## Learning Objective

Understand Bayesian Decision Theory, build utility functions that combine probabilities with financial payoffs, and calculate Expected Utility to make optimal business choices under uncertainty.

---

## The Problem This Solves

An A/B test shows a new feature increases conversion by 0.5% (p = 0.03). However, building and hosting this feature costs $5,000/month. 

Should you launch it? A statistical test only tells you if the 0.5% lift is real. It cannot calculate if the lift covers the $5,000 cost. Bayesian Decision Theory combines the probability distribution of your lift with the financial costs and payoffs to identify the decision that maximizes expected profit.

---

## The Concept

### The Core Elements

Bayesian Decision Theory evaluates choices using three components:

1. **Actions (a):** The decisions you can make (e.g. `a₁` = Launch Feature, `a₀` = Keep Old Feature).
2. **States of Nature (θ):** The true parameter value (e.g., the actual conversion rate lift).
3. **Utility Function U(a, θ):** The payoff (profit or loss) of taking action `a` when the true state is `θ`.

### Calculating Expected Utility

Instead of choosing based on statistical significance, we choose the action that maximizes **Expected Utility**:

```
Expected Utility: E[U(a)] = ∫ U(a, θ) * P(θ | Data) dθ

Estimated via Monte Carlo:
E[U(a)] = (1 / N) * Σ U(a, θ_i)
```

We choose the action `a*` with the highest Expected Utility.

### The Payoff Matrix

Consider a classic launch decision:
- **Cost of launch:** $5,000/month.
- **Payoff of lift:** $10,000 per 1% lift.

| Action (a) | State: Lift is negative (θ < 0%) | State: Lift is positive (θ > 0.5%) |
|------------|---------------------------------|-----------------------------------|
| **a₀: Keep Old** | $0 | $0 (Missed opportunity) |
| **a₁: Launch New**| -$5,000 (Loss) | `$10,000 * Lift - $5,000` (Gain) |

By running your posterior draws `θ_i` through this matrix, you calculate the exact expected value in dollars of launching vs. staying.

---

## Why Should a Data Analyst Care?

Because business executives do not care about statistical outputs; they care about business payoffs. If you present an analysis in terms of expected utility ("Launching this feature has an expected net value of +$12,000/month, accounting for the development cost and the probability range of our lift"), you are acting as a strategic decision scientist.

---

## When to Use It

- **Go/No-Go launch decisions** — when changes have operational costs
- **Pricing tiers** — balancing conversion drops against higher margins
- **Risk management** — evaluating high-cost, high-uncertainty investments

---

## Common Beginner Mistake

Assuming that utility is always linear. For a startup, a 10% chance of losing $1,000,000 might cause bankruptcy, while a 90% chance of making $200,000 is good. The utility of losing $1M is much worse than -10x the utility of making $100K. This is called **risk aversion**. Your utility function should reflect the business's risk tolerance.

---

## Real-World Example

An analyst evaluates a feature launch:
- **Launch Cost:** $2,000 one-time setup.
- **Value of Conversion Lift:** $5,000 per 1% conversion lift.
- **Posterior Lift Distribution (θ):** Mean = 0.5%, 95% Credible Interval: `[-0.2%, 1.2%]`.

**Expected Utility Calculation (Monte Carlo simulation):**
- For each draw `θ_i` of lift, calculate utility: `U(a₁) = $5,000 * θ_i - $2,000`.
- **E[U(a₁)] (Launch):** **+$500** (Positive expected utility).
- **E[U(a₀)] (Don't Launch):** **$0**.

**Decision:** Launch the feature. Even though there is a chance the lift is negative (and we lose the $2,000 setup cost), the probability-weighted expectation is a net gain of $500.

---

## 🔑 Key Takeaway

> Bayesian Decision Theory combines posterior probabilities with financial payoffs. By calculating the Expected Utility of each action, you identify the decision that maximizes expected profit while accounting for uncertainty.

---

[← Day 134: Expected Loss & Risk Metrics](day-134-expected-loss.md) · [Next: Day 136 – Multi-Armed Bandits for Online Learning →](day-136-multi-armed-bandits.md)
