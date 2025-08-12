# Nigerian Festival Info
# - Ask for:
#    *Festival name (string)
#    * Location (string)
#    * Month held (string)
# - Display the info with quoatations marks around the festival name using escape sequences (\")

festival_name = input("Enter festival name: ")
location = input("Enter the location of the festival: ")
month_held = input("Enter the month the festival is held: ")

print("The \""+ festival_name + "\" festival is held in " + location + " during the month of " + month_held +  ".")