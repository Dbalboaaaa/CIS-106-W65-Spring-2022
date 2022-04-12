def comprateofpay(jobcode):
  if jobcode == "L":
    rateofpay = 25
  elif jobcode == "A":
    rateofpay = 30
  elif jobcode == "J":
    rateofpay = 50

  return rateofpay

def compgrosspay(hrsworked,rateofpay):
  if float(hrsworked) > 40:
    grosspay = (hrsworked * rateofpay) * 1.5
  else:
    grosspay = hrsworked * rateofpay

  return grosspay

lastname = str(input("Enter last name"))
jobcode = str(input("Enter jobcode"))
hrsworked = float(input("Enter hoursworked"))

rateofpay = comprateofpay(jobcode)
grosspay = compgrosspay(hrsworked,rateofpay)

print("Last name:   ", lastname)
print("Grosspay:  ", grosspay)
