discountam = 0

response = input("Want to calculate your discount amount Yes or No")

while response == "Yes":
  discountam1 = discountam
  quantity = int(input("Enter quantity amount"))
  priceofanitem = float(input("Enter price of item"))
  extendedprice = int(quantity) * float(priceofanitem)
  if extendedprice > 10000.00:
    discount = 0.25
  else:
    discount = 0.1
  discountam = float(extendedprice) * float(discount)
  total = float(extendedprice) - float(discountam)
  discountsum = float(discountam1) + float(discountam)
  print("Extended price is: ", extendedprice)
  print("Discount amount is: ", discountam)
  print("Total is: ", total)
  print("Discount percent is: ", discount)
  response = input("Want to calculate your discount amount Yes or No")

discountsum = float(discountam1) + float(discountam)
print("Sum of all discounts: ", discountsum)
  
  
