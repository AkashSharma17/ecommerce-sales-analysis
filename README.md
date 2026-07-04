# Ecommerce Sales Analysis Pipeline

An end-to-end data analytics pipeline that processes raw ecommerce order data to deliver business KPIs, cleaned datasets, and visual insights.

---

## Project Overview

This pipeline automates the full analytics lifecycle for ecommerce sales data:

- Data ingestion and validation
- Cleaning (duplicates, missing values, data types, anomalies)
- Feature engineering (revenue, monthly and yearly breakdowns)
- Business metrics and KPI calculation
- Automated chart generation
- Export of cleaned and processed datasets separately for traceability

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core runtime |
| Pandas | Data manipulation and analysis |
| Matplotlib | Chart generation |
| Seaborn | Statistical visualization |

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/AkashSharma17/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis

# Create and activate a virtual environment
python -m venv venv
source .venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Run the Pipeline

```bash
python main.py
```

---

## Project Structure

```
Ecommerce_project/
├── main/
│   └── main.py                  # Pipeline orchestrator
├── src/
│   ├── logger.py                # Logging configuration
│   ├── loader.py                # Data ingestion
│   ├── data_cleaner.py          # Cleaning and validation
│   ├── feature_engineering.py   # Derived metrics
│   ├── data_analyzer.py         # Business KPI computation
│   ├── visualizer.py            # Chart generation
│   └── exporter.py              # Data export
├── data/
│   ├── raw/                     # Original input data
│   ├── cleaned/                 # Post-cleaning dataset
│   └── processed/               # Feature-engineered dataset
├── visualization/               # Generated charts (PNG)
├── logs/                        # Execution logs
├── setup_project.py             # One-time folder structure initializer
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Input Data Format

The pipeline expects a CSV file at `data/raw/raw_data.csv` with the following columns:

| Column | Format | Description |
|--------|--------|-------------|
| `Order_ID` | Integer | Unique order identifier |
| `Product` | String | Product name |
| `Quantity` | Float | Units ordered |
| `Price_Per_Unit` | Float | Unit selling price |
| `Order_Date` | `YYYY-MM-DD` | Date of order |
| `Customer_Region` | String | Customer region |

---

## Generated Outputs

### Business Metrics & KPIs
- Total revenue across all orders
- Top 5 selling products by quantity
- Sales and order volume by region
- Monthly sales trend
- Highest revenue-generating product

### Charts
- **Top 10 Selling Products** — Horizontal bar chart
- **Monthly Sales Trend** — Line chart with filled area
- **Sales Distribution by Region** — Donut chart
- **Quantity Distribution** — Histogram with KDE

### Exported Datasets
- `data/cleaned/clean_sales_data.csv` — Cleaned dataset before feature engineering
- `data/processed/processed_sales_data.csv` — Final dataset with engineered features

---

## Skills & Concepts Covered

| Area | Details |
|------|---------|
| **Data Engineering** | End-to-end pipeline from raw ingestion to structured output |
| **Data Cleaning** | Null handling, type normalization, duplicate and anomaly removal |
| **Feature Engineering** | Deriving revenue, month, and year from transactional fields |
| **Business Intelligence** | KPI computation across products, regions, and time periods |
| **Data Visualization** | Professional chart design using Matplotlib and Seaborn |
| **Logging** | Dual-handler logging to file and console |
| **Project Architecture** | Modular, production-style Python project organization |

---

## Author

**Akash Sharma**
GitHub: [@AkashSharma17](https://github.com/AkashSharma17)

---

## License

This project is open source and available under the [MIT License](LICENSE).