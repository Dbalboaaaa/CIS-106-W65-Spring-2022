def compbattingavg(hits, bats):
  battingavg = float(hits) / float(bats)

  return battingavg


lastname = input("Enter lastname")
hits = float(input("Enter number of hits"))
bats = float(input("Enter number of bats"))

battingavg = compbattingavg(hits, bats)

print("Last name:  ", lastname)
print("Batting average:   ", battingavg)

