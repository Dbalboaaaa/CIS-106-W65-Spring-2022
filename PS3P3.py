qty = input("Enter number of books to order")
bcost = float(input("Enter cost per book"))

ordertotal = float(qty) * float(bcost)

if ordertotal <= 50:
  scharge = 25
else:
  scharge = 0

comtotal = ordertotal + scharge 

print("Total is ", ordertotal)
print("Shipping Charge:  ", scharge)
print("Total and shipping charge combined:  ", comtotal )