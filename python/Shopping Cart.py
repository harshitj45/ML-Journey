cart = ["Laptop", "Mouse", "Keyboard"]
prices = [75000, 800, 1500]

# Print cart with prices
print("Cart Items:")
for i in range(len(cart)):
    print(cart[i], ":", prices[i])

# Total
total = sum(prices)
print("Total:", total)

# Remove Mouse
cart.remove("Mouse")
prices.remove(800)

# New total
new_total = sum(prices)

# Print updated cart
print("\nUpdated Cart:")
for i in range(len(cart)):
    print(cart[i], ":", prices[i])

print("New Total:", new_total)