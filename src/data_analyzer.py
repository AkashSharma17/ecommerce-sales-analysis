"""
Data analysis module for the Ecommerce Sales Analysis Pipeline.
Computes key business metrics from the processed sales dataset.
"""

import pandas as pd
import logging


class DataAnalyzer:
    """Performs statistical and business analysis on the sales dataset."""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        logging.info("DataAnalyzer initialized with cleaned dataset.")

    def total_revenue(self):
        """Calculate total revenue across all orders."""
        if "Total_Sales" in self.df.columns:
            return self.df["Total_Sales"].sum()
        elif "Quantity" in self.df.columns and "Price_Per_Unit" in self.df.columns:
            return (self.df["Quantity"] * self.df["Price_Per_Unit"]).sum()
        return 0

    def top_selling_product(self):
        """Return the top 5 products by total quantity sold."""
        return self.df.groupby("Product")["Quantity"].sum().nlargest(5)

    def profitable_region(self):
        """Return total quantity sold per customer region."""
        return self.df.groupby("Customer_Region")["Total_Sales"].sum()

    def monthly_sales_trend(self):
        """Return the number of orders placed per month."""
        return self.df.groupby(self.df["Order_Date"].dt.to_period("M"))["Quantity"].count()

    def sold_quantity_by_product(self):
        """Return total quantity sold per product."""
        return self.df.groupby("Product")["Quantity"].sum()

    def highest_revenue_by_product(self):
        """Return the single product generating the highest total revenue."""
        if "Total_Sales" in self.df.columns:
            return self.df.groupby("Product")["Total_Sales"].sum().nlargest(1)
        return "Total_Sales column missing"

    def total_orders_by_region(self):
        """Return the total number of orders placed per customer region."""
        return self.df.groupby("Customer_Region")["Order_ID"].count()