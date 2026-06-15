# Executive Summary: End-to-End Customer Analytics

**Date:** June 16, 2026  
**Audience:** Executive Leadership Team  
**Author:** MSc Statistics & Analytics Lead  

---

## 1. Key Business Insights

We conducted a comprehensive end-to-end customer analytics study on e-commerce transactions ($N = 1,000$ customers) to determine how site engagement drives order values, how to categorize our buyers, and whether segment-wide re-engagement strategies are commercially viable.

### 📈 Engagement vs. Order Values (OLS Regression)
- **Variance Explained:** Browsing time and page view density together explain **71.0%** of customer order values ($R^2 = 0.710$), outperforming our baseline model by **44.8%** in predictive accuracy.
- **The Page View Premium:** Controlling for browsing duration, each additional page view predicts an average spend increase of **$3.48** (95% CI: [$2.91$, $4.04$], $p < 0.001$).
- **The Duration Nudge:** Controlling for pages clicked, each extra minute of session duration predicts an average spend increase of **$1.11** (95% CI: [$0.63$, $1.59$], $p < 0.001$).
- **Relative Importance:** Standardized coefficients (Beta weights) indicate that Pages Visited (Beta: 0.620) is a much stronger predictor of purchase size than Session Duration (Beta: 0.234).

### 🏷️ RFM Customer Segmentation (Recency, Frequency, Monetary)
We classified customers into three distinct value segments based on Recency, Frequency, and Monetary scores:
1. **Champions (22.4% of base):** Highly engaged, high-spending frequent buyers. (Average tenure: 11.2 months, Mean lifetime spend: **$671.30**).
2. **Loyal Customers (54.8% of base):** Regular shoppers with moderate lifetime spend. (Average tenure: 11.0 months, Mean lifetime spend: **$245.05**).
3. **At-Risk / Lost (22.8% of base):** Churned or low-value transient shoppers. (Average tenure: 7.9 months, Mean lifetime spend: **$104.70**).

---

## 2. Hypothesis Testing: Segment Retention Associations

We evaluated if segment membership predicts a customer's repeat purchase rate using a Chi-Square Test of Independence.
- **Hypothesis Result:** We failed to reject the null hypothesis ($p = 0.551$, Cramer's V = 0.0345).
- **Interpretation:** There is **no statistically significant difference** in repeat purchase rates among Champions (37.9%), Loyal Customers (40.3%), and At-Risk shoppers (43.0%) in this dataset.

---

## 3. Executive Business Recommendations

Based on our empirical models, we propose three core interventions:

1. **Invest in Site Performance & Page Load Speeds:** Since page views are the single strongest predictor of transaction value (Beta: 0.620) and each extra page view generates an expected **$3.48** in spend, optimizing site navigation and layout to encourage page exploration is our highest ROI initiative. This satisfies our pre-analysis regression rule.
2. **Individualized Loyalty Strategy:** Do not launch segment-wide loyalty campaigns under the assumption that "Champions" have a higher repeat purchase rate than others (the difference is statistically negligible, $p = 0.55$). Re-engagement campaigns should instead be triggered by individualized customer purchase intervals.
3. **Targeted coupon distributions:** Transition away from blanket site-wide promotions (which decrease net profits by 39% due to margin cut) and target coupons strictly at churned, price-sensitive shoppers to win them back.
