"""
Data cleaning module for the Ecommerce Sales Analysis Pipeline.
Handles dataset inspection, deduplication, missing values, type fixes,
and anomaly removal.
"""

import pandas as pd
import logging
import io


class DataCleaner:
    """Performs cleaning and validation operations on the raw sales dataset."""

    def dataset_info(self, df):
        """Log dataset structure and missing value counts."""
        logging.info("Extracting dataset summary and missing value counts...")

        buffer = io.StringIO()
        df.info(buf=buffer)
        info_string = buffer.getvalue()

        missing_info = df.isna().sum().to_string()

        logging.info(f"\n=== DATASET INFO ===\n{info_string}")
        logging.info(f"\n=== MISSING VALUES ===\n{missing_info}")

    def remove_duplicates(self, df):
        """Remove duplicate rows from the dataset."""
        df_cleaned = df.copy()
        before = df_cleaned.shape[0]
        df_cleaned = df_cleaned.drop_duplicates()
        after = df_cleaned.shape[0]

        logging.info(f"Removed {before - after} duplicate rows. Remaining rows: {after}")
        return df_cleaned

    def handle_missing_values(self, df):
        """Fill missing values: median for numeric columns, 'Unknown' for categorical."""
        logging.info("Handling missing values in numeric and categorical columns...")
        df_cleaned = df.copy()

        numeric_columns = df_cleaned.select_dtypes(include=["int64", "float64"]).columns
        for col in numeric_columns:
            median_val = df_cleaned[col].median()
            df_cleaned[col] = df_cleaned[col].fillna(median_val)
            logging.info(f"Filled missing values in numeric column '{col}' with median: {median_val}")

        categorical_columns = df_cleaned.select_dtypes(include=["object"]).columns
        for col in categorical_columns:
            df_cleaned[col] = df_cleaned[col].fillna("Unknown")
            logging.info(f"Filled missing values in categorical column '{col}' with 'Unknown'")

        logging.info("All missing values handled successfully.")
        return df_cleaned

    def fix_data_types(self, df):
        """Convert columns to their correct data types."""
        logging.info("Fixing data types...")
        df_cleaned = df.copy()

        if "Order_Date" in df_cleaned.columns:
            df_cleaned["Order_Date"] = pd.to_datetime(df_cleaned["Order_Date"], errors="coerce")
            logging.info("Converted 'Order_Date' to datetime format.")

        return df_cleaned

    def handle_anomalies(self, df):
        """Remove rows with invalid (zero or negative) quantity or price values."""
        logging.info("Checking for anomalies (negative or invalid values)...")
        df_cleaned = df.copy()
        before = df_cleaned.shape[0]

        if "Quantity" in df_cleaned.columns:
            df_cleaned = df_cleaned[df_cleaned["Quantity"] > 0]

        if "Price_Per_Unit" in df_cleaned.columns:
            df_cleaned = df_cleaned[df_cleaned["Price_Per_Unit"] > 0]

        after = df_cleaned.shape[0]
        logging.info(f"Anomaly detection complete. Removed {before - after} invalid rows.")
        return df_cleaned