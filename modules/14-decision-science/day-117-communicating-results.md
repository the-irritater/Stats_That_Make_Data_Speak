# Day 117: Communicating Statistical Results

*Executives don't think in p-values. They think in ranges, risks, and trade-offs. Translate the statistics into their language.*

---

## Learning Objective

Translate complex statistical results (confidence intervals, p-values, regression coefficients) into clear, non-technical business executive summaries.

---

## The Problem This Solves

You present the results of an A/B test: *"We ran a Welch's t-test on daily conversions. The difference was significant with t(342) = 2.45 and p = 0.012. We reject the null hypothesis."* 

The VP responds: *"So what? What does this mean for our bottom line?"* 

If you cannot translate the statistics, they will ignore your finding. Translating stats ensures your rigor actually guides business strategy.

---

## The Concept

### The Translation Guide

| Statistical Term | Executive Translation | Why It Works |
|------------------|-----------------------|--------------|
| **p < 0.05 (Significant)** | "We are confident this is a real effect, not random variation." | Removes academic jargon while preserving the core meaning of H₀ rejection. |
| **p > 0.05 (Not Significant)**| "We don't have enough evidence to prove this difference is real." | Avoids declaring the lift is "zero" (avoids Type II error overconfidence). |
| **Confidence Interval (95% CI)**| "The most likely range of impact is between X and Y." | Represents uncertainty as a practical business range rather than a point estimate. |
| **Regression Coefficient (β)** | "Each unit increase in X drives an estimated Y change." | Translates slope into a predictive association. |
| **Effect Size (Cohen's d, V)** | "The size of this impact is small/medium/large." | Provides context for whether a significant result is worth operational investment. |

### The Executive Summary Structure (The 3-Sentence Rule)

When reporting a statistical finding, write a three-sentence summary:

1. **What we found:** The business outcome and direction.
2. **The uncertainty range (Confidence Interval):** The plausible scope of impact.
3. **The recommendation (So What?):** The actionable next step.

*Example:* 
"The new signup flow increased registration rates by 2.4% (p = 0.012). The most likely long-term impact is an increase of 1.1% to 3.7% in registrations, which would generate an estimated $12,000 to $40,000 in monthly revenue. We recommend rolling out the new flow to all users."

---

## Why Should a Data Analyst Care?

Because your career growth depends on your communication. Junior analysts write code and dump charts. Senior analysts interpret the numbers, manage uncertainty, and write executive-ready recommendations. Mastering this translation is the fastest way to earn trust with steering committees.

---

## Common Beginner Mistake

Hiding behind statistical terms when you are unsure. Reporting: *"The model has high heteroscedasticity and multicollinearity, with a VIF of 8.2."* 

A business leader hears: *"I don't know if my model works, and I'm using complex words to sound smart."* Instead, say: *"The variables in our model overlap heavily, which makes individual effects unstable. However, the overall prediction remains reliable."*

---

## Real-World Example

An analyst reports the results of a pricing experiment:

- **Technical Draft:** *"We ran a Chi-Square test comparing conversion rates. χ²(1) = 4.22, p = 0.040. The risk ratio is 1.15. We recommend the new price."*
- **Executive Revision:** *"Charging a lower price increased conversion rates by 15% (p = 0.040). The 95% confidence interval suggests a true lift between 2% and 28%. While the lift is statistically significant, the 15% volume increase does not compensate for the lower margin, resulting in a net profit drop of 3%. We recommend rejecting the price cut."*

**Business Impact:** The executive revision saves the company from a margin-collapsing pricing change that the technical draft would have recommended.

---

## 🔑 Key Takeaway

> Executives make decisions based on risk and ranges. Never report a p-value without a confidence interval, and always translate statistical significance into its net financial impact.

---

[← Day 116: Dashboard Storytelling](day-116-dashboard-storytelling.md) · [Next: Day 118 – Common Mistakes Analysts Make →](day-118-common-analyst-mistakes.md)
