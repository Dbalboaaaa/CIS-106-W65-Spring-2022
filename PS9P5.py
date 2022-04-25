total = 0.0
tax = 0.0

def comptotal(qty, price):
  global total
  total = (float(qty) * float(price)) 
  global tax
  tax = total * .07

  print("total: ", total)

  return tax, total

qty = input("Enter quantity")
price = input("Enter price")

comptotal(qty, price)
print("Tax:  ", tax)
print("Total: ", total)


