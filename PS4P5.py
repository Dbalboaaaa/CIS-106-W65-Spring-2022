lastname = input("Enter last name")
salary = float(input("Enter salary"))
joblevel = int(input("Enter job level"))

if joblevel >= 10:
  bonusrate = 0.25
elif joblevel >= 5:
  bonusrate = 0.2
else:
  bonusrate = 0.1

bonus = salary * bonusrate

print(lastname, ",", bonus)