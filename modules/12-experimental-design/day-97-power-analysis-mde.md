# Day 97: Power Analysis & Minimum Detectable Effect (MDE)

*Power analysis is your statistical flashlight. It tells you if you're searching in a dark room with a candle or a searchlight.*

---

## Learning Objective

Understand the concept of Minimum Detectable Effect (MDE), perform retrospective and prospective power analyses, and balance business tradeoffs between sample size and experiment sensitivity.

---

## The Problem This Solves

You launch an A/B test. After 3 days, conversions in Treatment look slightly higher. The product manager asks: *"Can we stop the test and declare a winner now?"*

If you don't understand power and MDE, you might look at a "significant" p-value and say yes. But stopping early on low-power tests leads to massive false positive rates (peeking bias). Power analysis tells you whether you've collected enough data to trust the result.

---

## The Concept

### What is Minimum Detectable Effect (MDE)?

The **MDE** is the smallest difference between Treatment and Control that your experiment is mathematically equipped to detect at a given significance level (α) and power (1 - β).

- **High sample size** → Low MDE (high sensitivity to tiny changes)
- **Low sample size** → High MDE (can only detect massive changes)

### Prospective vs. Retrospective Power Analysis

| Dimension | Prospective Power Analysis | Retrospective Power Analysis |
|-----------|----------------------------|------------------------------|
| **When is it run?** | **Before** the experiment starts | **After** the experiment completes |
| **Question it answers** | "How many users do we need to detect our MDE?" | "Given our sample size, did we have enough power to trust this negative result?" |
| **Role in decisions** | Determines budget and duration | Prevents false negative conclusions |

### The Tradeoff Matrix

```
       Sensitivity (Lower MDE)  ◄────────►  Speed (Smaller Sample)
                 │                                    │
  Pro: Detects small conversion shifts    Pro: Runs quickly (days, not weeks)
  Con: Requires massive traffic/time       Con: Misses small but profitable lifts
```

---

## Why Should a Data Analyst Care?

Because product leaders face constant pressure to move fast. They will push to stop tests early. You must use power calculations to explain the risk: *"If we stop the test now, we have a 60% chance of missing a real 2% improvement, and our false positive rate will balloon."* Power analysis gives you the mathematical authority to say "keep the test running."

---

## Common Beginner Mistake

Confusing "no statistical significance" with "the change has no effect." If a test has only 20% power to detect a 2% lift, getting p = 0.35 does **not** mean the lift is zero. It means your sample size was too small to distinguish a 2% lift from random noise. This is a false negative (Type II error).

---

## Real-World Example

A subscription business runs an A/B test on pricing pages with 10,000 visitors per group:
- **Baseline (Control):** 3.0% conversion
- **Test Result:** 3.4% conversion (Treatment)
- **Difference:** +0.4% absolute lift (p = 0.12)

**The Naive Conclusion:** *"p > 0.05, the new design is not a winner. Stick with the old page."*

**The Power Analysis:**
- With 10,000 visitors per group and a 3% baseline, the **MDE at 80% power was 0.68%**.
- The experiment was only powered to detect conversions of 3.68% or higher.
- A 0.4% lift (which represents a 13.3% relative lift — massive for business!) had only ~38% power.

**Correct Action:** Do not reject the new page. The study was underpowered. Extend the experiment to 30,000 visitors per group to reduce the MDE to 0.4%, allowing a reliable decision.

---

## 🔑 Key Takeaway

> Power analysis and MDE define the resolution of your experiment. If you don't calculate your MDE, you will routinely throw away highly profitable features because your statistical tool wasn't sensitive enough to see them.

---

[← Day 96: Sample Size Planning](day-96-sample-size-planning.md) · [Next: Day 98 – Multiple Testing Problem →](day-98-multiple-testing.md)
