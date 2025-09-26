import pandas as pd


df = pd.read_csv("bank_transactions.csv")

import matplotlib.pyplot as plt
import seaborn as sns

# Fraud vs Non-Fraud
print(df["is_fraud"].value_counts())
sns.countplot(x="is_fraud", data=df)
plt.title("Fraud vs Non-Fraud")
plt.show()

# Amount distribution
if "amount" in df.columns:
    sns.histplot(df["amount"], bins=50)
    plt.title("Transaction Amount Distribution")
    plt.show()

    sns.boxplot(x="is_fraud", y="amount", data=df)
    plt.title("Amount by Fraud/Non-Fraud")
    plt.show()

# Correlation heatmap
corr = df.corr(numeric_only=True)
plt.figure(figsize=(10,6))
sns.heatmap(corr, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
