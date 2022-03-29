counter = 0 

response = input("Do you want to compute your grosspay Yes or No")

while response == "Yes":
  counter = counter + 1
  lastname = input("Enter last name")
  hrsworked = int(input("Enter hours worked"))
  rateofpay = int(input("Enter rate of pay"))
  overtime = 1.5
  if hrsworked > 40:
    totalgross = (hrsworked * rateofpay) * 1.5
  else:
    totalgross = (hrsworked * rateofpay)
  grosspay = totalgross + totalgross
  print("Employee:  ", lastname, totalgross)
  response = input("Do you want to compute your grosspay Yes or No")

print("Total number of employees:   ", counter, "Grosspay sum: ", grosspay)
avgpay = grosspay / counter
print("Average pay is:   ", avgpay)

