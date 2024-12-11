# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a 
# discount. The function should take the original price (price) and the discount percentage (discount_percent) 
# as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price. 

def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # Return the original price if the discount is less than 20%
        return price

original_price = 100
discount = 25
# discount = 8
final_price = calculate_discount(original_price, discount)
print(f"The final price after a {discount}% discount is: {final_price}")  
