import random

items = []

for _ in range(1_000_000):
    obj = {"peso": random.randint(1, 15), "valor": random.randint(100, 1000)}
    items.append(obj)