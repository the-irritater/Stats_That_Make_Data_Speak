# Case Study: Restaurant Tipping Behavior (Real-World Dataset)

This case study analyzes tipping patterns in restaurant transactions using the classic **Bryant & Smith (1995)** tips dataset (which is also the default dataset in Seaborn). Unlike synthetic scenarios, this uses real-world customer transactions to demonstrate inference and predictive regression.

---

## 1. Business Questions
- Do tipping rates (percentage of the bill) vary significantly between **Lunch** and **Dinner** periods?
- Can we predict the absolute **tip amount** using `total_bill` and party `size`?
- Are the assumptions of OLS regression satisfied, or does real-world data exhibit heteroscedasticity?

---

## 2. Methodology & Statistical Tools
1. **Exploratory Data Analysis (EDA):** Tipping percentage calculations and grouping by demographic descriptors.
2. **Two-Sample Hypothesis Testing:** A Welch's t-test to check for differences in mean tipping rates between lunch and dinner.
3. **Multiple Linear Regression (OLS):** Fit an ordinary least squares model (`tip ~ total_bill + size`) to quantify how tip amounts scale with bill size and guest count.
4. **Residual Diagnostics:** Plotting residuals vs. fitted values and normal Q-Q plots to verify OLS assumptions.

---

## 3. Key Findings

### Tipping Rate Comparison (T-Test)
- **Lunch Patrons:** Average tipping rate is **16.41%** of the bill ($N = 68$).
- **Dinner Patrons:** Average tipping rate is **15.95%** of the bill ($N = 176$).
- **Statistical Significance:** Welch's t-test yields $p = 0.5145$, meaning we **fail to reject the null hypothesis**. There is no statistically significant difference in tipping percentage rates between lunch and dinner.

### Predictive Modeling (OLS)
- **R-squared ($R^2$):** **46.8%** of the variation in absolute tip amounts is predicted by total bill and party size.
- **Bill size coefficient:** For every $1 increase in the bill size, the tip is expected to increase by **$0.09** (controlling for party size, $p < 0.001$).
- **Party size coefficient:** For every additional customer in the party, the tip is expected to increase by **$0.19** (controlling for bill size, $p = 0.025$).

### OLS Diagnostics
- **Homoscedasticity:** The residuals show a slight "fan" shape at larger bills, representing mild heteroscedasticity. Larger bills show greater variance in customer tipping behavior.
- **Normality:** Q-Q plot reveals minor right skewness, but the residuals do not show severe violations, so the model is acceptable for educational and associative analysis.

---

## 4. How to Run
From the project root, run the Python script to recreate the statistical output and diagnostic plot:
```bash
python3 applied/case-studies/restaurant-tipping-behavior/analysis.py
```
To run the Jupyter Notebook:
```bash
jupyter notebook applied/case-studies/restaurant-tipping-behavior/analysis.ipynb
```
