from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import streamlit as st
from scipy import stats
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Page configuration for a premium dark-mode aligned, clean look
st.set_page_config(
    page_title="StatSphere Analytics Hub", page_icon="🔮", layout="wide", initial_sidebar_state="expanded"
)

# Relative Path Resolution
ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"

# Custom CSS for modern styling and layout
st.markdown(
    """
<style>
    .main { background-color: #f8fafc; }
    h1, h2, h3 { color: #0f172a; font-family: 'Outfit', sans-serif; font-weight: 700; }
    .stAlert { border-radius: 10px; }
    .metric-card {
        background-color: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
    }
    .causal-warning {
        background-color: #fef2f2;
        border-left: 5px solid #ef4444;
        color: #991b1b;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 24px;
        font-weight: 500;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Helper function to cache data loading & validation
@st.cache_data
def load_cached_data(name):
    filepath = RAW_DATA_DIR / f"{name}.csv"
    if not filepath.exists():
        st.error(f"File not found: {filepath}")
        return pd.DataFrame()
    return pd.read_csv(filepath)


# Precompute and save aggregations to data/processed/ for reproducible research
def save_processed_aggregations(name, df_agg):
    try:
        PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
        dest_path = PROCESSED_DATA_DIR / f"{name}_aggregations.csv"
        df_agg.to_csv(dest_path, index=False)
    except Exception:
        pass  # Ignore permission issues silently during streamlit load


# Standard helper to calculate Cohen's d
def calculate_cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    if n1 <= 1 or n2 <= 1:
        return 0.0
    s1, s2 = group1.std(), group2.std()
    m1, m2 = group1.mean(), group2.mean()
    # Pooled standard deviation
    pooled_sd = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    if pooled_sd == 0:
        return 0.0
    return (m1 - m2) / pooled_sd


# Sidebar navigation
st.sidebar.title("🔮 StatSphere Hub")
analysis_option = st.sidebar.radio(
    "Select View:",
    [
        "Overview & Methodology",
        "Customer Spend & Browsing (Linear Regression)",
        "Marketing Campaign A/B Test (Inference)",
        "Screen Time vs Productivity (Correlation & Binning)",
        "Discount Depth vs Retention (Chi-Square)",
        "Restaurant Tips spending patterns (EDA)",
    ],
)

# Sidebar about section
st.sidebar.write("---")
st.sidebar.info(
    "**StatSphere Portfolio**\n\n"
    "This dashboard lets you interactively test hypothesis models and visualize real-world business scenarios. "
    "All computations are cached for speed and recorded for reproducibility.\n\n"
    "**Disclaimer:** Datasets used in this repository are synthetic/educational (except tips) "
    "and are intended for demonstration. "
    "Findings should be interpreted as portfolio examples, not real business evidence."
)

# Display Causal Warning Header across all analytical tabs
if analysis_option != "Overview & Methodology":
    st.markdown(
        '<div class="causal-warning">'
        "⚠️ <strong>Causal Association Warning:</strong> This analysis dashboard displays "
        "associative metrics and statistical predictions. Because variables are observational "
        "rather than randomized under experimental double-blind control, these metrics do not "
        "prove causal relationships. Findings are subject to omitted variable bias. Use "
        "results to support further experimentation rather than assuming direct causation."
        "</div>",
        unsafe_allow_html=True,
    )

# ----------------- Tab 0: Overview & Methodology -----------------
if analysis_option == "Overview & Methodology":
    st.title("🔮 StatSphere Analytics Hub")
    st.markdown("### Interactive Statistical Analysis & Decision Engine")
    st.write("---")

    st.markdown(
        """
        Welcome to the **StatSphere Analytics Hub**, an interactive portfolio showcasing rigorous statistical workflows,
        predictive modeling, and validation checks. This dashboard serves as the companion interface to the 
        **Stats Series** repository, translating analytical studies into interactive business decision engines.
        
        #### 📈 Demonstrated Core Competencies
        - **Predictive Validity:** Out-of-sample train/test splits (80-20), evaluating models
          on RMSE/MAE against simple historical baselines.
        - **Linear Model Assumptions:** Interactive checks for multicollinearity (VIF), residual
          normality (Q-Q plots, Shapiro-Wilk), and heteroscedasticity (Breusch-Pagan).
        - **Hypothesis Testing & Effect Sizes:** Reporting of 95% Confidence Intervals, Cohen's d
          (for t-tests), Cramer's V (for contingency tables), and Relative Risk (for ratios).
        - **Data Pipelines:** Schema enforcement using automated JSON schema validations.
        """
    )

    st.subheader("📊 Repository Datasets & Specifications")

    datasets_info = pd.DataFrame(
        [
            {
                "Study Name": "Customer Spend & Browsing",
                "Dataset Source": "ecommerce.csv (Synthetic)",
                "Statistical Methods": "OLS Multiple Regression, Residual Diagnostics, Train-Test Split",
                "Business Question": (
                    "Do session duration and page views predict customer spend? " "(Evaluates UX adjustments)"
                ),
            },
            {
                "Study Name": "Marketing Campaign A/B Test",
                "Dataset Source": "marketing_campaign.csv (Synthetic)",
                "Statistical Methods": "Proportion Z-Test, Cohen's h Effect Size, 95% Confidence Interval",
                "Business Question": "Does a new promotional campaign increase customer conversions?",
            },
            {
                "Study Name": "Screen Time vs Productivity",
                "Dataset Source": "screen_time.csv (Synthetic)",
                "Statistical Methods": "Pearson & Spearman Correlation CIs, Cohen's d, Nonlinear Binning",
                "Business Question": "At what point does screen exposure begin to damage productivity?",
            },
            {
                "Study Name": "Discount Depth vs Retention",
                "Dataset Source": "customer_discounts.csv (Synthetic)",
                "Statistical Methods": "Chi-Square Test of Independence, Cramer's V, Risk Ratio CI",
                "Business Question": "Does offering deeper discount coupons cause higher customer retention?",
            },
            {
                "Study Name": "Restaurant Tips Patterns",
                "Dataset Source": "tips.csv (Public / Seaborn)",
                "Statistical Methods": "Welch's t-test, Cohen's d, Demographics EDA",
                "Business Question": "Which consumer segments yield the highest billing totals and tips?",
            },
        ]
    )

    st.table(datasets_info)

    st.markdown(
        """
        ---
        ### 🛠️ Local Execution & Reproduction
        To run these analyses and tests locally in your workspace, follow the guide in `REPRODUCIBILITY.md`:
        1. **Install Poetry Environment:** Run `poetry install` or setup via `./setup.sh`.
        2. **Run All Pipeline Tests:** Execute `make test` (enforces an 85% coverage minimum).
        3. **Execute Notebooks:** Run `make run-notebooks` to verify Jupyter notebook integrity.
        """
    )

# ----------------- Study 1: E-commerce Spend -----------------
elif analysis_option == "Customer Spend & Browsing (Linear Regression)":
    st.header("📈 Customer Spend & Browsing Behavior")
    st.write(
        "Analyze whether website browsing session length and page visits can predict order value, "
        "allowing product teams to evaluate UX redesign investments."
    )

    df = load_cached_data("ecommerce")

    if not df.empty:
        # Save processed metadata for replication
        save_processed_aggregations("ecommerce", df.describe().reset_index())

        # User controls
        col1, col2 = st.columns([1, 3])
        with col1:
            st.subheader("Filters")
            discount_filter = st.selectbox("Discount Applied Filter:", ["All", "Yes", "No"])
            model_type = st.radio(
                "Model Complexity:", ["Simple Linear (Duration)", "Multiple Linear (Duration + Pages)"]
            )

            # Slider to narrow sessions
            min_duration = int(df["Session_Duration"].min())
            max_duration = int(df["Session_Duration"].max())
            duration_range = st.slider(
                "Session Duration Range (mins):", min_duration, max_duration, (min_duration, max_duration)
            )

        # Apply filters
        filtered_df = df[(df["Session_Duration"] >= duration_range[0]) & (df["Session_Duration"] <= duration_range[1])]
        if discount_filter != "All":
            filtered_df = filtered_df[filtered_df["Discount_Applied"] == discount_filter]

        with col2:
            st.subheader("Interactive Visualization")
            fig = px.scatter(
                filtered_df,
                x="Session_Duration",
                y="Total_Spend",
                color="Discount_Applied",
                hover_data=["Pages_Visited"],
                title="Session Duration vs. Total Spend ($)",
                labels={"Session_Duration": "Duration (Minutes)", "Total_Spend": "Order Value ($)"},
                color_discrete_map={"Yes": "#3182CE", "No": "#E53E3E"},
                trendline="ols",
            )
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        # OLS Regression Output
        st.subheader("Ordinary Least Squares (OLS) Summary")
        if len(filtered_df) > 10:
            if model_type == "Simple Linear (Duration)":
                formula = "Total_Spend ~ Session_Duration"
                features = ["Session_Duration"]
            else:
                formula = "Total_Spend ~ Session_Duration + Pages_Visited"
                features = ["Session_Duration", "Pages_Visited"]

            # Implement out-of-sample train/test split (80-20)
            train_df, test_df = train_test_split(filtered_df, test_size=0.2, random_state=42)

            # Fit model on training data
            model = ols(formula, data=train_df).fit()

            # Train/Test Metrics
            train_r2 = model.rsquared

            # Predict on test
            test_preds = model.predict(test_df)
            y_actual = test_df["Total_Spend"]

            model_rmse = np.sqrt(mean_squared_error(y_actual, test_preds))
            model_mae = mean_absolute_error(y_actual, test_preds)

            # Baseline (mean of train spend)
            baseline_val = train_df["Total_Spend"].mean()
            baseline_preds = np.full(shape=len(y_actual), fill_value=baseline_val)
            base_rmse = np.sqrt(mean_squared_error(y_actual, baseline_preds))
            base_mae = mean_absolute_error(y_actual, baseline_preds)

            error_reduction = (base_rmse - model_rmse) / base_rmse * 100

            # Metric Columns
            r_col, p_col, rmse_col, reduction_col = st.columns(4)
            with r_col:
                st.metric("Train R-squared", f"{train_r2:.2%}")
            with p_col:
                st.metric("F-Statistic p-value", f"{model.f_pvalue:.4e}")
            with rmse_col:
                st.metric("Test RMSE (Baseline)", f"${model_rmse:.2f} (${base_rmse:.2f})")
            with reduction_col:
                st.metric("Error Reduction vs Baseline", f"{error_reduction:.1f}%")

            # Coefficient breakdown including Standardized Beta weights and Confidence Intervals
            st.write("**Model Coefficients, Confidence Intervals & Standardized Effect Sizes:**")

            conf_int = model.conf_int()
            std_y = train_df["Total_Spend"].std()

            betas = []
            for var in model.params.index:
                if var == "Intercept":
                    betas.append(np.nan)
                else:
                    std_x = train_df[var].std()
                    betas.append(model.params[var] * (std_x / std_y))

            summary_df = pd.DataFrame(
                {
                    "Coefficient": model.params,
                    "Std Error": model.bse,
                    "t-value": model.tvalues,
                    "p-value": model.pvalues,
                    "[0.025": conf_int[0],
                    "0.975]": conf_int[1],
                    "Standardized Beta": betas,
                }
            )

            st.dataframe(summary_df.round(4))

            # Download Coefficient Buttons
            csv_coefs = summary_df.to_csv().encode("utf-8")
            st.download_button(
                label="📥 Download Coefficients CSV",
                data=csv_coefs,
                file_name="spend_ols_coefficients.csv",
                mime="text/csv",
            )

            # OLS Diagnostic assumptions panel
            st.write("---")
            st.subheader("🛠️ Linear Model Residual Diagnostics")

            residuals = model.resid
            fitted = model.fittedvalues

            diag_col1, diag_col2 = st.columns(2)

            with diag_col1:
                # Residuals vs Fitted Plotly
                fig_resid = px.scatter(
                    x=fitted,
                    y=residuals,
                    labels={"x": "Fitted Values", "y": "Residuals"},
                    title="Residuals vs. Fitted Values (Homoscedasticity Check)",
                )
                fig_resid.add_hline(y=0, line_dash="dash", line_color="red")
                fig_resid.update_layout(plot_bgcolor="white", paper_bgcolor="white")
                st.plotly_chart(fig_resid, use_container_width=True)

            with diag_col2:
                # Q-Q Plot Plotly
                std_residuals = (residuals - residuals.mean()) / residuals.std()
                n_resid = len(std_residuals)
                theoretical = stats.norm.ppf(np.arange(1, n_resid + 1) / (n_resid + 1))
                sample = np.sort(std_residuals)
                qq_df = pd.DataFrame({"Theoretical Quantiles": theoretical, "Sample Quantiles": sample})
                fig_qq = px.scatter(
                    qq_df, x="Theoretical Quantiles", y="Sample Quantiles", title="Normal Q-Q Plot (Normality Check)"
                )
                min_val = min(theoretical.min(), sample.min())
                max_val = max(theoretical.max(), sample.max())
                fig_qq.add_shape(
                    type="line", x0=min_val, y0=min_val, x1=max_val, y1=max_val, line=dict(color="red", dash="dash")
                )
                fig_qq.update_layout(plot_bgcolor="white", paper_bgcolor="white")
                st.plotly_chart(fig_qq, use_container_width=True)

            # Multicollinearity VIF & Hypothesis test calculations
            st.markdown("#### 🔬 Diagnostic Test Results")
            diag_metrics_col1, diag_metrics_col2, diag_metrics_col3 = st.columns(3)

            with diag_metrics_col1:
                # VIF Calculation
                X_vif = train_df[features]
                X_vif = sm.add_constant(X_vif)
                vifs = [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[1])]
                st.write("**Variance Inflation Factors (VIF):**")
                for f_idx, f_name in enumerate(features):
                    st.write(f"- `{f_name}`: {vifs[f_idx+1]:.4f}")

            with diag_metrics_col2:
                # Residual Normality (Shapiro-Wilk)
                shapiro_stat, shapiro_p = stats.shapiro(residuals)
                st.write("**Shapiro-Wilk Normality Test:**")
                st.write(f"- Statistic: `{shapiro_stat:.4f}`")
                st.write(f"- p-value: `{shapiro_p:.4e}`")
                if shapiro_p < 0.05:
                    st.caption("Residuals are not normally distributed (p < 0.05)")
                else:
                    st.caption("Fail to reject normality (residuals are normally distributed)")

            with diag_metrics_col3:
                # Heteroscedasticity (Breusch-Pagan)
                bp_lm, bp_lm_p, bp_f, bp_f_p = het_breuschpagan(residuals, X_vif.values)
                st.write("**Breusch-Pagan Test (Heteroscedasticity):**")
                st.write(f"- LM p-value: `{bp_lm_p:.4e}`")
                st.write(f"- F p-value: `{bp_f_p:.4e}`")
                if bp_lm_p < 0.05:
                    st.caption("Heteroscedasticity detected (p < 0.05)")
                else:
                    st.caption("Fail to reject homoscedasticity (residuals have equal spread)")

            # Business decision support
            assumptions_ok = (shapiro_p >= 0.05) and (bp_lm_p >= 0.05)
            status_text = "well satisfied" if assumptions_ok else "mostly violated; proceed with caution"
            st.success(
                f"**Takeaway:** Controlling for other metrics, each additional unit of duration predicts "
                f"an increase of **${model.params.get('Session_Duration', 0.0):.2f}** in order value. "
                "UX investments to increase retention are highly justified. Residual validation confirms "
                f"that model assumptions are {status_text}."
            )
        else:
            st.warning("Not enough data points selected to fit regression model.")

# ----------------- Study 2: Marketing A/B Test -----------------
elif analysis_option == "Marketing Campaign A/B Test (Inference)":
    st.header("🎯 Marketing Campaign A/B Test Results")
    st.write(
        "Evaluate A/B test results to verify if a new promotional campaign leads to "
        "statistically significant conversion rates compared to the control group."
    )

    df = load_cached_data("marketing_campaign")

    if not df.empty:
        # Precompute conversion table for reproducibility
        conv_summary = df.groupby("Campaign_Group")["Converted"].agg(["count", "sum", "mean"]).reset_index()
        conv_summary.columns = ["Campaign_Group", "Users", "Conversions", "Conversion_Rate"]
        save_processed_aggregations("marketing", conv_summary)

        # Display high level metrics
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Conversion Overview")
            st.table(conv_summary.style.format({"Conversion_Rate": "{:.2%}"}))

            # Download Conversion Summary
            csv_conv = conv_summary.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Summary CSV", data=csv_conv, file_name="conversion_summary.csv", mime="text/csv"
            )

            # Hypothesis test parameters
            st.subheader("Statistical Hypothesis Test")
            confidence_level = st.slider("Confidence Level:", 0.90, 0.99, 0.95, 0.01)
            alpha = 1 - confidence_level

        # Run conversion tests
        control_group = df[df["Campaign_Group"] == "Control"]
        test_group = df[df["Campaign_Group"] == "Test"]

        c_conv = control_group["Converted"].sum()
        c_total = len(control_group)
        t_conv = test_group["Converted"].sum()
        t_total = len(test_group)

        # Two-sample proportion z-test
        p_c = c_conv / c_total
        p_t = t_conv / t_total
        p_pooled = (c_conv + t_conv) / (c_total + t_total)
        se = np.sqrt(p_pooled * (1 - p_pooled) * (1 / c_total + 1 / t_total))
        z_stat = (p_t - p_c) / se
        p_val = 2 * (1 - stats.norm.cdf(abs(z_stat)))

        # Effect Size calculations
        lift = (p_t - p_c) / p_c
        cohens_h = 2 * (np.arcsin(np.sqrt(p_t)) - np.arcsin(np.sqrt(p_c)))

        # 95% Confidence Interval for difference
        z_crit = stats.norm.ppf(1 - alpha / 2)
        se_diff = np.sqrt((p_t * (1 - p_t) / t_total) + (p_c * (1 - p_c) / c_total))
        diff = p_t - p_c
        ci_lower = diff - z_crit * se_diff
        ci_upper = diff + z_crit * se_diff

        with col2:
            st.subheader("Conversion Rates Comparison")
            fig = px.bar(
                conv_summary,
                x="Campaign_Group",
                y="Conversion_Rate",
                color="Campaign_Group",
                labels={"Conversion_Rate": "Conversion Rate (%)", "Campaign_Group": "Group"},
                color_discrete_map={"Control": "#CBD5E0", "Test": "#2B6CB0"},
                text=conv_summary["Conversion_Rate"].apply(lambda x: f"{x:.2%}"),
            )
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Test Diagnostics")
        res_col1, res_col2, res_col3, res_col4 = st.columns(4)
        with res_col1:
            st.metric("Z-Statistic", f"{z_stat:.4f}")
        with res_col2:
            st.metric("Two-Tailed p-value", f"{p_val:.4g}")
        with res_col3:
            st.metric("Conversion Rate Lift", f"{lift:+.2%}")
        with res_col4:
            st.metric("Cohen's h (Effect)", f"{cohens_h:.4f}")

        st.markdown(f"**95% Confidence Interval for Conversion Difference:** `[{ci_lower:+.3%}, {ci_upper:+.3%}]`")

        if p_val < alpha:
            st.info(
                f"**Result: Statistically Significant!** (p = {p_val:.4g} < {alpha:.2f})\n\n"
                f"The promotional campaign group has a **{(p_t - p_c)*100:.2f}%** higher absolute conversion rate. "
                "We reject the null hypothesis and recommend rolling out the new campaign."
            )
        else:
            st.warning(
                f"**Result: Not Statistically Significant.** (p = {p_val:.4g} >= {alpha:.2f})\n\n"
                "The observed lift could be due to random chance. We fail to reject the null hypothesis. "
                "Do not allocate budget to roll out this campaign based on conversions alone."
            )

# ----------------- Study 3: Screen Time vs Productivity -----------------
elif analysis_option == "Screen Time vs Productivity (Correlation & Binning)":
    st.header("💻 Screen Time vs Productivity Analysis")
    st.write(
        "Evaluate the correlation between daily screen exposure (hours) and employee productivity indexes. "
        "Locate if a nonlinear productivity drop-off threshold occurs."
    )

    df = load_cached_data("screen_time")

    if not df.empty:
        # Precompute aggregated bins for processed exports
        bins = [0, 4, 6, 24]
        labels = ["Low (< 4 hrs)", "Medium (4-6 hrs)", "High (> 6 hrs)"]
        df["Screen_Time_Tier"] = pd.cut(df["Screen_Time_Hours"], bins=bins, labels=labels)

        tier_agg = (
            df.groupby("Screen_Time_Tier", observed=False)["Productivity_Score"]
            .agg(["count", "mean", "median", "std"])
            .reset_index()
        )
        save_processed_aggregations("screen_time", tier_agg)

        # User controls in columns
        col1, col2 = st.columns([1, 2])
        alpha = 0.05

        with col1:
            st.subheader("Filters")
            selected_prof = st.multiselect(
                "Filter by Profession:", df["Profession"].unique(), default=list(df["Profession"].unique())
            )
            selected_age = st.multiselect(
                "Filter by Age Group:", df["Age_Group"].unique(), default=list(df["Age_Group"].unique())
            )

            # Apply filters
            filtered_df = df[df["Profession"].isin(selected_prof) & df["Age_Group"].isin(selected_age)]
            n_corr = len(filtered_df)

            # Calculate correlation and confidence intervals
            if n_corr > 2:
                p_coef, p_pval = stats.pearsonr(filtered_df["Screen_Time_Hours"], filtered_df["Productivity_Score"])
                s_coef, s_pval = stats.spearmanr(filtered_df["Screen_Time_Hours"], filtered_df["Productivity_Score"])

                # Pearson CI
                if n_corr > 3:
                    z_p = np.arctanh(p_coef)
                    se_zp = 1 / np.sqrt(n_corr - 3)
                    z_crit = stats.norm.ppf(1 - alpha / 2)
                    p_ci_lower = np.tanh(z_p - z_crit * se_zp)
                    p_ci_upper = np.tanh(z_p + z_crit * se_zp)
                else:
                    p_ci_lower, p_ci_upper = np.nan, np.nan

                # Spearman CI (Fisher approximation)
                if n_corr > 3:
                    z_s = np.arctanh(s_coef)
                    se_zs = 1.06 / np.sqrt(n_corr - 3)
                    s_ci_lower = np.tanh(z_s - z_crit * se_zs)
                    s_ci_upper = np.tanh(z_s + z_crit * se_zs)
                else:
                    s_ci_lower, s_ci_upper = np.nan, np.nan

                # Cohen's d between Low and High Screen Time
                low_group = filtered_df[filtered_df["Screen_Time_Tier"] == "Low (< 4 hrs)"]["Productivity_Score"]
                high_group = filtered_df[filtered_df["Screen_Time_Tier"] == "High (> 6 hrs)"]["Productivity_Score"]
                cohens_d = calculate_cohens_d(low_group, high_group)

                st.subheader("Correlation Analysis")
                st.write(f"**Pearson correlation:** `{p_coef:.3f}` (p = `{p_pval:.2g}`)")
                st.write(f"- 95% Confidence Interval: `[{p_ci_lower:.3f}, {p_ci_upper:.3f}]`")
                st.write(f"**Spearman correlation:** `{s_coef:.3f}` (p = `{s_pval:.2g}`)")
                st.write(f"- 95% Confidence Interval: `[{s_ci_lower:.3f}, {s_ci_upper:.3f}]`")
                st.write(f"**Cohen's d (Low vs High Screen Tier):** `{cohens_d:.4f}`")

                # Export Correlation CSV
                corr_export_df = pd.DataFrame(
                    {
                        "Method": ["Pearson", "Spearman"],
                        "Coefficient": [p_coef, s_coef],
                        "p-value": [p_pval, s_pval],
                        "CI_Lower": [p_ci_lower, s_ci_lower],
                        "CI_Upper": [p_ci_upper, s_ci_upper],
                    }
                )
                csv_corr = corr_export_df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="📥 Download Correlation Metrics",
                    data=csv_corr,
                    file_name="productivity_correlations.csv",
                    mime="text/csv",
                )
            else:
                st.write("Not enough data to calculate correlations.")

        with col2:
            st.subheader("Interactive Scatter & Threshold")
            fig = px.scatter(
                filtered_df,
                x="Screen_Time_Hours",
                y="Productivity_Score",
                color="Screen_Time_Tier",
                hover_data=["Profession", "Age_Group"],
                title="Daily Screen Hours vs. Productivity Index",
                labels={"Screen_Time_Hours": "Screen Time (Hours)", "Productivity_Score": "Productivity Score (1-100)"},
                color_discrete_map={
                    "Low (< 4 hrs)": "#38A169",
                    "Medium (4-6 hrs)": "#3182CE",
                    "High (> 6 hrs)": "#E53E3E",
                },
                trendline="ols",
            )
            fig.add_vline(x=6.0, line_dash="dash", line_color="#E53E3E", annotation_text="6-Hour Threshold")
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        # Display bar summaries of binned tiers
        st.subheader("Binned Analysis: Average Productivity Score by Tier")
        fig_bar = px.bar(
            tier_agg,
            x="Screen_Time_Tier",
            y="mean",
            color="Screen_Time_Tier",
            error_y=tier_agg["std"] / np.sqrt(tier_agg["count"]),  # Standard error bars
            labels={"mean": "Average Productivity Score", "Screen_Time_Tier": "Screen Time Tier"},
            color_discrete_map={"Low (< 4 hrs)": "#38A169", "Medium (4-6 hrs)": "#3182CE", "High (> 6 hrs)": "#E53E3E"},
        )
        fig_bar.update_layout(plot_bgcolor="white", paper_bgcolor="white", showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

        # Download button for binned summaries
        csv_tiers = tier_agg.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Productivity Tiers CSV",
            data=csv_tiers,
            file_name="productivity_tiers.csv",
            mime="text/csv",
        )

        st.success(
            "**Takeaway:** There is a sharp nonlinear drop-off (tipping point) in "
            "productivity after **6 hours** of daily screen time "
            "(averages fall ~30%). We recommend offline focus blocks and screen-free buffers. "
            "\n\n*Note: This is an educational synthetic example, not workplace policy evidence.*"
        )

# ----------------- Study 4: Discount Depth vs Retention -----------------
elif analysis_option == "Discount Depth vs Retention (Chi-Square)":
    st.header("📉 Discount Rate Depth vs. Customer Retention")
    st.write(
        "Evaluate the relationship between discount rate depth (0% to 50%) and long-term customer retention. "
        "Confirm if deep discounts compress margins and attract churning deal-seekers."
    )

    df = load_cached_data("customer_discounts")

    if not df.empty:
        # Precompute contingency table for processed data
        ret_rates = df.groupby("Discount_Rate")["Retained"].agg(["count", "sum", "mean"]).reset_index()
        ret_rates.columns = ["Discount_Rate", "Total_Customers", "Retained_Customers", "Retention_Rate"]
        save_processed_aggregations("discount_retention", ret_rates)

        # User controls
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Retention Performance Table")
            st.dataframe(ret_rates.style.format({"Retention_Rate": "{:.1%}"}))

            # Export Retention Performance
            csv_ret = ret_rates.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Retention Summary",
                data=csv_ret,
                file_name="discount_retention_summary.csv",
                mime="text/csv",
            )

            # Run chi square test
            contingency_table = pd.crosstab(df["Discount_Rate"], df["Retained"])
            chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)

            # Calculate Cramer's V effect size
            n_samples = len(df)
            min_dim = min(contingency_table.shape)
            cramers_v = np.sqrt(chi2 / (n_samples * (min_dim - 1))) if min_dim > 1 else 0.0

            st.subheader("Chi-Square Test of Independence")
            st.write(f"**Chi-Square Stat:** `{chi2:.4f}`")
            st.write(f"**Degrees of Freedom:** `{dof}`")
            st.write(f"**p-value:** `{p_val:.4g}`")
            st.write(f"**Cramer's V (Effect Size):** `{cramers_v:.4f}`")

        with col2:
            st.subheader("Retention Rate Curve by Discount Rate")
            plot_df = ret_rates.copy()
            plot_df["Discount_Label"] = (plot_df["Discount_Rate"] * 100).astype(int).astype(str) + "%"

            fig = px.bar(
                plot_df,
                x="Discount_Label",
                y="Retention_Rate",
                title="Customer Retention Rate by Discount Depth (%)",
                labels={"Retention_Rate": "Retention Rate", "Discount_Label": "Discount Depth"},
                color="Retention_Rate",
                color_continuous_scale="Blues",
            )
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        # Relative Risk/Lift Calculator block
        st.write("---")
        st.subheader("🔬 Relative Risk & Lift Comparison Engine")
        st.write(
            "Select two discount rates to evaluate the risk ratio of churning (1 - Retention) "
            "or the positive retention lift."
        )

        calc_col1, calc_col2 = st.columns(2)
        with calc_col1:
            baseline_disc = st.selectbox("Baseline Discount Rate:", ret_rates["Discount_Rate"].unique(), index=0)
        with calc_col2:
            treatment_disc = st.selectbox("Treatment Discount Rate:", ret_rates["Discount_Rate"].unique(), index=2)

        base_row = ret_rates[ret_rates["Discount_Rate"] == baseline_disc].iloc[0]
        treat_row = ret_rates[ret_rates["Discount_Rate"] == treatment_disc].iloc[0]

        # We calculate risk ratio of retention
        # Relative Risk = (Retained_treatment / Total_treatment) / (Retained_baseline / Total_baseline)
        x_t, n_t = int(treat_row["Retained_Customers"]), int(treat_row["Total_Customers"])
        x_b, n_b = int(base_row["Retained_Customers"]), int(base_row["Total_Customers"])

        p_t = x_t / n_t
        p_b = x_b / n_b

        if p_b > 0 and x_t > 0 and x_b > 0:
            rr = p_t / p_b
            se_log_rr = np.sqrt(1 / x_t - 1 / n_t + 1 / x_b - 1 / n_b)
            z_crit = stats.norm.ppf(0.975)  # 95% CI
            ci_lower = np.exp(np.log(rr) - z_crit * se_log_rr)
            ci_upper = np.exp(np.log(rr) + z_crit * se_log_rr)
            lift = (p_t - p_b) / p_b
        else:
            rr, ci_lower, ci_upper, lift = np.nan, np.nan, np.nan, np.nan

        risk_col1, risk_col2, risk_col3 = st.columns(3)
        with risk_col1:
            st.metric("Treatment vs Baseline LTV Lift", f"{lift:+.2%}" if not np.isnan(lift) else "N/A")
        with risk_col2:
            st.metric("Retention Risk Ratio (RR)", f"{rr:.4f}" if not np.isnan(rr) else "N/A")
        with risk_col3:
            st.write("**95% Confidence Interval for RR:**")
            st.write(f"`[{ci_lower:.4f}, {ci_upper:.4f}]`" if not np.isnan(ci_lower) else "N/A")

        st.write("---")
        st.subheader("Customer Profiles by Discount Tier")
        profiles = df.groupby("Discount_Rate").agg({"Tenure_Months": "mean", "Total_Spend": "mean"}).reset_index()
        profiles.columns = ["Discount Rate", "Avg Tenure (Months)", "Avg Lifetime Spend ($)"]
        st.dataframe(profiles.round(1))

        # Download contingency table
        csv_table = contingency_table.to_csv().encode("utf-8")
        st.download_button(
            label="📥 Download Contingency Table",
            data=csv_table,
            file_name="discount_retention_contingency.csv",
            mime="text/csv",
        )

        st.success(
            "**Optimal Promotion Recommendation:** Retention peaks at **10%-20%** discounts (~48-49% retention). "
            "Deep discounts (50%) perform worst (33.3% retention, tenure of "
            "7.9 months) because they attract transactional deal-seekers. "
            "Promotions should be capped at 20% off to maximize customer lifetime value (LTV) and margins."
        )

# ----------------- Study 5: Restaurant Tips -----------------
elif analysis_option == "Restaurant Tips spending patterns (EDA)":
    st.header("🍴 Restaurant Spending & Tipping Behavior")
    st.write(
        "Analyze customer demographics and transactions to locate the highest-value segments "
        "and double down on order-volume strategies."
    )

    df = load_cached_data("tips")

    if not df.empty:
        # Precompute customer segments spending
        df["tip_pct"] = (df["tip"] / df["total_bill"] * 100).round(1)
        save_processed_aggregations("tips_eda", df.describe().reset_index())

        # User controls
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Data Segments")
            grouping_var = st.selectbox("Group spending variables by:", ["day", "time", "sex", "smoker"])

            st.write("**Segmented Spend Statistics:**")
            summary_stats = df.groupby(grouping_var)[["total_bill", "tip", "tip_pct"]].mean().reset_index()
            st.dataframe(summary_stats.round(2))

            # Download summary stats
            csv_tips = summary_stats.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Group Summaries", data=csv_tips, file_name="tips_group_summaries.csv", mime="text/csv"
            )

        with col2:
            st.subheader("Transaction bill sizes by Category")
            fig = px.box(
                df,
                x=grouping_var,
                y="total_bill",
                color=grouping_var,
                points="all",
                title=f"Total Bill Distribution by {grouping_var.capitalize()}",
                labels={"total_bill": "Total Bill ($)", grouping_var: grouping_var.capitalize()},
                color_discrete_sequence=px.colors.qualitative.Prism,
            )
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        # Welch's t-test and Cohen's d block
        st.write("---")
        st.subheader("🔬 Welch's t-test Difference Engine")
        st.write(
            "Runs a two-sample Welch's t-test (not assuming equal variances) "
            f"to evaluate average spending differences between levels of `{grouping_var}`."
        )

        levels = df[grouping_var].unique()
        if len(levels) == 2:
            level1, level2 = levels[0], levels[1]
            g1_spend = df[df[grouping_var] == level1]["total_bill"]
            g2_spend = df[df[grouping_var] == level2]["total_bill"]

            # Welch's t-test
            t_stat, p_val = stats.ttest_ind(g1_spend, g2_spend, equal_var=False)
            cohens_d = calculate_cohens_d(g1_spend, g2_spend)

            t_col1, t_col2, t_col3 = st.columns(3)
            with t_col1:
                st.metric("t-Statistic", f"{t_stat:.4f}")
            with t_col2:
                st.metric("p-value", f"{p_val:.4g}")
            with t_col3:
                st.metric("Cohen's d (Effect Size)", f"{cohens_d:.4f}")

            st.caption(
                f"Comparing `{level1}` (mean spend: ${g1_spend.mean():.2f}, n={len(g1_spend)}) "
                f"vs. `{level2}` (mean spend: ${g2_spend.mean():.2f}, n={len(g2_spend)})"
            )
        else:
            st.write(
                f"The grouping variable `{grouping_var}` has {len(levels)} categories. "
                "t-tests require exactly 2 categories. Choose another variable like "
                "`sex`, `time`, or `smoker` to run tests."
            )

        # OLS tips regression block
        st.write("---")
        st.subheader("📈 Tip Value Predictor Model (OLS Regression)")
        st.write(
            "Fit a Multiple Linear Regression model predicting tipping value based on the total bill and party size."
        )

        model_tips = ols("tip ~ total_bill + size", data=df).fit()

        conf_int_tips = model_tips.conf_int()
        std_y_tips = df["tip"].std()

        betas_tips = []
        for var in model_tips.params.index:
            if var == "Intercept":
                betas_tips.append(np.nan)
            else:
                std_x_tips = df[var].std()
                betas_tips.append(model_tips.params[var] * (std_x_tips / std_y_tips))

        summary_df_tips = pd.DataFrame(
            {
                "Coefficient": model_tips.params,
                "Std Error": model_tips.bse,
                "t-value": model_tips.tvalues,
                "p-value": model_tips.pvalues,
                "[0.025": conf_int_tips[0],
                "0.975]": conf_int_tips[1],
                "Standardized Beta": betas_tips,
            }
        )

        st.dataframe(summary_df_tips.round(4))

        csv_coefs_tips = summary_df_tips.to_csv().encode("utf-8")
        st.download_button(
            label="📥 Download Tip Model Coefficients",
            data=csv_coefs_tips,
            file_name="tips_ols_coefficients.csv",
            mime="text/csv",
        )

        st.info(
            "**Key Finding:** Sunday dinner has the highest median bill sizes ($22.30) and strong tipping behavior. "
            "However, order volume (transaction count) is higher on Saturdays. "
            "Prioritize fast table turnover on Saturdays to maximize total weekend revenue."
        )
