"""
Byu-Idaho Online 
CSE-111 Programming with Functions
W01 Individual Activity: Discount
Author: Tiago Borges 


Program: Discount Calculator for Retail Store

This program calculates the total amount a customer needs to pay, applying a 10% discount on Tuesdays and Wednesdays if
 the subtotal is $50 or more.  The program automatically retrieves the current day from the system and applies a 6% sales 
 tax to the final amount.

Challenges and Bug Fixes:
- Initially, the discount logic was not applying correctly on Tuesdays and Wednesdays, so I added print statements for 
debugging and verified the day retrieval using `datetime.weekday()`.- Another issue was rounding errors in floating-point
 calculations. To fix this, I used Python's `round()` function for better precision.- I also encountered user input errors,
 so I implemented exception handling to ensure valid numerical input.

Lessons Learned:
- Understanding how to retrieve and use system date/time in Python
- Importance of debugging using print statements and testing edge cases
- Managing floating-point precision and improving user input handling

"""

# Let´s do it! 


from datetime import datetime

def calculate_discount(subtotal, day_of_week):
    discount = 0
    if day_of_week in [1, 2] and subtotal >= 50:  # Tuesday (1) or Wednesday (2)
        discount = subtotal * 0.10
    return discount

def calculate_sales_tax(subtotal, tax_rate=0.06):
    return subtotal * tax_rate

def main():
    try:
        subtotal = float(input("Please enter the subtotal: "))
        if subtotal < 0:
            print("Subtotal cannot be negative.")
            return
        
        current_date_and_time = datetime.now()
        day_of_week = current_date_and_time.weekday()
        
        discount = calculate_discount(subtotal, day_of_week)
        subtotal_after_discount = subtotal - discount
        sales_tax = calculate_sales_tax(subtotal_after_discount)
        total = subtotal_after_discount + sales_tax
        
        if discount > 0:
            print(f"Discount amount: {discount:.2f}")
        print(f"Sales tax amount: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()

# Final Thoughts:
#  This project helped me practice handling user input, working with dates, and applying conditional logic efficiently
#  It reinforced the importance of debugging and testing under different scenarios. Additionally, handling floating-point
#  precision issues gave me insights into best practices for financial calculations in Python

