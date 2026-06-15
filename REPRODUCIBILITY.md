# Reproducibility Guide

To ensure absolute replication of all results, figures, statistics, and interactive dashboards, follow this guide to align your local environment.

---

## 1. System Requirements & Environment Setup

This project is developed with **Python 3.10+** (tested up to Python 3.13) and managed using **Poetry** or standard **virtual environments**.

### Automated Environment Setup
The easiest way to initialize a clean environment is using the `Makefile`:

```bash
# 1. Initialize virtualenv and install all dependencies (runtime, dev, dashboard)
make setup
```

This creates a virtual environment in `.venv/` and installs core library requirements, development tools, and dashboard visualization libraries.

### Manual Setup (Alternative)
If you do not wish to use Poetry or GNU Make, you can configure your environment manually:

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install split dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -r requirements-dashboard.txt
```

---

## 2. Replication Commands (GNU Make Workflow)

Execute the following commands in sequence to reproduce the full project flow:

```bash
# 1. Setup the environment and install dependencies
make setup

# 2. Run the unit test suite and check code quality (black, isort, flake8)
make test
make lint

# 3. Precompute data aggregations from raw datasets
make generate-data

# 4. Execute all Jupyter Notebooks end-to-end (in-place execution check)
make run-notebooks

# 5. Run the Streamlit interactive dashboard locally
make run-dashboard
```

---

## 3. Data Integrity & Schema Validation

All raw datasets reside in the [data/raw/](file:///Users/the_irritater/Documents/Stats%20Series/data/raw/) directory as immutable CSV files.

### Schema Enforcement
Before any analytical step or notebook execution, datasets are validated against a machine-readable JSON schema located at [data/data-schema.json](file:///Users/the_irritater/Documents/Stats%20Series/data/data-schema.json). This checks:
- Column presence and type compliance (integers, floats, categories).
- Categorical options constraints (e.g., verifying `Discount_Applied` is strictly `Yes` or `No`).
- Data quality rules (e.g., duplicate customer identifiers, range limits).

### Cryptographic Hashes
Each raw dataset has its SHA-256 hash verified during testing to confirm the source data remains unmodified:
- `tips.csv`: `574e4c9f...`
- `ecommerce.csv`: `a2e584f2...`
- `screen_time.csv`: `7b32d0c1...`
- `customer_discounts.csv`: `1e54911d...`
- `marketing_campaign.csv`: `9f65c1bc...`

---

## 4. Deterministic Random Seeds

All calculations involving random states (synthetic data splits, segmentations, and model initializations) utilize a fixed random seed of **`42`**.
This ensures:
- Train-test splits in regression models remain identical.
- Cluster centroids in customer segmentations are stable.
- Resampling metrics yield identical confidence intervals and statistics.

Whenever replicating results manually, instantiate random components using:
```python
import numpy as np
np.random.seed(42)
```

---

## 5. Dashboard Deployment Guide (Streamlit Cloud)

The interactive dashboard can be deployed to Streamlit Community Cloud for public viewing.

### Steps to Deploy:
1. **GitHub Repository:** Ensure the latest changes are pushed to your GitHub repository.
2. **Streamlit Account:** Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) using your GitHub account credentials.
3. **New App:** Click the **"New app"** button.
4. **App Settings:**
   - **Repository:** Select `Stat_That_Make_Data_Speak` from the dropdown list.
   - **Branch:** Select `main` (or the active production branch).
   - **Main file path:** Set this to `dashboard/interactive_dashboard.py`.
5. **Advanced Settings (Optional):**
   - Ensure the deployment server reads `requirements.txt` and `requirements-dashboard.txt` to install dashboard packages. You can specify a custom `requirements.txt` path if required or merge them into one config file.
6. **Deploy:** Click **"Deploy!"**. Within minutes, your app will be live on a public URL.
