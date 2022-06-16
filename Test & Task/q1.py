origin_price = float(input("Enter the original price : "))
discount = float(input("Enter the discount percentage : "))

print(f"Discounted price is : {origin_price * (1-discount)}")
print(f"Final price including GST is {1.28 * (origin_price * (1-discount))}")
