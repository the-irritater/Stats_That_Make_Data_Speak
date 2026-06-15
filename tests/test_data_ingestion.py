from pathlib import Path

import pandas as pd
import pytest

from stats_series.data_loader import DataLoader


def test_data_loader_init():
    loader = DataLoader()
    assert loader.root_dir.exists()
    assert loader.schema_path.exists()
    assert "tips" in loader.schema


def test_raw_data_path():
    loader = DataLoader()
    path = loader.get_raw_data_path("tips")
    assert isinstance(path, Path)
    assert path.name == "tips.csv"


def test_validate_valid_dataframe():
    loader = DataLoader()
    # Create a valid tips df
    valid_tips = pd.DataFrame(
        {
            "total_bill": [15.20, 22.40],
            "tip": [2.50, 4.00],
            "sex": ["Male", "Female"],
            "smoker": ["No", "Yes"],
            "day": ["Thur", "Sat"],
            "time": ["Lunch", "Dinner"],
            "size": [2, 4],
        }
    )
    # This should complete without exceptions
    assert loader.validate_dataframe(valid_tips, "tips") is True


def test_validate_missing_columns():
    loader = DataLoader()
    # Missing 'size' column
    invalid_tips = pd.DataFrame(
        {
            "total_bill": [15.20, 22.40],
            "tip": [2.50, 4.00],
            "sex": ["Male", "Female"],
            "smoker": ["No", "Yes"],
            "day": ["Thur", "Sat"],
            "time": ["Lunch", "Dinner"],
        }
    )
    with pytest.raises(ValueError, match="missing expected columns"):
        loader.validate_dataframe(invalid_tips, "tips")


def test_validate_invalid_categorical():
    loader = DataLoader()
    # Invalid 'sex' option 'Unknown'
    invalid_tips = pd.DataFrame(
        {
            "total_bill": [15.20, 22.40],
            "tip": [2.50, 4.00],
            "sex": ["Male", "Unknown"],
            "smoker": ["No", "Yes"],
            "day": ["Thur", "Sat"],
            "time": ["Lunch", "Dinner"],
            "size": [2, 4],
        }
    )
    with pytest.raises(ValueError, match="contains unexpected values"):
        loader.validate_dataframe(invalid_tips, "tips")


def test_validate_invalid_type():
    loader = DataLoader()
    # 'total_bill' is text/string instead of numeric float
    invalid_tips = pd.DataFrame(
        {
            "total_bill": ["fifteen", "twenty-two"],
            "tip": [2.50, 4.00],
            "sex": ["Male", "Female"],
            "smoker": ["No", "Yes"],
            "day": ["Thur", "Sat"],
            "time": ["Lunch", "Dinner"],
            "size": [2, 4],
        }
    )
    with pytest.raises(TypeError, match="expected float"):
        loader.validate_dataframe(invalid_tips, "tips")


def test_load_real_tips_dataset():
    loader = DataLoader()
    df = loader.load_dataset("tips")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert "total_bill" in df.columns


def test_validate_primary_key_duplicates():
    loader = DataLoader()
    # Create invalid ecommerce df with duplicate Customer_ID
    invalid_ecommerce = pd.DataFrame(
        {
            "Customer_ID": [1, 1],
            "Session_Duration": [12.5, 14.2],
            "Pages_Visited": [8, 10],
            "Discount_Applied": ["Yes", "No"],
            "Total_Spend": [120.50, 150.00],
            "Repeat_Purchase": [1, 0],
            "Recency": [15, 30],
            "Frequency": [4, 5],
            "Monetary": [480.0, 750.0],
        }
    )
    with pytest.raises(ValueError, match="contains duplicate primary keys"):
        loader.validate_dataframe(invalid_ecommerce, "ecommerce")


def test_validate_categorical_outliers():
    loader = DataLoader()
    # Create invalid marketing df with categorical outliers
    invalid_marketing = pd.DataFrame(
        {
            "User_ID": [101, 102],
            "Campaign_Group": ["Control", "SuperTest"],  # 'SuperTest' is not valid
            "Converted": [0, 1],
            "Purchase_Amount": [0.0, 45.0],
        }
    )
    with pytest.raises(ValueError, match="contains unexpected values"):
        loader.validate_dataframe(invalid_marketing, "marketing_campaign")


def test_dashboard_data_loading_utility(tmp_path, monkeypatch):
    from dashboard.interactive_dashboard import load_cached_data

    # Set the RAW_DATA_DIR to a temporary directory for testing
    monkeypatch.setattr("dashboard.interactive_dashboard.RAW_DATA_DIR", tmp_path)

    # Test handling of missing file
    df_missing = load_cached_data("non_existent_dataset")
    assert df_missing.empty

    # Test loading of valid file
    temp_df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    temp_df.to_csv(tmp_path / "valid_dataset.csv", index=False)

    df_valid = load_cached_data("valid_dataset")
    assert not df_valid.empty
    assert list(df_valid.columns) == ["col1", "col2"]
