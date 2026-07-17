# Day 118: Common Mistakes Analysts Make

*Rigorous tools in biased hands are just instruments for confirming pre-existing opinions.*

---

## Learning Objective

Recognize and prevent the four most common cognitive and statistical biases in business analysis: confirmation bias, cherry-picking, survivor bias, and p-hacking.

---

## The Problem This Solves

You are asked to analyze the success of a new product feature. You want it to be a success (you worked on it). You query the database, find 3 metrics that improved, ignore 5 that dropped, run a t-test on the wins, get p = 0.04, and write a slide deck. 

The feature launches, but revenue drops. You fell victim to bias. Recognizing these pitfalls makes your analyses bulletproof.

---

## The Concept

### The Big Four Analytical Biases

| Bias | Definition | Business Example | Prevention |
|------|------------|------------------|------------|
| **Confirmation Bias** | Searching for data that confirms your hypothesis while ignoring data that refutes it. | Looking only at active users to prove an onboarding UI is successful. | Actively look for data that *disproves* your theory. Write down hypotheses before querying. |
| **Cherry-Picking** | Selecting only the sub-segments or metrics that showed positive results. | Reporting a campaign win in "Parisian Android users on Tuesdays" while it lost overall. | Pre-specify primary metrics and subgroups. Adjust for multiple testing (Day 98). |
| **Survivorship Bias** | Analyzing only the subjects that passed a selection process, ignoring those that dropped out. | Surveying current customers to find out why people churn. | Include dropouts and churned users in your sample base. |
| **p-Hacking** | Collecting and testing data until you find a statistically significant result. | Peeking at A/B test results daily and stopping the test the moment p < 0.05. | Lock sample sizes in advance (Day 96). Never stop tests early. |

### The Analyst's Code of Ethics

To remain objective, follow these rules:

1. **State your hypothesis first** — Write down what you expect and how you will measure it before pulling data.
2. **Report the denominator** — Always show how many users/records were excluded from the analysis and why.
3. **Report the losses** — Show negative results next to positive ones. If conversion went up but page load time slowed, show both.
4. **Publish the nulls** — A finding of "no difference" is a highly valuable business insight. It saves the company from launching useless features.

---

## Why Should a Data Analyst Care?

Because your most valuable asset is your integrity. If stakeholders realize that your analyses always confirm whatever the product manager wants to hear, they will treat you as a graphics designer, not a scientist. A rigorous analyst who reports uncomfortable truths objectively builds long-term authority.

---

## Common Beginner Mistake

Assuming "the numbers don't lie." Numbers are silent. Analysts compile them, select them, and interpret them. Every database query involves a series of design choices (which outliers to exclude, how to group dates, which variables to control). If you don't check your own biases, the numbers will say whatever you want them to say.

---

## Real-World Example

A subscription company wants to analyze user satisfaction:
- **The Biased Approach:** Email a survey to all active users who have been with the service for >6 months.
  - *Result:* 92% satisfaction. "We are doing amazing!"
  - *The Catch:* **Survivorship Bias**. You ignored the users who canceled in the first month because they hated the service.
- **The Unbiased Approach:** Email the survey to a random sample of signups from 6 months ago, including those who have since canceled.
  - *Result:* 54% satisfaction, with 40% citing onboarding confusion.
  - *Outcome:* The team redesigns onboarding, doubling retention.

---

## 🔑 Key Takeaway

> Rigor is a moral choice, not just a technical one. Protect your analysis from confirmation bias, survivorship bias, and p-hacking by setting hypotheses in advance, reporting losses alongside wins, and including dropouts in your data pools.

---

[← Day 117: Communicating Statistical Results](day-117-communicating-results.md) · [Next: Day 119 – Complete Business Case Study →](day-119-business-case-study.md)
