# Marketing Analytics with Python

## Project Overview

This project explores marketing performance measurement through two stages: basic marketing metric calculations and applied analysis of simulated marketing data.

Using Python, the project examines website traffic, conversion performance, advertising efficiency, and customer acquisition costs. The goal is to develop practical data analysis skills and understand how marketing KPIs can support business decision-making.

**Note:** All datasets used in this project are illustrative or simulated. They do not represent verified performance data from a real company or actual marketing campaigns.

## Project Structure

### 1. Basic Marketing Metrics — `marketing_metrics.py`

Introduces fundamental marketing KPIs through hardcoded sample data.

**Focus areas:**
- Exploring website traffic using visitors and page views
- Examining advertising spend and conversion rates
- Calculating Return on Advertising Spend (ROAS)
- Practicing basic metric calculations and visualizations

The sample dataset contains five dates and is intended for learning purposes rather than reliable trend analysis.

### 2. Applied Marketing KPI Analysis — `marketing_kpi_analysis.py`

Extends the basic exercises by analyzing a simulated marketing dataset containing 1,000 records.

**Focus areas:**
- Data preparation and exploratory data analysis
- Quarterly website traffic trends
- Marketing campaign ROAS comparisons
- Monthly ROAS fluctuations
- Campaign-level Click-Through Rate (CTR) comparisons
- Customer Acquisition Cost (CAC) analysis
- Business insights and marketing recommendations

The original Korean column names are mapped to English to support a consistent analytical workflow.

## Business Objectives

- Understand website traffic patterns over time.
- Evaluate marketing campaign performance using multiple KPIs.
- Compare advertising returns and customer acquisition costs across campaigns.
- Identify performance patterns that warrant further investigation.
- Translate analytical findings into potential business recommendations.

## Tools & Technologies

- **Python** — Data analysis and visualization
- **Pandas** — Data preparation, aggregation, and descriptive statistics
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Jupyter Notebook / Google Colab** — Basic metric exercises

## Key Performance Indicators

| KPI | Definition | Business Purpose |
|---|---|---|
| Website Visitors | Number of website visitors | Measure traffic volume |
| Page Views | Number of pages viewed | Understand browsing activity |
| Conversion Rate | Percentage of eligible visitors or sessions completing a defined conversion action | Evaluate conversion performance |
| Bounce Rate | Percentage of visits meeting the dataset's bounce definition | Examine website engagement |
| ROAS | Advertising-attributed revenue divided by advertising spend | Evaluate advertising returns |
| CTR | Clicks divided by impressions | Measure advertising engagement |
| CAC | Customer acquisition costs divided by new customers acquired | Assess acquisition efficiency |

*Note: The applied dataset provides KPI values directly. The definitions above describe the general metrics; the underlying raw data needed to independently recalculate every metric is not necessarily available.*

## Analysis Workflow

### 1. Basic Metric Calculations

- Create and inspect illustrative sample data.
- Calculate and visualize basic marketing metrics.
- Explore how advertising spend and conversion rates can be interpreted together.
- Calculate ROAS using revenue and advertising spend.

### 2. Data Preparation and Exploratory Analysis

- Load and inspect the simulated marketing dataset.
- Standardize column names and data types.
- Check missing values and descriptive statistics.
- Prepare date-based variables for time-series analysis.

### 3. Website Traffic Analysis

- Examine quarterly trends in visitors and page views.
- Compare traffic patterns across periods.

### 4. Campaign Performance Analysis

- Compare average ROAS across marketing campaigns.
- Evaluate differences in CTR and CAC across channels.
- Identify campaigns with relatively stronger or weaker KPI performance.

### 5. Monthly Trend Analysis

- Track monthly changes in ROAS.
- Examine monthly fluctuations in CAC.
- Identify periods that may require additional investigation.

### 6. Business Interpretation

- Summarize differences in marketing performance.
- Identify potential areas for campaign optimization.
- Develop recommendations for further analysis and marketing decisions.

## How to Run

### Prerequisites

Install Python and the required libraries:

```bash
pip install pandas matplotlib seaborn
```

### Basic Metrics

Run `marketing_metrics.py` in your preferred Python environment, such as Jupyter Notebook or Google Colab. This script uses hardcoded sample data.

### Applied KPI Analysis

**1. Prepare the dataset**

Place the simulated CSV file in the following location:

```text
01-marketing-analytics/
├── README.md
├── marketing_metrics.py
├── marketing_kpi_analysis.py
├── requirements.txt
└── data/
    └── marketing_data.csv
```

The CSV must contain the expected fields documented in the analysis code. The script supports the original Korean column names and their mapped English equivalents.

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the analysis**

From the `01-marketing-analytics` directory, run:

```bash
python marketing_kpi_analysis.py
```

The script is configured to save charts and summary tables in an `outputs/` directory.

## Limitations

- Both datasets are illustrative or simulated and do not represent verified real-world marketing performance.
- The five-date sample in the basic exercise is insufficient for reliable trend analysis.
- The applied analysis uses descriptive statistics and does not establish causal relationships.
- Average CTR may differ from a properly weighted campaign CTR calculated using total clicks and impressions.
- Average CAC may differ from a correctly calculated acquisition cost based on total spending and new customers acquired.
- ROAS measures advertising-attributed revenue relative to advertising spend; it does not necessarily represent overall profitability.
- More detailed data would be needed to validate findings and support stronger business recommendations.

## Future Improvements

- Calculate weighted CTR from raw click and impression counts.
- Calculate CAC from total acquisition spending and new-customer counts.
- Incorporate customer-level data to explore retention and customer behavior.
- Compare campaign performance using a larger and more representative dataset.
- Build an interactive marketing performance dashboard using Power BI or Tableau.
- Apply statistical testing to investigate whether observed differences are meaningful.

## Author

**Seul Lee**

GitHub: [leeseul0525](https://github.com/leeseul0525)

This project is part of my ongoing learning in data analytics, marketing performance measurement, and business-oriented decision-making.
