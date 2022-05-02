lastn = "Balboa", "Sullivan", "Cruise", "Cruz", "Brown"
score = 95, 84, 79, 91, 88

def displaylastn(lastn, score):
  lastn = "Balboa", "Sullivan", "Cruise", "Cruz", "Brown"
  score = 95, 84, 79, 91, 88
  for i in range(len(lastn)):
    print(lastn[i], score[i])


  return lastn, score




def displayrlastn(lastn, score):
  rlastn = lastn[::-1]
  rscore = score[::-1]
  for i in range(len(rlastn)):
    print(rlastn[i], rscore[i])
  

  return rlastn, rscore

comb = displaylastn(lastn, score)
rlastn= displayrlastn(lastn, score)

