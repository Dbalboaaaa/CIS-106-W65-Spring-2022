#comment input
lastname = (input("Enter last name"))
credits = float(input("Enter credits taken"))

#process phase
tuition = 250
fee = 100
totaltuition= ((credits * tuition) + fee)

#output
print (lastname, ",", "$", totaltuition)