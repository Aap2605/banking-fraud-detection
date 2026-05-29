import pandas as pd

df = pd.read_csv("pipeline/raw_transactions.csv")

# Remove duplicate transactions
df.drop_duplicates(inplace=True)

# Remove negative amounts
df = df[df["amount"] > 0]

# Fill missing values
df.fillna("Unknown", inplace=True)

# Save cleaned data
df.to_csv("pipeline/clean_transactions.csv", index=False)

print("Transaction data cleaned successfully!")