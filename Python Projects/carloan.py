# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:38:18 2024

@author: 2561986; Justin Marcel Camonayan

Computer Science 11

Car Loan Calculator
"""
# Constants for GST and PST rates 

GST_RATE = 0.05 
PST_RATE = 0.07   

vehicle_cost = float(input("Vehicle cost ($): ")) 
interest_rate = float(input("Annual interest rate (%): ")) 

# Calculate total tax amount
total_tax = vehicle_cost * (GST_RATE + PST_RATE) 

# Calculate total cost with tax (principal) 
principal = vehicle_cost + total_tax 

# Prompt user for loan duration 
years = int(input("Duration of loan (years): ")) 
while years > 10: 
    print("Maximum loan duration is 10 years.") 
    years = int(input("Duration of loan (years): ")) 

# Calculate interest rate and total number of payments 
monthly_interest = (interest_rate / 100) / 12 
months = years * 12  

# Calculate monthly payment using formula 
numerator = (principal * monthly_interest) 
denominator = (1 - (1 + monthly_interest) ** - months) 

monthly_payment = numerator / denominator

print("\nSummary:\n") 
print(f"Loan amount (vehicle cost with tax): {principal:.2f}") 
print("Interest rate: {:.2f}%".format(interest_rate)) 
print("Duration (Years):", years) 
print(f"Monthly payment: {monthly_payment:.2f}") 

remaining_balance = principal 

for year in range(years): 
    for month in range(12): 
        remaining_balance -= monthly_payment - (remaining_balance * monthly_interest) 
        if remaining_balance <= 0: 
            remaining_balance = 0
            break 
    print(f"Year {year + 1} Balance: {remaining_balance:.2f}") 


total_payments_amount = monthly_payment * months 
total_interest_paid = total_payments_amount - principal 

print(f"Total payments: {total_payments_amount:.2f}") 
print(f"Total interest paid: {total_interest_paid:.2f}") 

