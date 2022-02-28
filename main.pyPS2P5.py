#comment input
price = float(input("Enter price of an item"))
discount = float(input("Enter the discount percent"))

#process phase
discountamount = price * discount
discountedpriceofitem = price - discountamount

#output
print("$", discountedpriceofitem)