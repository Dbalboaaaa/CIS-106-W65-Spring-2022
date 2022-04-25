salesperson = input("Enter salesperson lastname")
sales = float(input("Enter sales made"))

def compcomm(sales):
  if sales <= 100000:
    comm = 0.05
  else:
    comm = 0.05

  nextysales = sales * 0.05

  return comm, nextysales

comm, nextysales = compcomm(sales)

print("Last name:   ", salesperson)
print("Commission:   ", comm)
print("Next year's target:   ", nextysales)

    
  