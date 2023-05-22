bal = 50
while bal > 0:
    print(f"Amount Due: {bal}")
    coin = int(input("Insert coin: "))
    bal = bal - coin

if bal < 0:
    bal *= 1
print(f"Change Owed: {-1*bal}")