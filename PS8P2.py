response = (input("Yes or No"))

if response == "Yes":
  length = input("Enter length")
  width = input("Enter width")
  height = input("Enter height")
  def compsquarefofroom (length, width, height):
    squarefofroom = (2 * (float(length) * float(width))) + (2 * (float(length) * float(height))) + (2 * (float(width) * float(height)))
    return squarefofroom

squarefofroom = compsquarefofroom(length, width, height)
gallons = squarefofroom / 50
print("Gallons needed:   ", gallons)