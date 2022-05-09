def items(mylist):
  n = int(input("Number of items for your list"))
  for n in range(0,n,1):
    s = int(input("Enter integer"))
    mylist.append(s)
  return mylist

def displaylist(mylist):
  for item in mylist:
    print(item)

mylist = []
mylist = items(mylist)
displaylist(mylist)
print(mylist)

mylist.insert(0,99)
print(mylist)

mylist[0] = 100
print(mylist)

mylist2 = [500, 600, 700, 800, 900]
mylist2.extend(mylist)
print(mylist2)

mylist2.remove(800)
print(mylist2)

mylist.remove(3)
print(mylist)

mylist3 = ["A", "B", "B", "C", "A", "A", "D"]
A_Count = mylist3.count("A")
print("Count of A grades: There are", A_Count, "A grades")

print(mylist3.index("B"))

if "F" != mylist3:
  print("F is not in the list")

mylist2.clear()
print(mylist2)

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print(players)

players.sort()
print(players)

players2 = players.copy()
print(players2)

players2.reverse()
print(players2)