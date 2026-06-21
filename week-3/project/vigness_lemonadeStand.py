"""
Author: Boyd Vigness
Date: September 2025
File Name: Vigness_lemonadeStand.py
Description: This program simulates a lemonade stand by calculating total
profit made by subtracting the costs from the earnings.
"""

# Calculates the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost
    return total_cost


# Calculates the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = calculate_cost(lemons_cost, sugar_cost)
    profit = selling_price - total_cost
    return profit


# Cost/Price Variables
lemons_cost = 5
sugar_cost = 3
selling_price = 12

# Call the functions
total_cost = calculate_cost(lemons_cost, sugar_cost)
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

# Build output strings
cost_output = str(lemons_cost) + " + " + str(sugar_cost) + " = " + str(total_cost)
profit_output = str(selling_price) + " - " + str(total_cost) + " = " + str(profit)

# Print results
print("Cost Calculation:")
print(cost_output)

print("\nProfit Calculation:")
print(profit_output)