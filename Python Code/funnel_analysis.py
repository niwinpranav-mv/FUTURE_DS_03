import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bank_marketing.csv", sep=';')

print(df.head())

print(df.isnull().sum())

df = df.dropna()

df['Converted'] = df['y'].map({
    'yes': 1,
    'no': 0
})

total_leads = df.shape[0]

converted_customers = df['Converted'].sum()

conversion_rate = (converted_customers / total_leads) * 100

print("----- KPI RESULTS -----")

print(f"Total Leads: {total_leads}")

print(f"Converted Customers: {converted_customers}")

print(f"Conversion Rate: {conversion_rate:.2f}%")

channel_performance = df.groupby('job')['Converted'].mean() * 100

print("\n----- CHANNEL PERFORMANCE -----")

print(channel_performance.sort_values(ascending=False))

campaign_performance = df.groupby('contact')['Converted'].mean() * 100

print("\n----- CAMPAIGN PERFORMANCE -----")

print(campaign_performance.sort_values(ascending=False))

monthly_conversion = df.groupby('month')['Converted'].mean() * 100

print("\n----- MONTHLY CONVERSION -----")

print(monthly_conversion)

plt.figure(figsize=(10,5))

channel_performance.sort_values().plot(kind='barh')

plt.title("Conversion Rate by Job Category")

plt.xlabel("Conversion Rate (%)")

plt.ylabel("Job Category")

plt.show()

plt.figure(figsize=(8,5))

campaign_performance.plot(kind='bar')

plt.title("Campaign Performance")

plt.xlabel("Contact Type")

plt.ylabel("Conversion Rate (%)")

plt.show()

plt.figure(figsize=(10,5))

monthly_conversion.plot(kind='line', marker='o')

plt.title("Monthly Conversion Trend")

plt.xlabel("Month")

plt.ylabel("Conversion Rate (%)")

plt.grid(True)

plt.show()

df.to_csv("cleaned_marketing_data.csv", index=False)

print("Cleaned dataset exported successfully!")