response = input("Want to calculate avg and total Yes or No")

def comptotal(score1, score2, score3):
  while response == "Yes":
    avg = (score1 + score2 + score3)/3
    tpoints = score1 + score2 + score3

    return avg, tpoints
 
lastname = input("Enter student last name")
score1 = float(input("Enter exam score 1"))
score2 = float(input("Enter exam score 2"))
score3 = float(input("Enter exam score 3"))

avg, tpoints = comptotal(score1, score2, score3)

print(lastname, " has an average score of ", avg, " and has ", tpoints, " total points")
