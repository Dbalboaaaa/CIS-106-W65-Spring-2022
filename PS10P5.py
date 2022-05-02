def displaynames(name, avg):
  for i in name, avg:
    print(i)
  for g in avg:
    print(g)
  l = len(name)
  print("Display array using for loop controls")
  for x in range(0,l,1):
    print(x, " ", name[x], " ", avg[x])

f = open("names.txt", "r")

name = []
avg = []

namess = f.readline()


while namess != "":
  name.append(str(namess).rstrip("\n"))
  a = float(f.readline())
  avg.append(a)
  namess = f.readline()
f.close()

displaynames(name, avg)

def seqsearch(name, sname):
  l = len(name)
  sindex = -1
  for y in range(0,l,1):
    if name[y] == sname:
      sindex = y

  return sindex 

response = input("Do you want to do this program (Yes or No)")

while response == "Yes":
  sname = input("Enter last name to search for")
  i = seqsearch(name, sname)
  if i == -1:
    print(sname, " not in the array")
  else:
    print(name[i], " has an average score of ", avg[i])

  response = input("Do you want to do this program (Yes or No)")
