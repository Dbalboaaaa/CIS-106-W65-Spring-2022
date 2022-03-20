partnumber = int(input("Enter part number"))
quantity = input("Enter quantity to purchase")

if partnumber == 10 or partnumber == 55:
  costpu = 1.00
elif partnumber == 99:
  costpu = 2.00
elif partnumber == 80 or partnumber == 70:
  costpu = 3.00
else:
  costpu = 5.00

total = costpu * float(quantity)

print ("Part number:   ", partnumber)
print("Unit price:     ", costpu)
print("Total:     ", total)


