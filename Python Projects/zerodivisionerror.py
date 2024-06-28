# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:47:32 2024

@author: 2561986; Justin Marcel Camonayan

Comp Sci 11

Basic Try and Except Program /  Zero Divison Error  

"""
try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator / denominator
    
    if result * denominator == numerator:
        print("Divides evenly!")
    else:
        print("Doesn't divide evenly.")
        
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integer values for numerator and denominator.")

