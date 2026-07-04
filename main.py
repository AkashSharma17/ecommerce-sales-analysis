"""
Main pipeline orchestrator for the Ecommerce Sales Analysis Pipeline.
Runs the full workflow: load, clean, engineer features, analyze, visualize, and export.
"""

import sys
import os

# This file lives at: Ecommerce_project/main/main.py
# One directory up from main/ gives the project root (Ecommerce_project).
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir   

sys.path.insert(0, project_root)

data_file_path = os.path.join(project_root, "data", "raw", "raw_data.csv")

import logging
from src.logger import LoggerSetup
from src.loader import Loader
from src.data_cleaner import DataCleaner
from src.exporter import DataExporter
from src.feature_engineering import FeatureEngineer
from src.data_analyzer import DataAnalyzer
from src.visualizer import DataVisualizer


def run_pipeline():
    """Execute the full ecommerce sales analysis pipeline end to end."""

    LoggerSetup.setup_logger()
    logging.info("Starting Ecommerce Sales Analysis Pipeline...")

    try:
        # Data Loading
        loader = Loader(data_file_path)
        df = loader.load_data()

        if df is None or df.empty:
            logging.error("Pipeline stopped: Dataframe is empty or could not be loaded.")
            print("\n[ERROR] Data could not be loaded. Check the logs for details.")
            sys.exit(1)

        # Cleaning Pipeline
        cleaner = DataCleaner()
        cleaner.dataset_info(df)
        df = cleaner.remove_duplicates(df)
        df = cleaner.fix_data_types(df)
        df = cleaner.handle_missing_values(df)
        df = cleaner.handle_anomalies(df)

        # Export Cleaned Data (before feature engineering)
        exporter = DataExporter()
        exporter.export_cleaned_data(df)

        # Feature Engineering
        feature_engineer = FeatureEngineer()
        df = feature_engineer.feature_engineering(df)

        # Data Analysis
        analyzer = DataAnalyzer(df)
        print("\n=== BUSINESS METRICS & KPIs ===")
        print(f"Total Revenue: {analyzer.total_revenue()}")
        print("\nTop Selling Products:\n", analyzer.top_selling_product())
        print("\nMost Profitable Region:\n", analyzer.profitable_region())
        print("\nMonthly Sales Trend:\n", analyzer.monthly_sales_trend())
        print("\nTotal Quantity Sold by Product:\n", analyzer.sold_quantity_by_product())
        print("\nHighest Revenue Generating Product:\n", analyzer.highest_revenue_by_product())
        print("\nTotal Orders by Region:\n", analyzer.total_orders_by_region())

        # Visualization
        logging.info("Generating visualizations...")
        visualizer = DataVisualizer()
        visualizer.top_product(df)
        visualizer.monthly_sales_trend(df)
        visualizer.sales_by_region(df)
        visualizer.distribution_histogram(df)

        # Export Processed (feature-engineered) Data
        exporter.export_processed_data(df)

        logging.info("Pipeline execution completed successfully!")

    except Exception as e:
        logging.error(f"Pipeline crashed due to an error: {str(e)}", exc_info=True)
        print(f"\n[ERROR] Pipeline failed: {e}")


if __name__ == "__main__":
    run_pipeline()