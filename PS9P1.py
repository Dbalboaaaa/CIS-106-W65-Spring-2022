quantity = float(input("Enter quantity"))
price = float(input("Enter price"))
discountrate = float(input("Enter discount rate"))

def comptotal(quantity, price):
  disamount = (float(quantity) * float(price)) * float(discountrate)
  disprice = (float(quantity) * float(price)) - float(disamount)

  return disamount and disprice

disprice = comptotal(quantity, price)

print("Discounted price is: ", disprice)
