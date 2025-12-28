import pandas as pd

weekly_file = "apple.csv"


# 1. Load your CSV file
# Replace 'your_data.csv' with the actual filename
df = pd.read_csv(weekly_file)

# 2. Clean 'Date' and convert to datetime objects
# This handles the "Dec 26, 2025" format
df["Date"] = pd.to_datetime(df["Date"].str.strip())

# 3. Sort by date ascending to ensure we correctly identify the start/end of the week
df = df.sort_values("Date")

# 4. Define the Week period (starts on Monday)
df["Week_ID"] = df["Date"].dt.to_period("W").apply(lambda r: r.start_time)

# 5. Group by week to find the First Open and Last Close
weekly_stats = df.groupby("Week_ID").agg(
    Week_Open=("Open", "first"), Week_Close=("Close", "last")
)

# 6. Calculate the Percentage Change: (Close - Open) / Open
weekly_stats["Weekly Price Change %"] = (
    (weekly_stats["Week_Close"] - weekly_stats["Week_Open"]) / weekly_stats["Week_Open"]
) * 100

# 7. Merge the results back to the original rows
df = df.merge(
    weekly_stats[["Weekly Price Change %"]], left_on="Week_ID", right_index=True
)

# 8. Clean up and save to a new CSV
df_final = df.drop(columns=["Week_ID"]).sort_values("Date", ascending=False)
df_final.to_csv("weekly_" + weekly_file, index=False)

print("Processing complete. Created 'weekly_analysis_output.csv'.")


print(df.head())
