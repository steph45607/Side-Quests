prices = {
    "Banana":4,
    "Apple":2,
    "Orange":1.5,
    "Pear":3
}

stocks = {
    "Banana":6,
    "Apple":0,
    "Orange":32,
    "Pear":15
}


Groceries = ["Banana", "Pear", "Orange"]


def compute_bill(food):
    total = 0
    for i in food:
        if stocks[i] > 0:
            total += prices[i]
            stocks[i] -= 1
    return total

print(compute_bill(Groceries))