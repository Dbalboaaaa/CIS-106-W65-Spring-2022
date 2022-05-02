lastn = "Balboa", "Sullivan", "Cruise", "Cruz", "Brown"
score = 95, 84, 79, 91, 88

def displaylastn(lastn, score):
  lastn = "Balboa", "Sullivan", "Cruise", "Cruz", "Brown"
  score = 95, 84, 79, 91, 88
  for i in range(len(lastn)):
    print(lastn[i], score[i])


  return lastn, score

def hilow(lastn, score):
  l = len(lastn)
  hiscore = -1
  lowscore = 99999999.99
  for i in range(0,l,1):
    if float(score[i]) > float(hiscore):
      hiindex = i
      hiscore = score[i]
    
    if float(score[i]) < float(lowscore):
      lowindex = i 
      lowscore = score[i]

  print("Highest score", lastn[hiindex], score[hiindex])
  print("Lowest score", lastn[lowindex], score[lowindex])
  

def displayrlastn(lastn, score):
  rlastn = lastn[::-1]
  rscore = score[::-1]
  for i in range(len(rlastn)):
    print(rlastn[i], rscore[i])
  

  return rlastn, rscore

comb = displaylastn(lastn, score)
rlastn = displayrlastn(lastn, score)
hilow(lastn, score)