from datetime import date
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

median_age = df["Age"].median()
df["Age"].fillna(median_age, inplace=True)

print("\nMissing ages have been replaced with the median:", median_age)


