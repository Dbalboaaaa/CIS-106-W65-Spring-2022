lastname = input("Enter last name")
numberofdependents = input("Enter number of dependents")
grossincome = input("Enter gross income")

adjgrossincome = float(grossincome) - float(numberofdependents)* 12000

if adjgrossincome <= 5000:
  taxrate = 0.1
else:
  taxrate = 0.2

incometax = adjgrossincome * taxrate

print(lastname)
print("Grossincome is $", grossincome)
print("Number of dependents: ", numberofdependents)
print("Adjusted gross income: $", adjgrossincome)
print("Income tax: $", incometax)

