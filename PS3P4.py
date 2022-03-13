appliance = input("Enter appliance")
appcost = float(input("Enter cost of appliance"))

if appcost <= 1000:
  warranty = appcost * 0.05
else:
  warranty = appcost * 0.1

total = appcost + warranty

print(appliance, " costs ", "$", appcost)
print("Warranty is $", warranty)
print("Total is $", total)


