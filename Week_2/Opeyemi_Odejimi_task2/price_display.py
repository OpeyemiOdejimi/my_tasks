# Price Display with Type Casting
# - Ask the user for the price of garri per paint in naira(as a string) and convert it to float. Display it with a message showing the amount in naira and kobo using print().

garriPrice=input("What is the price of garri per paint in Naira?:")
priceInFloat=float(garriPrice)
print(f"Garri currently sells for #{int(priceInFloat)} Naira and {round((priceInFloat % 1) * 100)} kobo.")
