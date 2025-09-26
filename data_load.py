import pandas as pd

# Load dataset
df = pd.read_csv("bank_transactions.csv")

# Look at the first 5 rows
print(df.head())

# Check rows and columns
print("Shape of dataset:", df.shape)

# Info about data types
print(df.info())

# Basic statistics
print(df.describe())
