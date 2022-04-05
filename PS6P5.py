counter = 0
response = input("Do you want to calculate tution owed Yes or No")

while response == "Yes":
  counter = counter + 1
  lastname = input("Enter lastname")
  credits = input("Enter credits taken")
  district = input("Enter district code I or O")
  if district == "I":
    tuition = 250.0
  else:
    tution = 500.0
  
  tuitionowed = float(credits) * float(tuition)
  totalowed = tuitionowed + tuitionowed
  print(lastname, credits, tuitionowed)
  response = input("Do you want to calculate tution owed Yes or No")

print("Sum of all tuition owed:  ", totalowed)
print("Number of students:  ", counter)
  
    


