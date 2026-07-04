"""
Data loading module for the Ecommerce Sales Analysis Pipeline.
Handles reading the raw dataset from disk.
"""

import pandas as pd
import logging


class Loader:
    """Loads raw sales data from a CSV file into a DataFrame."""

    def __init__(self, file_path):
        self.filepath = file_path

    def load_data(self):
        """
        Read the CSV file at self.filepath.

        Returns:
            pd.DataFrame on success, or None if loading fails.
        """
        try:
            logging.info("Loading dataset...")
            df = pd.read_csv(self.filepath)
            logging.info("Dataset loaded successfully")
            logging.info(f"Dataset shape: {df.shape}")
            return df
        except Exception as e:
            logging.error(f"Error loading dataset: {e}")
            return None