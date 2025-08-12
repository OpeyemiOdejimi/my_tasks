# Nigerian Currency Converter (Very Advanced)
# - Ask for:
#   * Amount in Naira(float)
#   * Exchange rate to US Dollars (float)
#   * Exchange rate to British Pounds(float)
# _ Convert and print results with thousands separators and currency symbpls, neatly aligned in a table-like format using escape sequences.

amount_in_naira = (float(input("Enter amount in Naira: ")))
exchange_in_usd = (float(input("Enter exchange rate to Dollars: ")))
exchange_in_pounds = (float(input("Enter exchange rate to pounds: ")))

amount_usd = amount_in_naira / exchange_in_usd
amount_pounds = amount_in_naira / exchange_in_pounds

print("\n--- SCHOOL FEES BREAKDOWN ---")
print("Currency\tAmount")
print(f"₦\t\t{amount_in_naira:,.2f}")
print(f"$\t\t{amount_usd:,.2f}")
print(f"£\t\t{amount_pounds:,.2f}")
print("-----------------------------")
