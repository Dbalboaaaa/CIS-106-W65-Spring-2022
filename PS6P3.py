response = input("Do you want to compute your salary and bonus Yes or No")

total_bonus = 0

while response == "Yes":
  lastname = input("Enter last name")
  salary = float(input("Enter salary amount"))
  if salary >= 100000:
    bonusrate = .2
  elif salary == 50000:
    bonusrate = .15
  else:
    bonusrate = .1

  bonus = (salary * bonusrate) + salary
  total_bonus = total_bonus + bonus
  print("Employee lastname:  ", lastname)
  print("Employee salary:   ", salary)
  print("Employee bonus:   ", bonus)
  response = input("Do you want to compute your salary and bonus Yes or No")
 
print("Sum of all bonuses:   ", total_bonus )



