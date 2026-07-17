# Day 149: Case Study — Customer Experience Index

*How to use PCA and Factor Analysis to compress 15 survey questions into a single, reliable metric that executives can act on.*

---

## Learning Objective

Integrate PCA, eigenvalue selection, and exploratory factor analysis to build a single Customer Experience Index (CXI) from a multi-question satisfaction survey.

---

## The Business Challenge

A retail brand collects feedback via a 15-question guest survey. The CEO is frustrated by the weekly reports: *"I cannot look at 15 different satisfaction percentages every Monday. Tell me our overall customer experience score, and show me what drives it."*

You are the Lead Analyst. Your task is to collapse these 15 questions into a single, statistically sound **Customer Experience Index (CXI)** and identify the core dimensions of customer satisfaction.

---

## The Analysis Pipeline

### Step 1: Data Preparation & Correlation Check

You analyze 1,000 survey responses.
- **Standardization:** Scale the 15 questions (1-5 Likert scale) to z-scores.
- **Correlation Matrix:** You check the matrix (Bartlett's test of sphericity, p < 0.001; KMO = 0.88), indicating the variables share high correlation, making them excellent candidates for dimension reduction.

### Step 2: Dimension Reduction via PCA (Day 143)

You run PCA on the 15 questions to determine the dimensionality:

- **Kaiser Criterion:** 3 components have eigenvalues > 1.0.
  - PC1: Eigenvalue = 5.82 (38.8% variance)
  - PC2: Eigenvalue = 2.45 (16.3% variance)
  - PC3: Eigenvalue = 1.22 (8.1% variance)
- **Scree Plot:** Shows a clear elbow after component 3.
- **Cumulative Variance:** Retaining 3 components explains **63.2%** of the total variance in the 15 survey questions.

**Decision:** Retain 3 components.

### Step 3: Latent Structure via Exploratory Factor Analysis (Day 145)

To identify the unobserved concepts driving these answers, you run EFA (with varimax rotation) to extract 3 factors:

**Rotated Factor Loading Matrix:**

| Survey Question | Factor 1 (Cleanliness) | Factor 2 (Service) | Factor 3 (Value) |
|-----------------|-------------------------|--------------------|------------------|
| Q1: Floor cleanliness | **0.82** | 0.12 | 0.05 |
| Q2: Bathroom check | **0.80** | 0.10 | 0.08 |
| Q3: Staff friendliness| 0.15 | **0.78** | 0.12 |
| Q4: Speed of checkout | 0.10 | **0.75** | 0.18 |
| Q5: Price fairness | 0.05 | 0.14 | **0.84** |
| Q6: Promotions value  | 0.08 | 0.11 | **0.80** |
| (remaining 9 questions load similarly...) | ... | ... | ... |

**Name the Latent Factors:**
- **Factor 1:** "Physical Environment / Cleanliness"
- **Factor 2:** "Staff Service Quality"
- **Factor 3:** "Perceived Price Value"

### Step 4: Constructing the Index (CXI)

To build the single index requested by the CEO, you calculate a weighted average of the factor scores based on their variance explained:

```
CXI = (38.8 * F_Cleanliness + 16.3 * F_Service + 8.1 * F_Value) / 63.2
```

This index compresses the 15 raw questions into a single score bounded between 0 and 100.

---

## Executive Presentation (Day 117)

You present the proposal to the CEO:

- **The New Metric:** We created a single **Customer Experience Index (CXI)** that summarizes all 15 survey questions, capturing 63% of the total survey information.
- **The Core Dimensions:** Our customer experience is driven by three distinct pillars:
  1. **Cleanliness** (accounts for 61% of CXI score)
  2. **Staff Service** (accounts for 26%)
  3. **Price Value** (accounts for 13%)
- **Strategic Recommendation:** Cleanliness is the primary driver of our overall score. Mid-year drops in CXI were caused by bathroom cleanliness complaints, not pricing. Allocate budget to floor staffing rather than promo discounts.

---

## 🔑 Key Takeaway

> Senior analysts do not present raw survey percentages. By using PCA to determine dimensionality and Factor Analysis to isolate latent variables, you compress multi-variable feedback into a single, nameable executive index.

---

[← Day 148: Canonical Correlation Analysis (CCA)](day-148-canonical-correlation.md) · [Next: Day 150 – Module Recap →](day-150-multivariate-recap.md)
