response = input("Enter response Yes or No")

if response == "Yes":
  lastname = input("Enter last name")
  miles = float(input("Enter miles from downtown Chicago"))
  def compprice (miles):
    if miles >= 30:
      tprice = 12
    elif miles >= 20:
      tprice = 10
    elif miles >= 10:
      tprice = 8
    else:
      tprice = 5

    price = miles * tprice


    return price

price = compprice(miles)

print("Ticket price:   ", price)
