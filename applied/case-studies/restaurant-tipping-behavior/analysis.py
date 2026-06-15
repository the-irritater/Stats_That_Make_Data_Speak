#!/usr/bin/env python
# ---
# jupyter:
#   title: "Case Study: Restaurant Tipping Behavior (Real-world Dataset)"
#   purpose: "Analyze factors associated with tipping percentage using t-tests and OLS regression"
#   dataset: "data/raw/tips.csv"
# ---

# %% [markdown]
# # Case Study: Restaurant Tipping Behavior
# 
# **Business Question:** What factors are most strongly associated with restaurant tip amounts and percentages? Specifically, do dinner patrons tip at a higher rate than lunch patrons? Does party size or bill size predict the absolute tip value?
# 
# **Why This Matters:** In the hospitality industry, understanding server compensation and customer behavior is critical for staffing, pricing, and point-of-sale tipping prompt designs.
# 
# **Dataset:** Bryant & Smith (1995) Restaurant Tips Dataset (244 transactions)  
# **Tools:** pandas, seaborn, scipy, statsmodels, matplotlib  
# **Key Skill:** Two-Sample t-test, Multiple Linear Regression, Residual Diagnostics, Standardized Effect Sizes, VIF
# 
# ---

# %% [markdown]
# ## Pre-Analysis Decision Rules
# Before running the tests, we define our analytical parameters:
# 1. **Significance Level:** We set our standard significance level to $\alpha = 0.05$.
# 2. **Decision Rule:** A factor (meal time, party size, total bill) is associated with tipping behavior if:
#    - The Welch's t-test yields $p < 0.05$ (for meal time).
#    - The OLS coefficient yields $p < 0.05$ (for total bill and party size).

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.graphics.gofplots import qqplot
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan

CASE_STUDY_DIR = Path(__file__).resolve().parent
ROOT_DIR = CASE_STUDY_DIR.parents[2]
DATA_PATH = ROOT_DIR / "data" / "raw" / "tips.csv"
DIAGNOSTICS_PATH = CASE_STUDY_DIR / "residual_diagnostics.png"

# Set clean style
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["figure.dpi"] = 100

# %% [markdown]
# ## Step 1: Load the Data & Calculate Tip Percentage

# %%
def load_tips_data(path=DATA_PATH):
    """Load the restaurant tips data and add a rounded tip percentage column."""
    df = pd.read_csv(path)
    df["tip_pct"] = (df["tip"] / df["total_bill"] * 100).round(2)
    return df

# %% [markdown]
# ## Step 2: Hypothesis Testing — Lunch vs. Dinner Tipping
# 
# Let's test if there is a significant difference in the tip percentage between Lunch and Dinner visits.
# * **Null Hypothesis ($H_0$):** There is no difference in mean tipping percentage between lunch and dinner.
# * **Alternative Hypothesis ($H_1$):** There is a significant difference in mean tipping percentage between lunch and dinner.

# %%
def run_lunch_dinner_ttest(df):
    """Run Welch's t-test comparing lunch and dinner tip percentages and compute Cohen's d."""
    lunch_tips = df[df["time"] == "Lunch"]["tip_pct"]
    dinner_tips = df[df["time"] == "Dinner"]["tip_pct"]
    
    t_stat, p_val = stats.ttest_ind(lunch_tips, dinner_tips, equal_var=False)
    
    # Cohen's d calculation
    n_lunch = len(lunch_tips)
    n_dinner = len(dinner_tips)
    pooled_std = np.sqrt(((n_lunch - 1) * lunch_tips.var() + (n_dinner - 1) * dinner_tips.var()) / (n_lunch + n_dinner - 2))
    cohens_d = (lunch_tips.mean() - dinner_tips.mean()) / pooled_std
    
    # 95% Confidence Interval for mean difference
    mean_diff = lunch_tips.mean() - dinner_tips.mean()
    se_diff = np.sqrt((lunch_tips.var() / n_lunch) + (dinner_tips.var() / n_dinner))
    ci_lower = mean_diff - 1.96 * se_diff
    ci_upper = mean_diff + 1.96 * se_diff
    
    return lunch_tips, dinner_tips, t_stat, p_val, cohens_d, (ci_lower, ci_upper)

# %% [markdown]
# ### Statistical Interpretation:
# * Since $p = 0.5145 > 0.05$, we fail to reject the null hypothesis.
# * **Cohen's d = 0.0757:** The standardized effect size is extremely small, confirming that the difference in tipping rates (%) between lunch and dinner patrons is practically negligible.
# * **95% Confidence Interval:** The CI for the mean tipping rate difference is `[-1.00%, 1.92%]`. Since it contains zero, we confirm no statistical difference.

# %% [markdown]
# ## Step 3: Predictive Modeling — Multiple Linear Regression
# 
# Let's build a multiple linear regression model to predict the absolute `tip` based on `total_bill` and party `size`.
# $$\text{Tip} = \beta_0 + \beta_1 \times \text{Total Bill} + \beta_2 \times \text{Party Size} + \epsilon$$

# %%
def fit_tip_model(df):
    """Fit the OLS model used in this case study."""
    return ols("tip ~ total_bill + size", data=df).fit()

# %% [markdown]
# ### Model Interpretation:
# * **R-squared ($R^2 = 0.468$):** The model predicts approximately 46.8% of the variance in tip amounts.
# * **Total Bill Coefficient ($\beta_1 = 0.0927$):** Controlling for party size, each additional dollar on the total bill is associated with an expected increase of ~$0.09 in the tip amount (95% CI: [$0.075$, $0.111$], $p < 0.001$).
# * **Party Size Coefficient ($\beta_2 = 0.1926$):** Controlling for the bill amount, each additional person in the party is associated with an expected increase of ~$0.19 in the tip amount (95% CI: [$0.025$, $0.361$], $p = 0.025$).

# %% [markdown]
# ## Step 4: Residual Diagnostics

# %%
def plot_residual_diagnostics(model, output_path=DIAGNOSTICS_PATH, show=True):
    """Create and save residual diagnostic plots for the fitted OLS model."""
    residuals = model.resid
    fitted = model.fittedvalues

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    sns.scatterplot(x=fitted, y=residuals, alpha=0.7, ax=axes[0])
    axes[0].axhline(0, color="red", linestyle="--", lw=2)
    axes[0].set_title("Residuals vs. Fitted Values", fontweight="bold")
    axes[0].set_xlabel("Fitted Values")
    axes[0].set_ylabel("Residuals")

    qqplot(residuals, line="s", ax=axes[1])
    axes[1].get_lines()[1].set_color("red")
    axes[1].set_title("Normal Q-Q Plot of Residuals", fontweight="bold")

    plt.tight_layout()
    fig.savefig(output_path, bbox_inches="tight", dpi=150)
    if show:
         plt.show()
    else:
         plt.close(fig)
    return output_path

# %% [markdown]
# ### Diagnostics Takeaway:
# * **Homoscedasticity:** The residuals vs. fitted plot shows a slight expansion (fan shape) at higher fitted values, suggesting mild heteroscedasticity.
# * **Normality:** Q-Q plot shows right skewness at the upper tail. The residual plots do not show severe violations, so the model is acceptable for this educational analysis.

# %% [markdown]
# ## Wrong Interpretation to Avoid: Causal Claim Warning
# > **Critical Caution:** Do not conclude that "expanding party sizes causes higher tips." Tipping is an observational behavior. Customers dining in larger parties might buy more items or feel more social pressure, which are confounding variables. The regression model captures *association*, not *causal proof*.

# %% [markdown]
# ## Statistical Limitations
# 1. **Observational Limit:** The lack of experimental randomization means we cannot confirm causal links.
# 2. **Omitted Factors:** Customer satisfaction, server service quality, and payment method (cash vs. card) are not captured in the dataset.
# 3. **Heteroscedasticity:** Tipping variance tends to scale with bill size, violating the constant variance assumption.

# %% [markdown]
# ## Key Finding
# 
# > **Absolute tips are strongly associated with bill size and party size. Together, they explain 46.8% of the variance in tips, with each dollar increase in bill size predicting an extra $0.09 in tips (95% CI: [$0.075$, $0.111$], p < 0.001), and each extra party member predicting an extra $0.19 (95% CI: [$0.025$, $0.361$], p = 0.025). Tipping rates (%), however, do not significantly differ between lunch and dinner times (Welch's t-test p = 0.5145, Cohen's d = 0.0757), showing that dining period is not a strong differentiator of tipping percentages in this dataset.**

# %%
def main():
    """Run the full restaurant tipping case study."""
    df = load_tips_data()
    print(f"Loaded records for {len(df)} restaurant visits.")
    print(df.head())

    lunch_tips, dinner_tips, t_stat, p_val, cohens_d, ci = run_lunch_dinner_ttest(df)
    print(
        f"\nLunch Tip Pct - Mean: {lunch_tips.mean():.2f}%, "
        f"Median: {lunch_tips.median():.2f}%, N: {len(lunch_tips)}"
    )
    print(
        f"Dinner Tip Pct - Mean: {dinner_tips.mean():.2f}%, "
        f"Median: {dinner_tips.median():.2f}%, N: {len(dinner_tips)}"
    )
    print(f"t-test results: t-statistic = {t_stat:.4f}, p-value = {p_val:.4f}")
    print(f"Cohen's d (Effect Size): {cohens_d:.4f}")
    print(f"95% CI for Difference:   [{ci[0]:.2f}%, {ci[1]:.2f}%]")

    model = fit_tip_model(df)
    print(model.summary())
    
    # VIF check
    X = df[['total_bill', 'size']]
    X = sm.add_constant(X)
    vifs = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    print("\nVariance Inflation Factors (VIF):")
    print(f"  total_bill VIF: {vifs[1]:.4f}")
    print(f"  size VIF:       {vifs[2]:.4f}")
    
    # Shapiro-Wilk test
    shapiro_stat, shapiro_p = stats.shapiro(model.resid)
    print(f"\nShapiro-Wilk test for residuals normality (p-value): {shapiro_p:.4e}")
    
    # Breusch-Pagan test
    bp_lm, bp_lm_p, bp_f, bp_f_p = het_breuschpagan(model.resid, X.values)
    print(f"Breusch-Pagan test for heteroscedasticity (p-value): {bp_lm_p:.4e}")

    plot_residual_diagnostics(model, show=False)


if __name__ == "__main__":
    main()
