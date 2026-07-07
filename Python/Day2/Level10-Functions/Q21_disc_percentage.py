try:
    # Function to calculate final price after discount
    def final_price(price,discount=10):
        # Calculate discount price
        return price - (price*discount/100)

    # Test cases
    print(final_price(100))
    print(final_price(100,20))
    
except TypeError:
    print("Invalid input: price and discount must be numbers.")

except Exception as e:
    print(f"Unexpected error: {e}")