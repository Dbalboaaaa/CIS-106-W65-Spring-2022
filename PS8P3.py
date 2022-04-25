response = input("Enter response Yes or No")

if response == "Yes":
  make = input("Enter make of car")
  model = input("Enter model of car")
  evehiclecode = input("Enter electric vehicle code Y or N")
  MSRP = float(input("Enter MSRP"))

  def compprice(MSRP, make, model, evehiclecode):
    if make and model == "Honda Accord":
      percentoff = 0.1
    elif make and model == "Toyota Rav4":
      percentoff = 0.15
    elif make and model == "EV":
      percentoff = 0.3
    else:
      percentoff = 0.05

    discount = float(MSRP) * float(percentoff)
    tax = 0.07
    NewMSRP = (float(MSRP) - float(discount)) * tax

    total = float(MSRP) - float(NewMSRP)

  

    return total
      
total = compprice(MSRP, make, model, evehiclecode)

print("Total is:  ", total)
      
  