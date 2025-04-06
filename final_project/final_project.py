'''
(BSc) Software Development at Byu-Idaho  
Course: CSE-111 Programming with Functions
Final  Project: - Loan Calculator
Author: Tiago Borges  

Advanced Loan Calculator -  "Simplified Financial Planning"
This program assists with loan decisions (car, house, etc)
 Quickly calculate payments, view amortization and compare scenarios (Offers from different banks)

Usefulness:

Monthly Payment: Estimate the exact monthly disbursement
Total Cost: Visualize the total amount paid, including interest
Outstanding Balance: Track balance evolution via the amortization table (principal, interest, balance)
Offer Comparison: Analyze the impact of different rates and terms

How it Works:
Input the principal amount, interest rate (annual/monthly), and term (months). The program calculates:

- Monthly Payment: Fixed monthly amount (principal + interest)
- Amortization Schedule: Detailed schedule per period (payment, principal, interest, balance)
- Total Paid and Interest: Total amount paid and total interest

Save and Compare>>>
Save: After calculation, type yes and the filename (or Enter for default: loan_calculation.txt) to save results
Compare: After calculation, type yes and the number of loans to compare (including the current one) Enter details
for each to view a comparison table. You can also load data from a loans.csv file (columns: principal, rate, time, 
rate_type)

'''
#Let´s do it work! 

import logging
import csv
from typing import List, Tuple
import os  

# Configure logging to capture the events in a log file
logging.basicConfig(filename='loan_calculator.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def validate_positive_float(value: float, field_name: str) -> bool:
    # Validates if a float value is positive
    if value <= 0:
        logging.error(f"Invalid {field_name}: must be greater than 0")
        print(f"Error: {field_name} must be greater than zero")
        return False
    return True

def validate_non_negative_float(value: float, field_name: str) -> bool:
    # Validates if a float value is non-negative 
    if value < 0:
        logging.error(f"Invalid {field_name}: cannot be negative")
        print(f"Error: {field_name} cannot be negative")
        return False
    return True

def calculate_monthly_payment(principal: float, monthly_rate: float, num_payments: int) -> float:
    # Calculates the fixed monthly payment for the loan (juros compostos)
    if monthly_rate == 0:
        monthly_payment = principal / num_payments if num_payments > 0 else 0
    else:
        monthly_payment = (principal * monthly_rate * (1 + monthly_rate) ** num_payments) / \
                          ((1 + monthly_rate) ** num_payments - 1)
    logging.info(f"Monthly payment calculated: principal={principal}, rate={monthly_rate*100:.4f}%, time={num_payments}, monthly_payment={monthly_payment:.2f}")
    return monthly_payment

def generate_amortization_schedule(principal: float, monthly_rate: float, num_payments: int) -> List[dict]:
    # Generates the loan amortization schedule 
    schedule = []
    remaining_balance = principal
    monthly_payment = calculate_monthly_payment(principal, monthly_rate, num_payments)

    for period in range(1, num_payments + 1):
        interest_paid = remaining_balance * monthly_rate
        principal_paid = monthly_payment - interest_paid
        remaining_balance -= principal_paid

        schedule.append({
            'Period': period,
            'Payment': monthly_payment,
            'Principal Paid': principal_paid,
            'Interest Paid': interest_paid,
            'Remaining Balance': remaining_balance
        })
    logging.info(f"Amortization schedule generated for principal={principal}, rate={monthly_rate*100:.4f}%, time={num_payments}")
    return schedule

def display_results(principal: float, annual_rate: float, period: int, monthly_payment: float, total_paid: float, total_interest: float):
    #Displays the loan calculation results 
    
    print("\n📊 Loan Calculation Result 📊")
    print(f"📌 Loan Amount: $ {principal:.2f}")
    print(f"📌 Annual Interest Rate: {annual_rate:.2f}%")
    print(f"📌 Loan Period: {period} months")
    print(f"🗓️ Estimated Monthly Payment: $ {monthly_payment:.2f}")
    print(f"💰 Total Amount to be Paid: $ {total_paid:.2f}")
    print(f"💸 Total Interest Paid: $ {total_interest:.2f}")

def display_amortization_schedule(schedule: List[dict]):
    
    # Displays the amortization schedule in a table format 
    print("\n🗓️ Amortization Schedule 🗓️")
    print("-------------------------------------------------------------------------")
    print("{:<8} {:<15} {:<15} {:<15} {:<15}".format("Period", "Payment", "Principal", "Interest", "Balance"))
    print("-------------------------------------------------------------------------")
    for item in schedule:
        print("{:<8} ${:<14.2f} ${:<14.2f} ${:<14.2f} ${:<14.2f}".format(
            item['Period'], item['Payment'], item['Principal Paid'], item['Interest Paid'], item['Remaining Balance']
        ))
    print("-------------------------------------------------------------------------")

def get_loan_details() -> Tuple[float, float, int, str]:
    # Gets user input for loan details, including interest rate type 
    while True:
        try:
            principal = float(input("Enter the loan amount: $ "))
            if not validate_positive_float(principal, "loan amount"):
                continue

            rate_type = input("Is the interest rate annual or monthly? (annual/monthly): ").lower()
            while rate_type not in ['annual', 'monthly']:
                print("Invalid rate type. Please enter 'annual' or 'monthly'.")
                rate_type = input("Is the interest rate annual or monthly? (annual/monthly): ").lower()

            rate = float(input(f"Enter the {'annual' if rate_type == 'annual' else 'monthly'} interest rate (in %): "))
            if not validate_non_negative_float(rate, "interest rate"):
                continue

            time = int(input("Enter the loan period (in months): "))
            if not validate_positive_float(float(time), "loan period"):
                continue

            return principal, rate, time, rate_type
        except ValueError:
            logging.error("Invalid input format")
            print("Error: Invalid input. Please enter valid numbers")

def calculate_loan_totals(principal: float, monthly_rate: float, num_payments: int) -> Tuple[float, float]:
    # Calculates the total amount to be paid and the total interest paid 
    total_paid = calculate_monthly_payment(principal, monthly_rate, num_payments) * num_payments
    total_interest = total_paid - principal
    logging.info(f"Loan totals calculated: principal={principal}, rate={monthly_rate*100:.4f}%, time={num_payments}, total_paid={total_paid:.2f}, total_interest={total_interest:.2f}")
    return total_paid, total_interest

def compare_loans(loans_data: List[Tuple[float, float, int, str]]):
    # Compares multiple loan scenarios 
    print("\n📊 Loan Comparison 📊")
    print("--------------------------------------------------------------------------------------------------")
    print("{:<10} {:<15} {:<10} {:<15} {:<15} {:<15}".format("Loan", "Principal", "Rate", "Period", "Monthly Payment", "Total Interest"))
    print("--------------------------------------------------------------------------------------------------")
    for i, (principal, rate, time, rate_type) in enumerate(loans_data):
        monthly_rate = rate / 100 if rate_type == 'monthly' else (rate / 100) / 12
        monthly_payment = calculate_monthly_payment(principal, monthly_rate, time)
        total_interest = (monthly_payment * time) - principal
        print("{:<10} ${:<14.2f} {:<9.2f}% {:<9} ${:<14.2f} ${:<14.2f}".format(
            f"Loan {i+1}", principal, rate, time, monthly_payment, total_interest
        ))
    print("--------------------------------------------------------------------------------------------------")

def save_results_to_file(principal: float, annual_rate: float, period: int, monthly_payment: float, total_paid: float, total_interest: float, schedule: List[dict], filename="loan_calculation.txt"):
    # Saves the loan calculation results and amortization schedule to a file 
    try:
        # Ensure the filename has the .txt extension
        if not filename.lower().endswith(".txt"):
            filename += ".txt"

        with open(filename, 'w', newline='') as f:
            f.write("💰 Loan Calculation Results 💰\n\n")
            f.write(f"Loan Amount: $ {principal:.2f}\n")
            f.write(f"Annual Interest Rate: {annual_rate:.2f}%\n")
            f.write(f"Loan Period: {period} months\n")
            f.write(f"Estimated Monthly Payment: $ {monthly_payment:.2f}\n")
            f.write(f"Total Amount to be Paid: $ {total_paid:.2f}\n")
            f.write(f"Total Interest Paid: $ {total_interest:.2f}\n\n")

            f.write("🗓️ Amortization Schedule 🗓️\n")
            f.write("-------------------------------------------------------------------------\n")
            f.write("{:<8} {:<15} {:<15} {:<15} {:<15}\n".format("Period", "Payment", "Principal", "Interest", "Balance"))
            f.write("-------------------------------------------------------------------------\n")
            for item in schedule:
                f.write("{:<8} ${:<14.2f} ${:<14.2f} ${:<14.2f} ${:<14.2f}\n".format(
                    item['Period'], item['Payment'], item['Principal Paid'], item['Interest Paid'], item['Remaining Balance']
                ))
            f.write("-------------------------------------------------------------------------\n")
        print(f"\nResults saved to '{filename}'")
    except Exception as e:
        logging.error(f"Error saving results to file: {e}")
        print(f"Error: Could not save results to file.")

def main():
    # Main function that coordinates the program logic 
    print("💰 Welcome to the Advanced Loan Calculator 💰")

    principal, rate, time, rate_type = get_loan_details()

    monthly_rate = rate / 100 if rate_type == 'monthly' else (rate / 100) / 12
    annual_rate_display = rate if rate_type == 'annual' else rate * 12

    monthly_payment = calculate_monthly_payment(principal, monthly_rate, time)
    total_paid, total_interest = calculate_loan_totals(principal, monthly_rate, time)
    amortization_schedule = generate_amortization_schedule(principal, monthly_rate, time)

    display_results(principal, annual_rate_display, time, monthly_payment, total_paid, total_interest)
    display_amortization_schedule(amortization_schedule)

    save_option = input("\nDo you want to save the results to a file? (yes/no): ").lower()
    if save_option == 'yes':
        default_filename = "loan_calculation.txt"
        filename = input(f"Enter the filename to save (default: {default_filename}): ").strip()
        if not filename:
            filename = default_filename
        save_results_to_file(principal, annual_rate_display, time, monthly_payment, total_paid, total_interest, amortization_schedule, filename)

    compare_option = input("\nDo you want to compare this loan with another? (yes/no): ").lower()
    if compare_option == 'yes':
        while True:
            try:
                num_loans_to_compare = int(input("Enter the number of loans you want to compare (including the current one): "))
                if num_loans_to_compare > 0:
                    loans_to_compare = [(principal, rate, time, rate_type)]
                    for i in range(num_loans_to_compare - 1):
                        print(f"\nEnter details for Loan {i+2}:")
                        loan_data = get_loan_details()
                        if loan_data:
                            loans_to_compare.append(loan_data)
                    compare_loans(loans_to_compare)
                    break  # Exit the loop if input is valid
                else:
                    print("Please enter a number greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    # Option to load loan details from a CSV file
    load_option = input("\nDo you want to load loan details from a CSV file? (yes/no): ").lower()
    if load_option == 'yes':
        load_from_csv()

    # Option to export the amortization schedule to a CSV file
    export_schedule_option = input("\nDo you want to export the amortization schedule to a CSV file? (yes/no): ").lower()
    if export_schedule_option == 'yes':
        default_csv_filename = "amortization_schedule.csv"
        csv_filename = input(f"Enter the filename for the amortization schedule (default: {default_csv_filename}): ").strip()
        if not csv_filename:
            csv_filename = default_csv_filename
        export_amortization_to_csv(amortization_schedule, csv_filename)
def load_from_csv(filename="loans.csv"):
    #Loads loan details from a CSV file and performs comparison 
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    loans_data = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    principal = float(row['principal'])
                    rate = float(row['rate'])
                    time = int(row['time'])
                    rate_type = row['rate_type'].lower()
                    if rate_type not in ['annual', 'monthly']:
                        print(f"Warning: Invalid rate type '{rate_type}' in CSV, skipping row.")
                        continue
                    loans_data.append((principal, rate, time, rate_type))
                except (ValueError, KeyError) as e:
                    print(f"Warning: Invalid data in CSV row: {row}. Error: {e}")
                    continue
        if loans_data:
            compare_loans(loans_data)
        else:
            print("No valid loan data found in the CSV file.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

def export_amortization_to_csv(schedule: List[dict], filename="amortization_schedule.csv"):
    # Exports the amortization schedule to a CSV file 
    try:
        # Ensure the filename has the .csv extension
        if not filename.lower().endswith(".csv"):
            filename += ".csv"

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = schedule[0].keys() if schedule else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(schedule)
        print(f"\nAmortization schedule exported to '{filename}'")
    except Exception as e:
        logging.error(f"Error exporting amortization schedule to CSV: {e}")
        print(f"Error: Could not export amortization schedule to CSV file.")

if __name__ == "__main__":
    main()

 # Uaw;  297 Code-Lines? 
 # It demanded a lot of work! (A many  errors  occurred hehe) 
 # # Thanks for review my code