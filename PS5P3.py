counter = 0

response = input("Want to calculate average score Yes or No")

while response == "Yes":
  counter = counter + 1
  lastname = input("Enter student name")
  score1 = float(input("Enter exam score 1"))
  score2 = float(input("Enter exam score 2"))
  avg = (score1 + score2)/2
  print(lastname, " has average of ", avg)
  response = input("Want to calculate average score Yes or No")

print ("Number of students:  ", counter)

