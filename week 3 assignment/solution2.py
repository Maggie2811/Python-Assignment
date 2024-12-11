# Using the calculate_discount function, prompt the user to enter the original price of an item 
# and the discount percentage. Print the final price after applying the discount, or
# if no discount was applied, print the original price.

def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user for the original price and discount percentage
original_price = float("100")
discount_percent = float("22")

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price == original_price:
    print(f"No discount was applied. The original price is: {original_price}")
else:
    print(f"The final price after applying the {discount_percent}% discount is: {final_price}")