# School Fees Breakdown
# - Ask for:
#    * Tuition fee(float)
#    * Hostel fee(float)
#    * Feeding fee(float)
# - Calculate the total and print it in receipt format with each fee on a new line

tuition_fee =(float(input("Enter tuition fee: ")))
hostel_fee =(float(input("Enter hostel fee: ")))
feeding_fee = (float(input("Enter  feeding fee: ")))

total = tuition_fee + hostel_fee + feeding_fee

print("\n--- SCHOOL FEES RECEIPT ---")
print(f"Tuition Fee:\t₦{tuition_fee:,.2f}")
print(f"Hostel Fee:\t₦{hostel_fee:,.2f}")
print(f"Feeding Fee:\t₦{feeding_fee:,.2f}")
print("----------------------------")
print(f"Total:\t\t₦{total:,.2f}")
print("----------------------------")