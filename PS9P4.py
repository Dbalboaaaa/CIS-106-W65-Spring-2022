def compscore(score1, score2, score3):
  avg = (score1 + score2 + score3)/3
  handiscore = ((score1 + score2 + score3) - avg) * 0.9

  return avg, handiscore

lastname = input("Enter  bowlers last name")
score1 = float(input("Enter score 1"))
score2 = float(input("Enter score 2"))
score3 = float(input("Enter score 3"))

avg, handiscore = compscore(score1, score2, score3)

print("Last name:  ", lastname)
print("Average score is:   ", avg)
print("Average score with handicap is:   ", handiscore)
  