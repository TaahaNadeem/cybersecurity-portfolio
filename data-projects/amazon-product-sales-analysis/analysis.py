# Amazon Product Sales – Mini Data Analysis
# Built to practise basic data analysis skills for Data Analyst / Cyber roles.

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("dataset.csv")

# Make sure Date is treated as a real date, not just text
df["Date"] = pd.to_datetime(df["Date"])

# 2. Create a Revenue column
df["Revenue"] = df["Price"] * df["Units_Sold"]

print("First few rows of the dataset with Revenue column added:")
print(df.head())
print("\n")

# 3. Top products by revenue
top_products = df.sort_values(by="Revenue", ascending=False)[
    ["Product", "Category", "Revenue", "Units_Sold", "Price"]
]

print("Top products by revenue:")
print(top_products.to_string(index=False))
print("\n")

# 4. Revenue by category
category_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("Revenue by category:")
print(category_revenue)
print("\n")

# Bar chart: revenue by category
plt.figure()
category_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue (£)")
plt.tight_layout()
plt.savefig("plots/revenue_by_category.png")  # save chart for GitHub
plt.show()

# 5. Revenue by month (using the Date column)
monthly_revenue = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()

print("Revenue by month:")
print(monthly_revenue)
print("\n")

# Line chart: revenue over time
monthly_revenue_indexed = monthly_revenue.copy()
monthly_revenue_indexed.index = monthly_revenue_indexed.index.to_timestamp()

plt.figure()
monthly_revenue_indexed.plot(marker="o")
plt.title("Revenue Over Time")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.tight_layout()
plt.savefig("plots/revenue_over_time.png")  # save chart for GitHub
plt.show()

# 6. Simple text summary / mini report
total_revenue = df["Revenue"].sum()
best_product_row = df.loc[df["Revenue"].idxmax()]
best_product = best_product_row["Product"]
best_product_revenue = best_product_row["Revenue"]

best_category = category_revenue.idxmax()
best_category_revenue = category_revenue.max()

print("Quick insights:")
print(f"- Total revenue in this dataset: £{total_revenue:.2f}")
print(f"- Best-selling product by revenue: {best_product} (about £{best_product_revenue:.2f})")
print(f"- Best-performing category by revenue: {best_category} (about £{best_category_revenue:.2f})")
