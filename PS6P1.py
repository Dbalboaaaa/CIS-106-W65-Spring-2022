p = float(input("Enter principle"))
r = float(input("Enter interest rate"))

for count in range (1, 6, ):
  i = p * r 
  eb = p + i 
  print(count, "     ", p, "     ", eb)
  p = eb
