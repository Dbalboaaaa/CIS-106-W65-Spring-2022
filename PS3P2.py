item = input("Enter item to order (A or B)")
qty = float(input("Enter quantity to order"))

if item == "A":
  up = 10.00
else: 
  up = 20.00

exprice = up * qty

print("Item ordered:  ", item)
print("Quantity is:  ", qty)
print("Unit price is:  ", up)
print("Extended price is:  ", exprice)


