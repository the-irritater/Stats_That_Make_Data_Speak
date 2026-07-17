# Day 70: Module Recap + Decision Framework

*10 days. One framework: choose the right test, interpret it honestly, and make the decision.*

---

## Learning Objective

Consolidate everything from Module 9 into a decision framework you can use on any comparison problem, and understand how these tools connect to what comes next.

---

## What We Covered (Day 61–70)

| Day | Topic | Core Insight |
|-----|-------|-------------|
| 61 | Why Compare Groups? | Every business decision is a comparison |
| 62 | Independent t-Test | Compare means of two unrelated groups |
| 63 | Paired t-Test | Compare before vs after on the same subjects |
| 64 | One-Way ANOVA | Compare means across 3+ groups |
| 65 | Two-Way ANOVA | Test two factors and their interaction |
| 66 | Post-Hoc Tests | Identify which specific groups differ |
| 67 | Chi-Square Test | Test association between categorical variables |
| 68 | Effect Size & Power | Measure magnitude and study adequacy |
| 69 | Business Case Study | All tools applied to one real problem |

---

## The Decision Framework

Use this every time someone asks "Is there a difference?"

```
START: What type of outcome variable?
│
├── CONTINUOUS (revenue, score, time)
│   │
│   ├── How many groups?
│   │   ├── 2 groups
│   │   │   ├── Same subjects? → Paired t-Test (Day 63)
│   │   │   └── Different subjects? → Independent t-Test (Day 62)
│   │   │
│   │   └── 3+ groups
│   │       ├── One factor? → One-Way ANOVA (Day 64)
│   │       │   └── Significant? → Post-Hoc Tests (Day 66)
│   │       └── Two factors? → Two-Way ANOVA (Day 65)
│   │           └── Check interaction first
│   │
│   └── ALWAYS REPORT: p-value + CI + effect size (d or η²)
│
└── CATEGORICAL (yes/no, category A/B/C)
    │
    └── Two categorical variables
        └── Chi-Square Test (Day 67)
            └── ALWAYS REPORT: p-value + Cramér's V

BEFORE any test: Power Analysis (Day 68)
  └── Do you have enough data to detect the expected effect?

AFTER any test: Ask three questions
  1. Is it statistically significant? (p-value)
  2. Is it practically meaningful? (effect size)
  3. Was the study adequately powered? (power)
```

---

## The Five Reporting Rules

Every statistical comparison you present should follow these rules:

1. **State the test used and why** — "We used a Welch's t-test because the outcome is continuous and we're comparing two independent groups."

2. **Report the test statistic, df, and p-value** — "t(578) = -7.12, p < 0.001"

3. **Report the effect size** — "Cohen's d = 0.59, medium effect"

4. **Report the confidence interval** — "95% CI: [-10.98, -6.22]"

5. **Translate to business language** — "Premium customers are 6–11 points more satisfied than Basic customers. This difference is real and large enough to matter."

---

## How Module 9 Connects to What's Next

| This Module (Decision Making) | Next Module (Predictive Statistics) |
|------------------------------|-----------------------------------|
| "Are groups different?" | "Can we predict the outcome?" |
| t-tests compare group means | Regression models those means as a function of inputs |
| ANOVA tests factors | Regression includes factors as predictor variables |
| Chi-Square tests associations | Logistic regression predicts categorical outcomes |
| Effect size measures magnitude | R² measures explained variance |

Module 9 asked: *"Is there a difference?"*
Module 10 asks: *"How much of the outcome can we explain — and predict?"*

---

## 🔑 Key Takeaway

> Statistical decision making is a framework, not a formula. Choose the right test based on your data types and groups. Report the p-value, effect size, and confidence interval together. Translate the statistics into a business recommendation. That's what makes data speak.

---

[← Day 69: Business Case Study](day-69-business-case-study.md) · [Back to Module 9](README.md)
