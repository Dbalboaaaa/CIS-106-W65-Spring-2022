response = input("Enter response Yes or No")

if response == "Yes":
  lastname = input("Enter last name")
  sales = float(input("Enter sales"))
  month = input("Enter month")
  def compnextmforecast(month, sales):
    if month == "Jan or Feb or Mar":
      forecastperc = 0.10
    elif month == "Apr or May or Jun":
      forecastperc = 0.15
    elif month == "Jul or Aug or Sep":
      forecastperc = 0.2
    else:
      forecastperc = 0.25
    
    return forecastperc

forecatsperc = compnextmforecast(month, sales)
nextmsales = sales * (1 + forecatsperc)

print("Next months sales:    ", nextmsales)
