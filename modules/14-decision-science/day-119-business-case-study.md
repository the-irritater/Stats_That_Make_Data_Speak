# Day 119: Complete Business Case Study

*One company. One major strategy shift. This is how you integrate SQL, python, experiments, forecasting, and decision science into one executive proposal.*

---

## Learning Objective

Integrate experimental design, cohort retention analysis, forecasting, and data storytelling to construct a unified business growth proposal for steering committees.

---

## The Business Challenge

A SaaS company offers a project management tool. Growth has plateaued.
- **The Product Manager** wants to launch a new collaboration feature.
- **The Marketing Director** wants to run a referral campaign.

You are the Lead Analyst. Your task is to analyze the data, determine where the leverage is, evaluate the experiment, forecast the business impact, and write the executive proposal.

---

## The Analysis Steps

### Step 1: Funnel & Cohort Diagnostic (Decision Science)

You query the historical databases and build a cohort retention matrix:

| Cohort | Size | Month 1 Retention | Month 3 Retention | Month 6 Retention |
|--------|------|-------------------|-------------------|-------------------|
| Q1 Cohort | 5,000 | 45% | 22% | 12% |
| Q2 Cohort | 6,000 | 44% | 21% | 11% |
| Q3 Cohort | 7,500 | 43% | 20% | 10% |

**Diagnostic:** Retention curves are decaying (leaky bucket). The business is growing active users only because Q3 acquisition was high.
**The Verdict:** Do not invest in marketing referral campaigns (breadth). You must fix retention (frequency/depth). The collaboration feature is the right path.

### Step 2: The A/B Test (Experimental Design)

The product team launches the collaboration feature as an A/B test:
- **Baseline Conversion (Control A - standard UI):** Month 1 Retention = 44%
- **Target MDE:** 4% absolute lift
- **Required Sample Size (80% power, α = 0.05):** ~2,400 users per group
- **Duration:** 14 days

**Results after 14 days:**
- **Control (A):** n = 2,450, Month 1 Retention = 43.8%
- **Treatment (B - Collaboration Feature):** n = 2,420, Month 1 Retention = 48.2%
- **Statistical Test (Chi-Square):** χ²(1) = 9.82, **p = 0.002** (Significant ✅)
- **95% Confidence Interval for Lift:** [+1.6%, +7.2%]

**Finding:** The collaboration feature causes a statistically significant 4.4% absolute lift in Month 1 retention.

### Step 3: Business Forecasting (Forecasting)

Using the 4.4% retention lift, you forecast the impact on Active User counts over the next 12 months using a simple trend-projection model:

```
Active Users (12 Months Out)
  ▲
  │                                    ● Treatment (Forecasted: 45,000 users)
  │                                  ╱
  │                                ╱
  │                              ╱
  │  Current (25,000) ●────────● Control (Forecasted: 32,000 users)
  └─────────────────────────────────────►
                         Months
```

- **Control Forecast (current trajectory):** 32,000 Active Users (RMSE: 1,200)
- **Treatment Forecast (with 4.4% retention lift):** 45,000 Active Users (RMSE: 1,800)
- **Difference:** +13,000 active users.

---

## The Executive Proposal (Storytelling)

You compile these steps into a three-slide proposal for the CEO:

### Slide 1: The Opportunity (Why Retention?)
- **The Metric:** Our cohort retention curves are decaying to 10% by Month 6, meaning 90% of acquired users leave the app.
- **The Decision:** Prioritizing user acquisition is unprofitable on these retention rates. We must plug the leak first.

### Slide 2: The Proof (The A/B Test)
- **The Experiment:** We tested a new Collaboration Feature with 4,870 users over 14 days.
- **The Result:** The feature increased Month 1 retention by 4.4% (p = 0.002, 95% CI: 1.6% to 7.2%). This result is highly significant and mathematically sound.

### Slide 3: The Impact (12-Month Forecast)
- **The Forecast:** Implementing the collaboration feature for all users is projected to increase our active user count from 32,000 to 45,000 over the next 12 months (+13,000 users).
- **The Revenue Link:** At our current average customer value ($15/month), this lift represents an **additional $195,000 in monthly recurring revenue (MRR)**.
- **Recommendation:** Roll out the collaboration feature immediately.

---

## 🔑 Key Takeaway

> A senior analyst coordinates different statistical tools into a single narrative: use cohorts to find the problem, experiments to prove the solution, forecasting to calculate the future impact, and clear storytelling to win executive buy-in.

---

[← Day 118: Common Mistakes Analysts Make](day-118-common-analyst-mistakes.md) · [Next: Day 120 – Becoming a Data Professional with Statistics →](day-120-becoming-a-professional.md)
