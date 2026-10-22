# Retail Sales & Profitability Analysis

An end-to-end exploratory data analysis (EDA) project investigating revenue drivers, discount effectiveness, sales channel performance, and operational health across 5,000 retail transactions.

## Project Overview

This project analyses an e-commerce retail dataset to understand what drives sales and profit, whether discounts improve order performance, which sales channels perform best, and whether delivery times are associated with customer satisfaction.

The analysis uses Python and its data analysis and visualization libraries to clean and validate the dataset, engineer useful features, explore business questions, and translate findings into practical recommendations.

## Business Questions

The project investigates four main business questions:

1. **Revenue Drivers:** Which product categories and regions contribute the most sales and profit? Does higher revenue necessarily indicate better profitability?
2. **Discount Impact:** How do discounts relate to quantity sold, profit, and profit margin? Do discount patterns differ by product category?
3. **Channel Performance:** How do the Website, Mobile App, and Marketplace compare in order volume, average order value, total profit, and profit margin?
4. **Operational Health:** What do delivery times reveal about operational performance? Is delivery speed associated with customer ratings, and do delivery times vary across regions?

## Tools & Technologies

- **Python** — data analysis and programming
- **Pandas** — data manipulation, cleaning, grouping, and aggregation
- **NumPy** — numerical operations and feature engineering
- **Matplotlib** — data visualization
- **Seaborn** — statistical visualizations
- **Jupyter Notebook** — interactive analysis and documentation

## Dataset

This project uses the **E-Commerce Business Analytics Dataset** from Kaggle.

**Source:** [E-Commerce Business Analytics Dataset](https://www.kaggle.com/datasets/mmumairkhattak/e-commerce-business-analytics-dataset)

The dataset contains 5,000 transactions and 21 original columns covering orders, customers, product categories, sales channels, discounts, profitability, delivery, and customer ratings.

### Download Instructions

1. Open the Kaggle dataset page linked above.
2. Download the dataset and extract the CSV file.
3. Place the CSV in the project's `data/` directory.
4. Ensure the filename is `ecommerce_business_analytics.csv`, or update the path in the notebook to match the downloaded filename.

The dataset is not included in this repository. Please follow the source's applicable terms and license when downloading or using it.
## Project Workflow

### 1. Data Understanding
- Inspected the dataset structure and data types.
- Reviewed descriptive statistics and categorical variables.
- Checked for missing values and duplicate records.

### 2. Data Cleaning & Validation
- Converted order dates to an appropriate datetime format.
- Optimized numeric and categorical data types.
- Investigated negative values and potential outliers.
- Validated the arithmetic relationships between gross sales, discounts, and net sales.
- Retained legitimate high-value transactions rather than removing outliers automatically.

### 3. Feature Engineering
Created additional features to support the analysis:

- `Month` — month extracted from the order date
- `Year` — year extracted from the order date
- `Profit_Margin` — profit as a percentage of net sales
- `Discount_Band` — discounts grouped into qualitative levels

### 4. Exploratory Data Analysis
Used grouped summaries, comparative charts, scatter plots, box plots, heatmaps, and correlation analysis to investigate the four business questions.

### 5. Insights & Recommendations
Summarized the findings, identified potential business actions, and documented the limitations of the dataset.

## Key Findings

### Revenue Drivers
- Fashion generated the highest total profit overall.
- Category leadership varied by region. Home & Kitchen and Electronics performed particularly well in the South.
- The relationship between sales and profit was very strong, but this was partly explained by the mathematical relationship between net sales, cost, and profit.

### Discount Impact
- Higher discounts were not associated with a meaningful increase in average quantity per order.
- Deeper discounts were associated with lower average profit margins overall.
- The relationship varied by category, making category-specific discount testing more appropriate than applying a single discount rule across all products.

### Channel Performance
- Website and Mobile App together accounted for approximately 84.8% of orders.
- The Website contributed the highest total profit.
- The Mobile App had a slightly higher profit margin than the Website.
- Marketplace performed below the other two channels on order volume, average order value, total profit, and profit margin.

### Operational Health
- Average delivery time was approximately 5.4 days.
- Delivery times were similar across regions.
- Delivery days and customer ratings showed virtually no correlation in this dataset, suggesting that delivery speed alone did not explain rating differences.

## Recommendations

Based on the exploratory findings:

1. Evaluate product-category performance by region instead of relying solely on national totals.
2. Test category-specific discount limits, particularly in categories where deeper discounts were associated with substantial margin reductions.
3. Investigate Marketplace fees, product assortment, and conversion performance before increasing investment in that channel.
4. Explore other possible drivers of customer satisfaction, such as product quality, price perception, and post-purchase support.
5. Compare results across order statuses and time periods before using the findings to make operational or financial decisions.

These recommendations are hypotheses for further investigation, not proof of causal effects.

## Limitations

- The dataset appears synthetic or curated, based on its unusually clean structure and patterns.
- Recorded profit may include cancelled or returned orders and should not automatically be interpreted as realised profit.
- Correlation does not establish causation.
- Some category-and-discount combinations may contain relatively few observations.
- The absence of a relationship between delivery time and customer ratings may reflect how the dataset was generated rather than real-world retail behaviour.

## Future Improvements

- Compare all transactions with delivered-only transactions.
- Analyse cancellation and return rates by channel and product category.
- Investigate whether category and regional patterns remain stable across years.
- Add confidence intervals or other statistical methods to assess uncertainty in discount comparisons.
- Incorporate return reasons, customer reviews, and support data to investigate customer satisfaction further.

## How to Run the Project

### Prerequisites

- Python 3.10 or later
- Jupyter Notebook
- The dataset used in the analysis

### Installation

1. Clone or download this repository.
2. Navigate to the project directory.
3. Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

4. Place the dataset in the expected location and update the notebook's file path if necessary.
5. Launch Jupyter Notebook:

```bash
jupyter notebook
```

6. Open the analysis notebook and run the cells from top to bottom.

## Author

**Abdul Wahab**

Aspiring Data Analyst | Python | Pandas | Data Visualization

