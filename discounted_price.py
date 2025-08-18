def calculate_discount(price, discount_percent):
    # if discount is applied
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # No discount applied
        return price


# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Discount applied! The final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {final_price:.2f}")
