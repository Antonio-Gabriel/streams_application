import random
from faker import Faker
from random_date import random_date

faker = Faker()

transactions_faker = [
    {
        "id": index,
        "amount": random.randint(100, int(1e9)),
        "date": random_date("1/1/2014 1:30 PM", "1/1/2022 4:40 AM", random.random())
    } for index in range(1, 20)
]
