response = input("Enter response Yes or No")

if response == "Yes":
  county = input("Enter county")
  marketvalue = float(input("Enter market value"))
  def compvalue(marketvalue):
    if county == "Cook":
      avpercent = 0.9
    elif county == "Dupage":
      avpercent = 0.8
    elif county == "McHenry":
      avpercent = 0.75
    elif county == "Kane":
      avpercent = 0.6
    else:
      avpercent = 0.7

    assessedvalue = float(marketvalue) * float(avpercent)

    return assessedvalue

assessedvalue = compvalue(marketvalue)

print("Market value:  ", marketvalue)
print("Assessed value:  ", assessedvalue)
      