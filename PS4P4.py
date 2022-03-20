numberoft = int(input("Enter number of tickets"))

if numberoft >= 25:
  priceoft = 50
elif numberoft >= 10:
  priceoft = 60
elif numberoft >= 5:
  priceoft = 70
else:
  priceoft = 75

totalcost = numberoft * priceoft 

print("Number of ticket:    ", numberoft)
print("Price per ticket:    ", priceoft)
print("Total cost:    ", totalcost)


