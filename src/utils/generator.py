import random
from datetime import datetime, timedelta

categories = ["Food", "Travel", "Shopping", "Bills"]

def generate_fake_data(n=50):
    data = []

    for _ in range(n):
        category = random.choice(categories)
        amount = random.randint(50, 1000)

        random_days = random.randint(0, 30)
        date = datetime.now() - timedelta(days=random_days)
        date = date.strftime("%Y-%m-%d")

        data.append({
            "category": category,
            "amount": amount,
            "date": date
        })

    return data