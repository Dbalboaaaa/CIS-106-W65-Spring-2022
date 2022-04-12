def comptotal(qty, price): 
  total = float(qty) * float(price)
  
  if total > 10000.00:
    total = total * 0.9
  else:
    total = total

  return total

qty = float(input("Enter quantity"))
price = float(input("Enter price"))

total = comptotal(qty, price)

print("Total is $", total)

