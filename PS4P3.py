principleamount = float(input("Enter principle amount"))
yearsofm = float(input("Enter years of maturity"))

if principleamount > 100000 and yearsofm == 5:
  interestrate = 0.06
elif principleamount >= 50000 and yearsofm == 10:
  interestrate = 0.05
elif principleamount >= 50000 and yearsofm == 5:
  interestrate = 0.04
else:
  interestrate = 0.02

firstyearint = principleamount * interestrate 

print("Principle amount:   ", principleamount)
print("Interest rate:   ", interestrate)
print("Interest amount for first year:    ", firstyearint)


