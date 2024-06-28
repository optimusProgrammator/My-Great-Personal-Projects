# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:15:30 2024

@author: 2561986 : Justin Marcel Camonayan

Amortization Activity
"""
purchase_price = float(input("Purchase price (in dollars): "))
down_payment_percentage = float(input("Down payment percentage: "))
interest_rate = float(input("Interest rate (as a percentage): "))
payment_type = input("Payment type (Monthly, Semi-Monthly, Bi-weekly, Weekly): ").lower()
payment_amount = float(input("Payment amount (in dollars): "))

down_payment = purchase_price * (down_payment_percentage / 100)
loan_amount = purchase_price - down_payment

if payment_type == "monthly":
    payments_per_year = 12
elif payment_type == "semi-monthly":
    payments_per_year = 24
elif payment_type == "bi-weekly":
    payments_per_year = 26
elif payment_type == "weekly":
    payments_per_year = 52
else:
    print("Invalid payment type.")
    exit()

period = 0
total_interest_paid = 0
total_principal_paid = 0
cumulative_interest = 0
cumulative_principal = 0

print("{:<7} {:<18} {:<12} {:<10} {:<10} {:<18}".format("Period", "Starting Balance", "Payment", "Interest", "Principal", "Ending Balance"))
print("-" * 80)

while loan_amount > 0:
    period += 1
    interest_payment = round(loan_amount * ((interest_rate / 100) / payments_per_year),2)
    total_interest_paid += interest_payment
    cumulative_interest += interest_payment
    
    principal_payment = round(payment_amount - interest_payment,2)
    total_principal_paid += principal_payment
    cumulative_principal += principal_payment
    
    ending_balance = round(loan_amount - principal_payment,2)
    loan_amount = round(ending_balance,2)
    
    print("{:<7} ${:<16} ${:<12} ${:<10} ${:<10} ${:<16}".format(period, round(loan_amount + principal_payment, 2), payment_amount, interest_payment, principal_payment, ending_balance))

    if period % payments_per_year == 0:
        print(f"Year {period // payments_per_year} Summary:")
        print(f"Total interest paid this year: ${round(cumulative_interest, 2)}")
        print(f"Total principal paid this year: ${round(cumulative_principal, 2)}")
        print("-" * 30)
        cumulative_interest = 0
        cumulative_principal = 0
    

print("\n Overall Summary:")
print(f"Initial loan amount: ${round(purchase_price - down_payment, 2)}")
print(f"Total interest paid: ${round(total_interest_paid, 2)}")
print(f"Total principal paid: ${round(total_principal_paid, 2)}")
