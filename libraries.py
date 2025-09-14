import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1: Create an array from 1 to 10 and calculate the mean
arr = np.arange(1, 11)  
mean_val = np.mean(arr)
print("NumPy Array:", arr)
print("Mean of Array:", mean_val)

# 2: Create a small dataset and display summary statistics
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "Score": [88, 92, 79, 95]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())

# 3: Fetch data from a public API
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if response.status_code == 200:
    todo_data = response.json()
    print("\nFetched Todo Title:", todo_data["title"])
else:
    print("\nFailed to fetch data from API")

# 4: Simple line graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker='o')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
