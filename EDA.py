import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("bank_transactions.csv")
# A histogram shows how transaction amounts are distributed. Each bar represents how many transactions fall
# into that range. Adding the KDE line helps visualize the curve of the distribution.
# plt.figure(figsize=(8, 5))
# sns.histplot(df["TransactionAmount"], bins=30, kde=True, color="blue")
# plt.title("Distribution of Transaction Amounts")
# plt.xlabel("Transaction Amount")
# plt.ylabel("Frequency")
# plt.show()

# A boxplot shows the spread of the transaction amounts. The box represents 
# the middle 50% of the data, the line inside
# is the median, and the dots outside are outliers. It’s useful for spotting unusually high or low amounts
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["TransactionAmount"], color="orange")
plt.title("Boxplot of Transaction Amounts")
plt.xlabel("Transaction Amount")
plt.show()

# A violin plot combines a boxplot with a density plot. Here, I used it to compare how customer
#  ages are distributed across Debit
#  and Credit transactions. The width of the violin shows how many people fall in that age range
plt.figure(figsize=(8, 5))
sns.violinplot(x="TransactionType", y="CustomerAge", data=df, palette="Set2")
plt.title("Distribution of Customer Age by Transaction Type")
plt.xlabel("Transaction Type")
plt.ylabel("Customer Age")
plt.show()
