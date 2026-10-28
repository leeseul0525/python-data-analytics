
# Marketing Analytics: Traffic, Conversion, and ROAS
# Note: This project uses illustrative, hardcoded sample data.

import pandas as pd
import matplotlib.pyplot as plt

# 1. Website traffic analysis
traffic_data = {
    "Date": [
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-04",
        "2025-01-05",
    ],
    "Campaign": ["A", "A", "B", "B", "A"],
    "Visitors": [5000, 5200, 7000, 6800, 5500],
    "Page_Views": [12000, 13000, 18000, 17500, 12500],
}

traffic_df = pd.DataFrame(traffic_data)

print("Website Traffic Data")
display(traffic_df)

# Visualize visitors and page views over time
plt.figure(figsize=(9, 5))
plt.plot(
    traffic_df["Date"],
    traffic_df["Visitors"],
    label="Visitors",
    marker="o",
)
plt.plot(
    traffic_df["Date"],
    traffic_df["Page_Views"],
    label="Page Views",
    marker="s",
)
plt.xlabel("Date")
plt.ylabel("Count")
plt.title("Website Traffic: Visitors vs. Page Views")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 2. Conversion analysis
conversion_data = {
    "Date": [
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-04",
        "2025-01-05",
    ],
    "Ad_Spend_USD": [1000, 2000, 1500, 2500, 3000],
    "Conversion_Rate_Pct": [2.5, 3.8, 3.0, 4.5, 5.2],
}

conversion_df = pd.DataFrame(conversion_data)

print("Conversion and Advertising Data")
display(conversion_df)

# Explore the relationship between ad spend and conversion rate
plt.figure(figsize=(8, 5))
plt.scatter(
    conversion_df["Ad_Spend_USD"],
    conversion_df["Conversion_Rate_Pct"],
    alpha=0.7,
)
plt.xlabel("Advertising Spend (USD)")
plt.ylabel("Conversion Rate (%)")
plt.title("Advertising Spend vs. Conversion Rate")
plt.tight_layout()
plt.show()

# 3. Return on ad spend (ROAS)
roas_data = {
    "Date": [
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-04",
        "2025-01-05",
    ],
    "Ad_Spend_USD": [1000, 2000, 3000, 4000, 5000],
    "Revenue_USD": [5000, 9000, 14000, 18000, 22000],
}

roas_df = pd.DataFrame(roas_data)

# Calculate ROAS as revenue divided by advertising spend
roas_df["ROAS"] = (
    roas_df["Revenue_USD"] / roas_df["Ad_Spend_USD"]
).round(2)

print("Return on Ad Spend (ROAS)")
display(roas_df)

plt.figure(figsize=(8, 5))
plt.plot(
    roas_df["Ad_Spend_USD"],
    roas_df["ROAS"],
    marker="o",
)
plt.xlabel("Advertising Spend (USD)")
plt.ylabel("ROAS (Revenue / Ad Spend)")
plt.title("Advertising Spend vs. ROAS")
plt.tight_layout()
plt.show()
