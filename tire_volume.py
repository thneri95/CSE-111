"""
(BSc) Software Development at Byu-Idaho  
Course: CSE-111 Programming with Functions
W01 Project: Tire Volume - Final
Author: Tiago Borges 

About the Program: 
This program calculates the air volume inside a tire based on user input for width, aspect ratio, and wheel diameter
It saves this data, along with the date, in volumes.txt and checks for predefined tire prices.
If available, the user is given the option to purchase the tires, and their phone number is stored if they choose to buy.

Challenges:
Key challenges included ensuring accurate calculations, managing file operations without overwriting data, 
and handling user interactions with validation and pricing logic

"""

# How It Works:
# The user enters tire specifications
# The program calculates the tire volume
# It checks for a matching tire price
# If the user wants to buy, it collects their phone number
# The data is saved to volumes.txt with a confirmation message

#Let´s do it!

from datetime import datetime
import math

# Predefined tire prices based on size
tire_prices = {
    (185, 50, 14): 80.99,
    (195, 55, 15): 95.50,
    (205, 60, 15): 110.75,
    (215, 65, 16): 125.00
}

# Ask for user input
width = int(input("Enter the width of the tire in mm (ex. 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex. 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex. 15): "))

# Tire volume formula
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000_000

# Display the formatted result
print(f"\nThe approximate volume is {volume:.2f} liters")

# Check for tire price
price = tire_prices.get((width, aspect_ratio, diameter), None)
if price:
    print(f"The price for this tire size is ${price:.2f}")
else:   
    print("Sorry, we don't have a price listed for this tire size.")

# Ask if the user wants to buy
buy_tire = input("\nWould you like to buy these tires? (yes/no): ").strip().lower()

phone_number = ""
if buy_tire == "yes":
    phone_number = input("Please enter your phone number: ")
    print("Thank you! We will contact you soon.")

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Append data to volumes.txt
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}")
    if phone_number:
        file.write(f", {phone_number}")
    file.write("\n")

print("\nData has been saved to volumes.txt")


"""
Through this project I improved my skills in file handling, user input validation, and conditional logic
 I learned how to correctly apply mathematical formulas in Python, manage data persistence using files, 
 and enhance user interaction by offering purchase options.

"""
# Bonus:
# To exceed requirements: I added a feature that checks predefined tire prices and allows users to purchase tires,
# storing their phone numbers if they agree. This enhancement improves real-world applicability and makes the program
# more engaging and practical.

# Thanks for your support and time to review my program
# May Heavenly Father bless you with wisdom, patience and joy in all that you do!