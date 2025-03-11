"""
(BSc) Software Development at Byu-Idaho  
Course: CSE-111 Programming with Functions
W01 Project: Tire Volume - Milestone
Author: Tiago Borges 
"""

#Let´s create the program! 

import math

# Ask for user input
width = float(input("Enter the width of the tire in mm (ex. 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex. 60): "))
diameter = float(input("Enter the diameter of the wheel in inches(ex. 15): "))

# Tire volume formula
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000_000

# Display the formatted result
print(f"The approximate volume is {volume:.2f} liters")


# Done!
