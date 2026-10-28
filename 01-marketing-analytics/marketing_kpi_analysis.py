# ============================================================
# Marketing KPI Analysis
# ============================================================
# Project Overview:
# This project analyzes simulated e-commerce marketing data to
# evaluate website traffic, campaign performance, and customer
# acquisition efficiency.
#
# Business Objectives:
# 1. Understand website traffic trends over time.
# 2. Compare ROAS across marketing channels.
# 3. Identify monthly changes in marketing performance.
# 4. Evaluate CTR and CAC across marketing campaigns.
# 5. Translate analytical findings into actionable insights.
#
# Tools: Python, Pandas, Matplotlib, Seaborn
# Dataset: Simulated marketing dataset containing 1,000 records
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# ------------------------------------------------------------
# 1. Configuration
# ------------------------------------------------------------

DATA_PATH = Path("data/marketing_data.csv")
OUTPUT_DIR = Path("outputs")
CHART_DIR = OUTPUT_DIR / "charts"
SUMMARY_DIR = OUTPUT_DIR / "summaries"

# Create output directories if they do not already exist.
CHART_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


# ------------------------------------------------------------
# 2. Load and Prepare Data
# ------------------------------------------------------------

def load_and_prepare_data(file_path: Path) -> pd.DataFrame:
    """
    Load the marketing dataset, standardize column names,
    and prepare the data for analysis.

    The original dataset uses Korean column names.
    These are mapped to English for a consistent,
    portfolio-ready analytical workflow.
    """

    df = pd.read_csv(file_path)

    # Map original Korean column names to English.
    column_mapping = {
        "날짜": "date",
        "마케팅 캠페인": "marketing_campaign",
        "방문자 수": "visitors",
        "페이지뷰 수": "page_views",
        "이탈률 (%)": "bounce_rate",
        "광고 수익률 (ROAS)": "roas",
        "클릭률 (%)": "ctr",
        "고객 획득 비용 (CAC)": "cac",
    }

    df = df.rename(columns=column_mapping)

    # Standardize column names in case the source file
    # already contains English column names.
    df.columns = df.columns.str.strip()

    # Confirm that all required columns are available.
    required_columns = list(column_mapping.values())
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}. "
            "Please check the column names in the source CSV."
        )

    # Convert the date column to datetime format.
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Remove rows with invalid dates.
    df = df.dropna(subset=["date"]).copy()

    # Convert KPI columns to numeric values.
    numeric_columns = [
        "visitors",
        "page_views",
        "bounce_rate",
        "roas",
        "ctr",
        "cac",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Derive time-based fields for trend analysis.
    df["year"] = df["date"].dt.year
    df["quarter"] = df["date"].dt.to_period("Q").astype(str)
    df["month"] = df["date"].dt.to_period("M").astype(str)

    print("Dataset loaded successfully.")
    print(f"Number of records: {len(df):,}")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")

    return df


# ------------------------------------------------------------
# 3. Exploratory Data Analysis
# ------------------------------------------------------------

def explore_data(df: pd.DataFrame) -> None:
    """
    Inspect the dataset structure and calculate
    descriptive statistics for the main marketing KPIs.
    """

    print("\n" + "=" * 60)
    print("EXPLORATORY DATA ANALYSIS")
    print("=" * 60)

    print("\nFirst Five Records:")
    print(df.head())

    print("\nDataset Information:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDescriptive Statistics:")
    print(
        df[
            [
                "visitors",
                "page_views",
                "bounce_rate",
                "roas",
                "ctr",
                "cac",
            ]
        ].describe().round(2)
    )


# ------------------------------------------------------------
# 4. Overall Website Performance
# ------------------------------------------------------------

def analyze_overall_performance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize the overall performance of the website
    using average traffic and engagement metrics.
    """

    overall_metrics = {
        "Average Visitors": df["visitors"].mean(),
        "Average Page Views": df["page_views"].mean(),
        "Average Bounce Rate (%)": df["bounce_rate"].mean(),
        "Average ROAS": df["roas"].mean(),
        "Average CTR (%)": df["ctr"].mean(),
        "Average CAC": df["cac"].mean(),
    }

    summary = pd.DataFrame(
        overall_metrics.items(),
        columns=["Metric", "Average Value"]
    )

    summary["Average Value"] = summary["Average Value"].round(2)

    print("\n" + "=" * 60)
    print("OVERALL WEBSITE PERFORMANCE")
    print("=" * 60)
    print(summary.to_string(index=False))

    summary.to_csv(
        SUMMARY_DIR / "overall_performance_summary.csv",
        index=False
    )

    return summary


# ------------------------------------------------------------
# 5. Website Traffic Trend Analysis
# ------------------------------------------------------------

def analyze_website_traffic(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze quarterly website traffic trends.

    Quarterly averages are used to examine changes in
    visitor volume and page views over time.
    """

    quarterly_traffic = (
        df.groupby("quarter")
        .agg(
            average_visitors=("visitors", "mean"),
            average_page_views=("page_views", "mean"),
        )
        .reset_index()
    )

    print("\nQuarterly Website Traffic:")
    print(quarterly_traffic.round(2).to_string(index=False))

    quarterly_traffic.to_csv(
        SUMMARY_DIR / "quarterly_traffic_summary.csv",
        index=False
    )

    # Plot quarterly visitor and page-view trends.
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=quarterly_traffic,
        x="quarter",
        y="average_visitors",
        marker="o",
        label="Average Visitors"
    )

    sns.lineplot(
        data=quarterly_traffic,
        x="quarter",
        y="average_page_views",
        marker="o",
        label="Average Page Views"
    )

    plt.title("Quarterly Website Traffic Trends")
    plt.xlabel("Quarter")
    plt.ylabel("Average Volume")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "quarterly_traffic_trends.png",
        dpi=300
    )
    plt.show()

    return quarterly_traffic


# ------------------------------------------------------------
# 6. Marketing Campaign Performance: ROAS
# ------------------------------------------------------------

def analyze_campaign_roas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compare average Return on Advertising Spend (ROAS)
    across marketing campaigns.

    A higher ROAS indicates more revenue generated
    per unit of advertising spend, assuming consistent
    metric definitions across campaigns.
    """

    campaign_roas = (
        df.groupby("marketing_campaign")["roas"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    campaign_roas.columns = [
        "marketing_campaign",
        "average_roas"
    ]

    print("\nAverage ROAS by Marketing Campaign:")
    print(campaign_roas.round(2).to_string(index=False))

    campaign_roas.to_csv(
        SUMMARY_DIR / "campaign_roas_summary.csv",
        index=False
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=campaign_roas,
        x="marketing_campaign",
        y="average_roas"
    )

    plt.title("Average ROAS by Marketing Campaign")
    plt.xlabel("Marketing Campaign")
    plt.ylabel("Average ROAS")
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "campaign_roas_comparison.png",
        dpi=300
    )
    plt.show()

    return campaign_roas


# ------------------------------------------------------------
# 7. Monthly ROAS Trend Analysis
# ------------------------------------------------------------

def analyze_monthly_roas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Examine monthly changes in average ROAS
    to identify periods of stronger or weaker
    advertising performance.
    """

    monthly_roas = (
        df.groupby("month")["roas"]
        .mean()
        .reset_index(name="average_roas")
    )

    print("\nMonthly ROAS Trends:")
    print(monthly_roas.round(2).to_string(index=False))

    monthly_roas.to_csv(
        SUMMARY_DIR / "monthly_roas_summary.csv",
        index=False
    )

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=monthly_roas,
        x="month",
        y="average_roas",
        marker="o"
    )

    plt.title("Monthly ROAS Trends")
    plt.xlabel("Month")
    plt.ylabel("Average ROAS")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "monthly_roas_trends.png",
        dpi=300
    )
    plt.show()

    return monthly_roas


# ------------------------------------------------------------
# 8. Click-Through Rate (CTR) Analysis
# ------------------------------------------------------------

def analyze_campaign_ctr(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compare average Click-Through Rate (CTR)
    across marketing campaigns.

    CTR represents the proportion of impressions
    that result in clicks. The source dataset provides
    CTR values but does not include raw click and
    impression counts for recalculating the rate.
    """

    campaign_ctr = (
        df.groupby("marketing_campaign")["ctr"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    campaign_ctr.columns = [
        "marketing_campaign",
        "average_ctr"
    ]

    print("\nAverage CTR by Marketing Campaign:")
    print(campaign_ctr.round(2).to_string(index=False))

    campaign_ctr.to_csv(
        SUMMARY_DIR / "campaign_ctr_summary.csv",
        index=False
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=campaign_ctr,
        x="marketing_campaign",
        y="average_ctr"
    )

    plt.title("Average CTR by Marketing Campaign")
    plt.xlabel("Marketing Campaign")
    plt.ylabel("Average CTR (%)")
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "campaign_ctr_comparison.png",
        dpi=300
    )
    plt.show()

    return campaign_ctr


# ------------------------------------------------------------
# 9. Customer Acquisition Cost (CAC) Analysis
# ------------------------------------------------------------

def analyze_campaign_cac(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compare the average Customer Acquisition Cost (CAC)
    across marketing campaigns.

    A lower CAC may indicate more cost-efficient customer
    acquisition, provided the campaigns use consistent
    definitions and measurement periods.
    """

    campaign_cac = (
        df.groupby("marketing_campaign")["cac"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    campaign_cac.columns = [
        "marketing_campaign",
        "average_cac"
    ]

    print("\nAverage CAC by Marketing Campaign:")
    print(campaign_cac.round(2).to_string(index=False))

    campaign_cac.to_csv(
        SUMMARY_DIR / "campaign_cac_summary.csv",
        index=False
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=campaign_cac,
        x="marketing_campaign",
        y="average_cac"
    )

    plt.title("Average CAC by Marketing Campaign")
    plt.xlabel("Marketing Campaign")
    plt.ylabel("Average CAC")
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "campaign_cac_comparison.png",
        dpi=300
    )
    plt.show()

    return campaign_cac


# ------------------------------------------------------------
# 10. Monthly CAC Trend Analysis
# ------------------------------------------------------------

def analyze_monthly_cac(df: pd.DataFrame) -> pd.DataFrame:
    """
    Track monthly average CAC to explore changes
    in customer acquisition efficiency over time.
    """

    monthly_cac = (
        df.groupby("month")["cac"]
        .mean()
        .reset_index(name="average_cac")
    )

    print("\nMonthly CAC Trends:")
    print(monthly_cac.round(2).to_string(index=False))

    monthly_cac.to_csv(
        SUMMARY_DIR / "monthly_cac_summary.csv",
        index=False
    )

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=monthly_cac,
        x="month",
        y="average_cac",
        marker="o"
    )

    plt.title("Monthly Customer Acquisition Cost Trends")
    plt.xlabel("Month")
    plt.ylabel("Average CAC")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "monthly_cac_trends.png",
        dpi=300
    )
    plt.show()

    return monthly_cac


# ------------------------------------------------------------
# 11. Business Insights and Recommendations
# ------------------------------------------------------------

def generate_business_insights(
    campaign_roas: pd.DataFrame,
    campaign_ctr: pd.DataFrame,
    campaign_cac: pd.DataFrame,
) -> None:
    """
    Translate campaign KPI comparisons into
    concise, data-driven business observations.

    The insights are based on observed rankings.
    They do not establish causal relationships.
    """

    print("\n" + "=" * 60)
    print("BUSINESS INSIGHTS AND RECOMMENDATIONS")
    print("=" * 60)

    # ROAS insight
    best_roas = campaign_roas.iloc[0]
    lowest_roas = campaign_roas.iloc[-1]

    print(
        f"\n1. ROAS Performance: "
        f"{best_roas['marketing_campaign']} has the highest "
        f"average ROAS ({best_roas['average_roas']:.2f}), "
        f"while {lowest_roas['marketing_campaign']} has "
        f"the lowest ({lowest_roas['average_roas']:.2f})."
    )

    print(
        "   Recommendation: Review campaign-level spending, "
        "targeting, and conversion performance before "
        "reallocating advertising budgets."
    )

    # CTR insight
    best_ctr = campaign_ctr.iloc[0]

    print(
        f"\n2. CTR Performance: "
        f"{best_ctr['marketing_campaign']} has the highest "
        f"average CTR ({best_ctr['average_ctr']:.2f})."
    )

    print(
        "   Recommendation: Examine its audience targeting, "
        "creative content, and messaging to identify "
        "potential practices worth testing in other campaigns."
    )

    # CAC insight
    lowest_cac = campaign_cac.sort_values(
        "average_cac",
        ascending=True
    ).iloc[0]

    highest_cac = campaign_cac.sort_values(
        "average_cac",
        ascending=False
    ).iloc[0]

    print(
        f"\n3. Customer Acquisition Cost: "
        f"{lowest_cac['marketing_campaign']} has the lowest "
        f"average CAC ({lowest_cac['average_cac']:.2f}), "
        f"while {highest_cac['marketing_campaign']} has "
        f"the highest ({highest_cac['average_cac']:.2f})."
    )

    print(
        "   Recommendation: Investigate differences in "
        "audience quality, conversion rates, and campaign "
        "spending to understand acquisition cost variation."
    )

    print(
        "\nNote: These comparisons are descriptive. "
        "Further analysis is required before making causal "
        "claims or final budget allocation decisions."
    )


# ------------------------------------------------------------
# 12. Main Workflow
# ------------------------------------------------------------

def main() -> None:
    """
    Run the complete marketing KPI analysis workflow.
    """

    # Step 1: Load and prepare the dataset.
    df = load_and_prepare_data(DATA_PATH)

    # Step 2: Inspect data quality and distributions.
    explore_data(df)

    # Step 3: Summarize overall website performance.
    analyze_overall_performance(df)

    # Step 4: Analyze website traffic trends.
    analyze_website_traffic(df)

    # Step 5: Compare ROAS across campaigns.
    campaign_roas = analyze_campaign_roas(df)

    # Step 6: Analyze monthly ROAS fluctuations.
    analyze_monthly_roas(df)

    # Step 7: Compare CTR across campaigns.
    campaign_ctr = analyze_campaign_ctr(df)

    # Step 8: Compare CAC across campaigns.
    campaign_cac = analyze_campaign_cac(df)

    # Step 9: Examine monthly CAC trends.
    analyze_monthly_cac(df)

    # Step 10: Summarize business implications.
    generate_business_insights(
        campaign_roas,
        campaign_ctr,
        campaign_cac,
    )

    print("\nAnalysis completed successfully.")
    print(f"Charts saved to: {CHART_DIR}")
    print(f"Summary tables saved to: {SUMMARY_DIR}")


if __name__ == "__main__":
    main()
