"""
Data export module for the Ecommerce Sales Analysis Pipeline.
Saves the cleaned and processed dataset to disk.
"""

import logging
import os


class DataExporter:
    """Exports the cleaned dataset to the project's data/cleaned directory."""

    def __init__(self):
        # This file lives at: Ecommerce_project/src/exporter.py
        # One directory up from src/ gives the project root.
        current_file_path = os.path.abspath(__file__)
        self.root_path = os.path.dirname(os.path.dirname(current_file_path))

        self.cleaned_dir = os.path.join(self.root_path, "data", "cleaned")
        self.processed_dir = os.path.join(self.root_path, "data", "processed")
        os.makedirs(self.cleaned_dir, exist_ok=True)
        os.makedirs(self.processed_dir, exist_ok=True)

    def export_cleaned_data(self, df):
        """Save the cleaned DataFrame (post-cleaning, pre-feature-engineering) to a CSV file."""
        output_path = os.path.join(self.cleaned_dir, "clean_sales_data.csv")
        df.to_csv(output_path, index=False)
        logging.info(f"Cleaned data exported to: {output_path}")

    def export_processed_data(self, df):
        """Save the feature-engineered DataFrame to the processed data directory."""
        output_path = os.path.join(self.processed_dir, "processed_sales_data.csv")
        df.to_csv(output_path, index=False)
        logging.info(f"Processed data exported to: {output_path}")