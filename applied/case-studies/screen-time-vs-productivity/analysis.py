#!/usr/bin/env python
# ---
# jupyter:
#   title: "Case Study: Screen Time vs Productivity"
#   purpose: "Analyze correlation between daily screen time and employee productivity"
#   dataset: "../../../data/raw/screen_time.csv"
# ---

# %% [markdown]
# # Case Study: Screen Time vs Productivity
# 
# **Business Question:** Does higher daily screen time correlate with lower productivity scores? 
# Should our organization implement strict policies or guide employees toward healthier screen limits?
# 
# **Why This Matters:** In a remote and digital-first work culture, screen time is at an all-time high. 
# While digital tools are essential for work, excessive screen time is often linked to fatigue, distraction, and cognitive overload. 
# This analysis checks if there is a statistical threshold where screen time starts negatively impacting productivity.
# 
# **Dataset:** Tech-firm employee screen tracking & self-reported productivity index (150 employees)  
# **Tools:** pandas, seaborn, scipy, matplotlib  
# **Key Skill:** Correlation Analysis, Fisher's z Transformation (CIs for correlation), Cohen's d Effect Size, Segmented Binning
# 
# ---

# %% [markdown]
# ## Pre-Analysis Decision Rules
# We establish our analytical decision framework:
# 1. **Significance Level:** We set our standard significance level to $\alpha = 0.05$.
# 2. **Decision Rule:** We will recommend implementing screen-free policies or breaks *only* if:
#    - There is a statistically significant overall negative correlation ($p < 0.05$).
#    - The standardized difference in productivity (Cohen's d) between high-screen-time users (>6 hours) and low/medium-screen-time users is at least **0.50** (medium-to-large effect size).

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set clean style
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100

# Load screen time dataset
df = pd.read_csv('../../../data/raw/screen_time.csv')
print(f"Loaded records for {len(df)} employees.")
df.head()

# %% [markdown]
# ## Step 1: Correlation Analysis (Overall Relationship & CIs)
# We compute Pearson and Spearman correlation coefficients and calculate the 95% confidence interval for Pearson's $r$ using the Fisher's z transformation.

# %%
pearson_r, p_val_p = stats.pearsonr(df['Screen_Time_Hours'], df['Productivity_Score'])
spearman_r, p_val_s = stats.spearmanr(df['Screen_Time_Hours'], df['Productivity_Score'])

# Fisher's z transform for confidence interval
z_r = 0.5 * np.log((1 + pearson_r) / (1 - pearson_r))
se_z = 1 / np.sqrt(len(df) - 3)
z_ci = [z_r - 1.96 * se_z, z_r + 1.96 * se_z]
pearson_ci = [np.tanh(z_ci[0]), np.tanh(z_ci[1])]

print("Correlation Analysis:")
print("=" * 40)
print(f"  Pearson correlation (r):  {pearson_r:.4f}  (p-value: {p_val_p:.4e})")
print(f"  Pearson 95% CI:           [{pearson_ci[0]:.4f}, {pearson_ci[1]:.4f}]")
print(f"  Spearman correlation (r): {spearman_r:.4f}  (p-value: {p_val_s:.4e})")

# %% [markdown]
# ### Observation:
# - There is a **strong negative correlation** ($r = -0.7431$, 95% CI: [$-0.8066$, $-0.6657$]).
# - The p-value is extremely small ($p < 0.001$), meaning this relationship is highly statistically significant.
# 
# Let's visualize this with a regression line.

# %%
fig, ax = plt.subplots(figsize=(10, 6))

sns.regplot(
    x='Screen_Time_Hours', 
    y='Productivity_Score', 
    data=df, 
    scatter_kws={'alpha':0.6, 'color': '#2B6CB0'},
    line_kws={'color': '#E53E3E', 'lw': 3},
    ax=ax
)

ax.set_title('Impact of Screen Time on Employee Productivity Score', fontweight='bold', fontsize=14)
ax.set_xlabel('Daily Screen Time (Hours)', fontsize=12)
ax.set_ylabel('Productivity Score (1-100)', fontsize=12)

# Annotate correlation coefficient
ax.text(
    7, 85, 
    f"Pearson's r = {pearson_r:.2f}\n95% CI: [{pearson_ci[0]:.2f}, {pearson_ci[1]:.2f}]", 
    bbox=dict(boxstyle="round,pad=0.3", fc="#FFF5F5", ec="#FEB2B2", lw=1),
    fontsize=11, fontweight='bold', color='#C53030'
)

plt.tight_layout()
plt.savefig('screen_time_vs_productivity_scatter.png', bbox_inches='tight', dpi=150)
plt.show()

# %% [markdown]
# ## Step 2: Segmented Analysis (Finding the Threshold)
# We segment employees into low, medium, and high screen time tiers:
# - **Low Screen Time:** < 4 hours
# - **Medium Screen Time:** 4 to 6 hours
# - **High Screen Time:** > 6 hours

# %%
# Define bins and labels
bins = [0, 4, 6, 24]
labels = ['Low (< 4 hrs)', 'Medium (4-6 hrs)', 'High (> 6 hrs)']
df['Screen_Time_Tier'] = pd.cut(df['Screen_Time_Hours'], bins=bins, labels=labels)

# Group by tier
tier_stats = df.groupby('Screen_Time_Tier', observed=False)['Productivity_Score'].agg(['count', 'mean', 'median', 'std']).reset_index()
print("Productivity Stats by Screen Time Tier:")
print("=" * 60)
print(tier_stats.round(1).to_string(index=False))

# %% [markdown]
# Let's check the correlation *within* each tier to see where the drop kicks in.

# %%
for tier in labels:
    tier_data = df[df['Screen_Time_Tier'] == tier]
    r, p = stats.pearsonr(tier_data['Screen_Time_Hours'], tier_data['Productivity_Score'])
    print(f"  {tier:18s} correlation: r = {r:.2f} (p-value: {p:.4f})")

# %% [markdown]
# ### Crucial Business Insight:
# - **Low Screen Time (<4 hrs):** No significant correlation ($r = 0.06$, $p = 0.69$).
# - **Medium Screen Time (4-6 hrs):** Weak negative correlation ($r = -0.19$, $p = 0.19$).
# - **High Screen Time (>6 hrs):** Strong negative correlation ($r = -0.52$, $p < 0.001$).
# - **The Tipping Point:** Employee productivity is stable up to 6 hours of daily screen time (averaging ~72-74 points). However, once screen time exceeds 6 hours, productivity scores drop sharply to an average of **50.6 points** (a **30%+ drop**).

# %% [markdown]
# ## Step 3: Compute Effect Size (Cohen's d)
# We combine Low and Medium tiers (<= 6 hours) into a single "Acceptable" group and compare it to the High tier (> 6 hours) to calculate the standardized effect size (Cohen's d).

# %%
low_med_scores = df[df['Screen_Time_Hours'] <= 6.0]['Productivity_Score']
high_scores = df[df['Screen_Time_Hours'] > 6.0]['Productivity_Score']

mean_diff = low_med_scores.mean() - high_scores.mean()
pooled_std = np.sqrt(((len(low_med_scores) - 1) * low_med_scores.var() + (len(high_scores) - 1) * high_scores.var()) / (len(low_med_scores) + len(high_scores) - 2))
cohens_d = mean_diff / pooled_std

print("Low/Medium vs. High Screen Time Comparison:")
print("=" * 45)
print(f"  Low/Medium Mean Score: {low_med_scores.mean():.2f} (N = {len(low_med_scores)})")
print(f"  High Mean Score:       {high_scores.mean():.2f} (N = {len(high_scores)})")
print(f"  Cohen's d Effect Size: {cohens_d:.4f} (Very large standardized difference)")

# %% [markdown]
# ## Step 4: Visualizing Productivity by Tier

# %%
fig, ax = plt.subplots(figsize=(8, 6))

sns.barplot(
    x='Screen_Time_Tier', 
    y='Productivity_Score', 
    data=df, 
    errorbar=('ci', 95), 
    capsize=0.1, 
    palette=['#38A169', '#3182CE', '#E53E3E'],
    ax=ax
)

ax.set_title('Average Productivity Score by Screen Time Tier', fontweight='bold', fontsize=14)
ax.set_xlabel('Daily Screen Time Tier', fontsize=12)
ax.set_ylabel('Average Productivity Score (95% CI)', fontsize=12)

# Annotate heights
for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2., 
        height - 8, 
        f'{height:.1f}', 
        ha="center", va="bottom", color="white", fontweight='bold', fontsize=12
    )

plt.tight_layout()
plt.savefig('productivity_by_tier_barplot.png', bbox_inches='tight', dpi=150)
plt.show()

# %% [markdown]
# ## Wrong Interpretation to Avoid: Causal Claim Warning
# > **Critical Caution:** Do not state that "high screen time causes employees to become less productive." Because this is observational data, we cannot prove a causal relationship. For example, employees who are struggling to get their work done (less productive) might have to spend more hours staring at their screens trying to finish, or distracted employees might browse the web longer (causing high screen time). Correlation does not equal causation.

# %% [markdown]
# ## Statistical Limitations
# 1. **Self-Reported Productivity:** Productivity scores are self-reported indices, which can introduce subjective measurement errors and reporting bias.
# 2. **Confounding Variables:** Factors like job complexity, employee seniority, and individual workspace setups are not included.
# 3. **Non-random Sampling:** The 150 employees tracked might not be representative of other companies or industries.

# %% [markdown]
# ## Key Finding
# 
# > ** Screen time has a clear tipping point associated with employee productivity, meeting our pre-analysis decision criteria. Below 6 hours, daily screen time has minimal correlation with productivity (scores average ~73). However, for employees with more than 6 hours of daily screen time, productivity scores drop by 31% to an average of 50.6. This difference represents an exceptionally large standardized effect size (Cohen's d = 1.95, highly significant). Focus on encouraging screen-free focus blocks and healthy breaks rather than complete screen time restriction policies.**
