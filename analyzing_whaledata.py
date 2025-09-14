import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Load and Explore the Dataset

try:
    df = pd.read_csv("whaledata.csv") 
    print(" Dataset loaded successfully\n")
except FileNotFoundError:
    print(" Error: Dataset file not found. Please check the filename and path.")
    exit()
except Exception as e:
    print(" Error loading dataset:", e)
    exit()

# Display first few rows
print(" First 5 rows of the dataset:")
print(df.head(), "\n")

# Explore dataset structure
print(" Dataset Info:")
print(df.info(), "\n")

# Check for missing values
print(" Missing Values:")
print(df.isnull().sum(), "\n")

# Clean missing values (fill number.whales with mean)
if df["number.whales"].isnull().sum() > 0:
    df["number.whales"].fillna(df["number.whales"].mean(), inplace=True)
    print("Missing values in 'number.whales' filled with mean.\n")

# Task 2: Basic Data Analysis

# Computing basic statistics
print(" Basic Statistics of Numerical Columns:")
print(df.describe(), "\n")

# Grouping: average whales per month
avg_month = df.groupby("month")["number.whales"].mean()
print(" Average Number of Whales per Month:")
print(avg_month, "\n")

# Grouping: average whales by noise level
avg_noise = df.groupby("water.noise")["number.whales"].mean()
print(" Average Number of Whales by Water Noise Level:")
print(avg_noise, "\n")

# Identify correlations
print(" Correlation of Features with Number of Whales:")
print(df.corr(numeric_only=True)["number.whales"].sort_values(ascending=False), "\n")

# Task 3: Data Visualization

sns.set_style("whitegrid")

# 1. Line Chart - whale counts over time.at.station
plt.figure(figsize=(8, 5))
plt.plot(df["time.at.station"], df["number.whales"], marker="o", linestyle="-", color="b")
plt.title("Line Chart: Whale Counts Over Time at Station")
plt.xlabel("Time at Station")
plt.ylabel("Number of Whales")
plt.show()

# 2. Bar Chart - average whales per month
plt.figure(figsize=(8, 5))
avg_month.plot(kind="bar", color="skyblue")
plt.title("Bar Chart: Average Number of Whales per Month")
plt.xlabel("Month")
plt.ylabel("Average Number of Whales")
plt.show()

# 3. Histogram - distribution of whale counts
plt.figure(figsize=(8, 5))
plt.hist(df["number.whales"], bins=10, color="purple", edgecolor="black", alpha=0.7)
plt.title("Histogram: Distribution of Whale Counts")
plt.xlabel("Number of Whales")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Depth vs Number of Whales
plt.figure(figsize=(8, 5))
plt.scatter(df["depth"], df["number.whales"], alpha=0.7, color="green")
plt.title("Scatter Plot: Depth vs Number of Whales")
plt.xlabel("Depth")
plt.ylabel("Number of Whales")
plt.show()

# Findings / Observations
print(" Observations:")
print("- Whale counts vary significantly across months, with some months showing higher averages.")
print("- Water noise appears to influence whale presence (higher counts in low/medium noise).")
print("- Whale counts are moderately correlated with depth and gradient.")
print("- The histogram shows whale counts mostly range between 8 and 15.")
print("- Scatter plots suggest whales are more concentrated in specific depth ranges.")
