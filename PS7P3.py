def compmilespergallon(miles, gallonsused):
  milespergallon = float(miles) / float(gallonsused)
  
  return milespergallon

def compcost(gallonsused):
  cost = float(gallonsused) * 2.50

  return cost

city = input("Enter destination city")
miles = input("Enter miles travelled")
gallonsused = input("Enter gallons used")

cost = compcost(gallonsused)

print("Destination city:   ", city)
print("Miles travelled:    ", miles)
print("Cost of gas:   ", cost)
