"""
Byu-Idaho  
CSE-111 Programming with Functions
W05 Project- Grocery Store - Final
Author: Tiago Borges 

About program

Main Functionality>>>  The program simulates a grocery store receipt generator, reading product data from a CSV file and
 processing the customer’s order to calculate the total price, including sales tax.

Program Workflow: The program loads product data, processes the order, applies discounts if needed and prints a
 detailed receipt with all necessary information, including a "return by" date 30 days in the future
"""
# Exceeding Requirements: To exceed the requirements, extra features were added
# A New Year’s Sale reminder showing how many days are left until January 1st
# A Buy One, Get One Half-Off discount for the product D083 (yogurt), applied based on the quantity ordered
# A coupon for one of the products in the cart, printed at the bottom of the receipt


import csv
from datetime import datetime, timedelta


# Function to add the "return by" date, which is 30 days in the future at 9:00 PM
def get_return_by_date():
    future_date = datetime.now() + timedelta(days=30)
    return future_date.replace(hour=21, minute=0, second=0, microsecond=0)


# Function to calculate how many days until the New Year's Sale
def days_until_new_year():
    new_year = datetime(datetime.now().year + 1, 1, 1)  # Next year's New Year's day
    return (new_year - datetime.now()).days


# Function to apply the Buy One Get One Half Off discount for product D083
def apply_bogo_discount(product_code, quantity, price):
    if product_code == 'D083':
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        total_price = (full_price_items * price) + (half_price_items * price * 0.5)
        return total_price
    else:
        return price * quantity


def main():
    key_column_index = 0
    try:
        # Read the product data into a dictionary
        dictionary_products = read_dictionary("products.csv", key_column_index)

        print("\nGROCERY STORE\n")
        print("YOUR CART:")
        print('-' * 30)

        # Open the request file and process it
        with open("request.csv", "rt") as request_csv:
            next(request_csv)  # Skip the header
            request = csv.reader(request_csv)

            sum_quantity = 0
            sum_subtotal = 0
            sales_tax = 0
            total = 0
            products_ordered = []  # To keep track of products for coupons

            for line in request:
                product = line[0]
                quantity = int(line[1])

                try:
                    # Fetch the product information from the dictionary
                    product_info = dictionary_products[product]

                    product_code = product_info[0]
                    product_name = product_info[1]
                    product_cost = float(product_info[2])

                    # Apply Buy One, Get One Half Off discount for D083
                    total_price = apply_bogo_discount(product_code, quantity, product_cost)

                    # Print the item details
                    print(f"{product_name}: {quantity} @ ${product_cost:.2f}.")
                    print(f"Discounted Price: ${total_price:.2f}")
                    sum_quantity += quantity
                    sum_subtotal += total_price
                    products_ordered.append(product_name)  # Track ordered products

                except KeyError:
                    # Handle unknown product IDs in the request file
                    print(f"ERROR: unknown product ID in the request.csv file: '{product}'")
                    break

            # Calculate the sales tax and total
            sales_tax += (sum_subtotal * 0.06)
            total += (sum_subtotal + sales_tax)

            print('-' * 30)
            print(f"Number of items in your cart: {sum_quantity}")
            print()
            print(f"Subtotal: ${sum_subtotal:.2f}")
            print(f"Sales Tax: ${sales_tax:.2f}")
            print(f"Total: ${total:.2f}")
            print()

            # Print the current date and time
            print("Thank you!")
            dt = datetime.now()
            print(f"Date and Time: {dt:%A %I:%M %p}")

            # Print the "return by" date 30 days from now at 9:00 PM
            return_by_date = get_return_by_date()
            print(f"Return By: {return_by_date:%A, %B %d, %Y %I:%M %p}")

            # Print a reminder for how many days until the New Year's Sale
            days_to_new_year = days_until_new_year()
            print(f"New Year's Sale starts in {days_to_new_year} days!")

            # Print a coupon for one of the products ordered
            if products_ordered:
                product_for_coupon = products_ordered[0]  # You can adjust this logic as needed
                print(f"Coupon: Save 10% on your next purchase of {product_for_coupon}!")

    except FileNotFoundError:
        print("File 'products.csv' or 'request.csv' not found.")
    except PermissionError:
        print("You don't have permission to access one of the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a dictionary and return it.

    Parameters:
        filename: The name of the CSV file to read.
        key_column_index: The index of the column to use as the keys in the dictionary.

    Return:
        A dictionary containing the contents of the CSV file.
    """
    dictionary_products = {}

    try:
        with open(filename, "rt") as csv_file:
            next(csv_file)  # Skip the header
            file = csv.reader(csv_file)

            for line in file:
                key = line[key_column_index]
                dictionary_products[key] = line
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"You don't have permission to access '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")

    return dictionary_products


# Call main to start the program
if __name__ == "__main__":
    main()
