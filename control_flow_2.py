#calculate price of item after apppling the discount
def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount.

    Args:
        price: The original price of the item.
        discount_percent: The discount percentage.

    Returns:
        The final price after the discount, or the original price if the discount
        is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Get input from the user
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
    exit()  # Exit the program if input is invalid.

# Calculate the final price using the function
final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price == price:
    print("No discount applied. The original price is:", price)
else:
    print("The final price after applying the discount is:", final_price)

