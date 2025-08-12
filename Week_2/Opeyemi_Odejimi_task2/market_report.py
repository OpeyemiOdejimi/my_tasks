# Daily Market Report Ask the user to input:
# - Market name
# - Number of traders
# - Daily revenue in naira
# - Display the result using f-string formatting with commas for thousands seperator.

market_name = input("Market name:")
number_of_traders = (int(input("Number of traders:")))
daily_revenue = (float(input("Daily revenue in naira:")))

print(f"Market: {market_name} | Traders: {number_of_traders:,} | Daily revenue: {daily_revenue:,.2f}")