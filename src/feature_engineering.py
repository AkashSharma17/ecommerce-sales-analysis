"""
Feature engineering module for the Ecommerce Sales Analysis Pipeline.
Derives additional columns used in downstream analysis.
"""

import pandas as pd
import logging


class FeatureEngineer:
    """Adds derived columns to the cleaned sales dataset."""

    def feature_engineering(self, df):
        """Create Total_Sales, Month, and Year columns from existing data."""
        logging.info("Starting feature engineering process...")
        df_feature = df.copy()

        df_feature["Total_Sales"] = df_feature["Quantity"] * df_feature["Price_Per_Unit"]
        logging.info("Created 'Total_Sales' column successfully.")

        if "Order_Date" in df_feature.columns and pd.api.types.is_datetime64_any_dtype(
            df_feature["Order_Date"]
        ):
            df_feature["Month"] = df_feature["Order_Date"].dt.month
            df_feature["Year"] = df_feature["Order_Date"].dt.year
            logging.info("Extracted 'Month' and 'Year' from 'Order_Date'.")
        else:
            logging.warning("'Order_Date' is missing or not in datetime format. Month/Year extraction skipped.")

        logging.info("Feature engineering completed successfully.")
        return df_feature