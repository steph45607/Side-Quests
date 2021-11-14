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

for fruit in prices:
    print(fruit)
    print("Price:",prices[fruit])
    print("Stock:",stocks[fruit])
    print()

total = 0
for thing in prices:
    calc = prices[thing]*stocks[thing]
    print("{}:".format(thing),calc)
    total += calc

print()
print("Total:",total)