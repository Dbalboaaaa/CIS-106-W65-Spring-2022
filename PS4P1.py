quantityofw = int(input("Enter quantity of widgets"))

if quantityofw > 10000:
  price = 10
elif quantityofw >= 5000:
  price = 20
else:
  price = 30 

extendedprice = quantityofw * price
tax = 0.07
taxamount = extendedprice * tax
total = extendedprice + taxamount

print("Extended price:     ", extendedprice)
print("Tax:     ", tax)
print("Total:   ", total)


