#comment input
lastname = (input("Enter last name"))
hours = float(input("Enter hours"))
payrate = float(input ("Enter pay rate"))


#process phase
grosspayrate = hours * payrate

#output
print(lastname,",","$", grosspayrate)