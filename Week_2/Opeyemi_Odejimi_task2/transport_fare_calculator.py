# Transport Fare Calculator
# - Ask for:
#    * Distance in km (float)
#    * Fare per km (float)
# - Calculate and display the total fare with two decimal places using f"{value:.2f}

distance = (float(input("Enter distance in km: ")))
fare_per_km = (float(input("Enter fare per km: ")))

total_fare = distance * fare_per_km

print(f"Total transport fare: #{total_fare:.2f}")