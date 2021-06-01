prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78,
          48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

for val in prices:
    rub, kop = str(f"{val:.2f}").split(".")
    print(f" {rub} руб {int(kop):02} коп,", end=" ")

print(f"\n{'+' * 12} \n")
print(f"ID before: {id(prices)} - {prices}")
prices.sort()
print(f"ID after: {id(prices)} - {prices}")
print(prices)

prices_copy = prices.copy()
prices_copy.reverse()
print(prices_copy)
print(f"{prices_copy[:5]}")
