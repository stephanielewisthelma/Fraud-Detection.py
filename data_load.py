import pandas as pd


df = pd.read_csv("bank_transactions.csv")


print(df.head())

print("Shape of dataset:", df.shape)

print(df.info())

print(df.describe())

#  Missing values
print(df.isnull().sum())

print("Duplicates:", df.duplicated().sum())


df = df.drop_duplicates()
