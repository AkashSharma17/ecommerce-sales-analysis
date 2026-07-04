"""
Visualization module for the Ecommerce Sales Analysis Pipeline.
Generates and saves charts summarizing sales performance.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os


class DataVisualizer:
    """Creates and saves visualizations from the processed sales dataset."""

    def __init__(self):
        # This file lives at: Ecommerce_project/src/visualizer.py
        # One directory up from src/ gives the project root.
        current_file_path = os.path.abspath(__file__)
        self.root_path = os.path.dirname(os.path.dirname(current_file_path))

        self.output_dir = os.path.join(self.root_path, "visualization")
        os.makedirs(self.output_dir, exist_ok=True)

    def top_product(self, df):
        """Plot and save a bar chart of the top 10 best-selling products."""
        logging.info("Generating top 10 selling products chart...")
        top_products = df.groupby("Product")["Quantity"].sum().nlargest(10)

        plt.figure(figsize=(10, 6))
        sns.barplot(
            x=top_products.values,
            y=top_products.index,
            hue=top_products.index,
            palette="viridis",
            legend=False,
        )
        plt.title("Top 10 Selling Products")
        plt.xlabel("Total Quantity Sold")
        plt.ylabel("Product Name")
        plt.tight_layout()

        save_path = os.path.join(self.output_dir, "top_products.png")
        plt.savefig(save_path)
        plt.close()
        logging.info(f"Top 10 selling products chart saved at: {save_path}")

    def monthly_sales_trend(self, df):
        """Plot and save a line chart of monthly sales trends."""
        logging.info("Generating monthly sales trend chart...")

        if "Order_Date" not in df.columns:
            logging.warning("'Order_Date' column missing. Monthly sales trend skipped.")
            return

        monthly_sales = df.groupby(df["Order_Date"].dt.to_period("M"))["Quantity"].sum()
        x_labels = monthly_sales.index.astype(str)
        x_positions = range(len(x_labels))

        plt.figure(figsize=(10, 6))
        plt.plot(
            x_positions,
            monthly_sales.values,
            marker="o",
            markersize=8,
            markerfacecolor="#2c5f8a",
            markeredgecolor="white",
            markeredgewidth=1.5,
            color="#3d7ab5",
            linewidth=2.5,
        )
        plt.fill_between(x_positions, monthly_sales.values, alpha=0.15, color="#3d7ab5")

        plt.title("Monthly Sales Trend", fontsize=14, fontweight="bold", pad=15)
        plt.xlabel("Month", fontsize=11)
        plt.ylabel("Total Quantity Sold", fontsize=11)
        plt.xticks(x_positions, x_labels, rotation=0, fontsize=10)
        plt.yticks(fontsize=10)

        ax = plt.gca()
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="y", linestyle="--", alpha=0.3)
        plt.tight_layout()

        save_path = os.path.join(self.output_dir, "monthly_sales_trend.png")
        plt.savefig(save_path)
        plt.close()
        logging.info(f"Monthly sales trend chart saved at: {save_path}")

    def sales_by_region(self, df):
        """Plot and save a pie chart of sales distribution by region."""
        logging.info("Generating sales by region chart...")

        if "Customer_Region" not in df.columns:
            logging.warning("'Customer_Region' column missing. Regional sales chart skipped.")
            return

        region_sales = df.groupby("Customer_Region")["Quantity"].sum().sort_values(ascending=False)

        colors = sns.color_palette("viridis", len(region_sales))

        plt.figure(figsize=(8, 8))
        wedges, texts, autotexts = plt.pie(
            region_sales.values,
            labels=region_sales.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            wedgeprops={"width": 0.45, "edgecolor": "white", "linewidth": 2},
            textprops={"fontsize": 11},
            pctdistance=0.8,
        )
        for autotext in autotexts:
            autotext.set_color("white")
            autotext.set_fontweight("bold")
            autotext.set_fontsize(10)

        plt.title("Sales Distribution by Region", fontsize=14, fontweight="bold", pad=15)
        plt.axis("equal")

        save_path = os.path.join(self.output_dir, "sales_by_region.png")
        plt.savefig(save_path)
        plt.close()
        logging.info(f"Sales by region chart saved at: {save_path}")

    def distribution_histogram(self, df):
        """Plot and save a histogram of order quantity distribution."""
        logging.info("Generating quantity distribution histogram...")

        if "Quantity" not in df.columns:
            logging.warning("'Quantity' column missing. Distribution histogram skipped.")
            return

        plt.figure(figsize=(10, 6))
        sns.histplot(df["Quantity"], kde=True, bins=15, color="#3d7ab5", edgecolor="white", linewidth=0.8)
        plt.title("Quantity Distribution", fontsize=14, fontweight="bold", pad=15)
        plt.xlabel("Quantity", fontsize=11)
        plt.ylabel("Frequency", fontsize=11)

        ax = plt.gca()
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="y", linestyle="--", alpha=0.3)

        save_path = os.path.join(self.output_dir, "quantity_distribution.png")
        plt.savefig(save_path)
        plt.close()
        logging.info(f"Distribution histogram saved at: {save_path}")