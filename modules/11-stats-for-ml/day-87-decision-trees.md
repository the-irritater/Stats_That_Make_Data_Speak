# Day 87: Decision Trees

*A decision tree makes predictions the way a human makes decisions — by asking a series of yes/no questions.*

---

## Learning Objective

Understand how decision trees work, why they're so interpretable, learn the key concepts of splitting and pruning, and know their strengths and limitations compared to regression.

---

## The Problem This Solves

Linear regression assumes a straight-line relationship. But what if the pattern is: "customers under 30 who spend more than $50 are very likely to churn, but customers over 30 with the same spend are not"? Decision trees capture these non-linear, conditional patterns naturally — without requiring you to specify interaction terms in advance.

---

## The Concept

### How a Decision Tree Works

The tree splits data into increasingly specific groups based on feature thresholds:

```
                    [All Customers]
                    Avg Churn: 25%
                         │
              Monthly Charges > $65?
                    ╱            ╲
                 Yes              No
          [High Charges]     [Low Charges]
          Churn: 42%         Churn: 12%
               │                  │
        Contract < 12mo?    Support Tickets > 3?
          ╱        ╲          ╱         ╲
        Yes        No       Yes         No
     Churn: 68%  Churn: 24%  Churn: 28%  Churn: 5%
```

### Key Concepts

| Concept | What It Means |
|---------|--------------|
| **Root node** | The top split — the most informative feature |
| **Internal nodes** | Decision points (feature thresholds) |
| **Leaf nodes** | Final predictions (the bottom of each branch) |
| **Depth** | Number of levels from root to deepest leaf |
| **Splitting criterion** | How the algorithm chooses the best split |

### How Splits Are Chosen

The tree selects the feature and threshold that best separates the target variable:

| Criterion | Used For | What It Measures |
|-----------|----------|-----------------|
| **Gini Impurity** | Classification | How mixed the classes are in a node |
| **Entropy / Information Gain** | Classification | Reduction in uncertainty after splitting |
| **MSE (Mean Squared Error)** | Regression | Reduction in variance after splitting |

Lower impurity = purer groups = better split.

### Decision Trees vs Regression

| Aspect | Linear Regression | Decision Tree |
|--------|------------------|---------------|
| **Relationship** | Linear only | Any shape (non-linear, conditional) |
| **Interactions** | Must specify manually | Discovered automatically |
| **Interpretability** | Coefficients | Visual tree structure |
| **Extrapolation** | Can predict beyond data range | Cannot — bounded by training range |
| **Stability** | Stable | Sensitive to small data changes |
| **Feature scaling** | Required for regularization | Not needed |

### Overfitting and Pruning

Deep trees memorize training data. Control this with:

| Technique | What It Does |
|-----------|-------------|
| **Max depth** | Limit how deep the tree grows |
| **Min samples per leaf** | Require minimum observations at each endpoint |
| **Min samples to split** | Require minimum observations to create a new branch |
| **Cost-complexity pruning** | Remove branches that don't improve test performance |

---

## Why Should a Data Analyst Care?

Because decision trees are the most interpretable ML model. You can show a tree to a non-technical stakeholder and they'll understand it instantly: "If charges are above $65 and contract is under 12 months, churn risk is 68%." That interpretability is invaluable for business buy-in. They're also the building block for Random Forests (Day 88).

---

## Common Beginner Mistake

Growing a deep tree and reporting training accuracy. A tree with enough depth will achieve 100% training accuracy by memorizing every data point — but it won't generalize. Always limit depth and validate on test data. Also: using decision trees when relationships are truly linear — regression will be more accurate and stable.

---

## Real-World Example

A bank builds a loan approval decision tree:

```
                [All Applications]
                Approval Rate: 65%
                       │
              Credit Score > 680?
                  ╱          ╲
               Yes            No
          Approved: 88%   Approved: 31%
               │                │
        DTI Ratio < 35%?   Employment > 2yr?
          ╱       ╲          ╱        ╲
        Yes       No       Yes        No
    Approve: 94%  72%     45%      Deny: 92%
```

**Business insight:** Credit score is the strongest predictor (root split). Among low-credit applicants, employment stability is the deciding factor. This tree is transparent enough for regulatory review.

---

## 🔑 Key Takeaway

> Decision trees make predictions by asking a sequence of questions about your features. They're intuitive, handle non-linear patterns naturally, and are easy to explain. But they overfit easily — which is why we combine many trees into forests (tomorrow).

---

[← Day 86: Feature Engineering](day-86-feature-engineering.md) · [Next: Day 88 – Random Forests →](day-88-random-forests.md)
