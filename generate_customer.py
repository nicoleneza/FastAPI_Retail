import csv
import random
from faker import Faker
from datetime import datetime, timedelta
from tabulate import tabulate

fake = Faker()
num_customers = 50000

customers = [
    {
        "Customer ID": f"CUST-{i+1:04d}",
        "Customer Name": fake.name(),
        "Customer Address": fake.address(),
        "Email": fake.email(),
        "Phone": fake.phone(),
    }
    for i in range(num_customers)
]

customers_file = "customer.csv"
with open(customers_file, mode="w", newline="",encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,fieldnames=["Customer ID","Customer Name","Customer Address","Email","Phone"]
    )
    writer.writeheader()
    writer.writerows(customers)

print(f"Dataset with {num_customers} records saved to {customers_file}")