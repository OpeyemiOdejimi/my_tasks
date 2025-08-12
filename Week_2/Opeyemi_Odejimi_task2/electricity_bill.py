# Electricity Bill Formatter
# - Ask for:
#   *Customer's full name 
#   *Units consumed (kWh) - integer
#   *Cost per unit - float
# Calculate the total bill and print it in a neatly formatted receipt using sequences for line breaks.

customer_name = input("What is your name?:")
units_consumed = int(input("Enter the number of units consumed: "))
per_unit_cost = float(input("Enter cost per unit: "))

# Total bills calculation
total_bill = units_consumed * per_unit_cost

print(f"Customer Name: {customer_name}\nUnits consumed: {units_consumed}\nCost per Unit: {per_unit_cost:,.2f}\nTotal bill: {total_bill:,.2f}")