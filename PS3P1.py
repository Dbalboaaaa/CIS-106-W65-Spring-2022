qty = float(input("Enter quantity to order"))

if qty >=1000:
  up = 3.00
else:
  up = 5.00

exprice = qty * up

tax = exprice * 0.07 

total = tax + exprice 

print("Quantity order is ", qty)
print("Unit price is:      ", up)
print("Extended price is:     ", exprice)
print("Tax is:    ", tax)
print("Total is:    ", total)