import pandas as pd
import random
from datetime import datetime, timedelta
import uuid

transactions = []

locations = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Pune"
]

payment_types = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]

for i in range(1000):

    amount = round(random.uniform(100, 50000), 2)

    fraud_flag = random.choices(
        [0, 1],
        weights=[95, 5]
    )[0]

    transaction = {
        "transaction_id": str(uuid.uuid4())[:8],
        "timestamp": datetime.now() - timedelta(minutes=random.randint(1, 10000)),
        "location": random.choice(locations),
        "amount": amount,
        "payment_type": random.choice(payment_types),
        "fraud_flag": fraud_flag
    }

    transactions.append(transaction)

df = pd.DataFrame(transactions)

df.to_csv("pipeline/raw_transactions.csv", index=False)

print("Fake transaction data generated successfully!")