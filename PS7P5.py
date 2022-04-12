def comptuitionowed(credithrs, districtcode):
  if districtcode == "I":
    tuitionowed = credithrs * 250
  elif districtcode == "O":
    tuitionowed = credithrs * 550
  
  return tuitionowed

lastname = str(input("Enter last name"))
credithrs = float(input("Enter credit hours taken:"))
districtcode = str(input("Enter disctrict code"))

tuitionowed = comptuitionowed(credithrs, districtcode)

print("Last name:   ", lastname)
print("Tuitionowed:  ", tuitionowed)