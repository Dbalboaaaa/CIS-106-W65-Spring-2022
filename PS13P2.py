class Student:
  def __init__(self, first, last, district, credits):
    self.first = first
    self.last = last
    self.district = district
    self.credits = credits

  def fullname(self):
    return "{} {}".format(self.first, self.last)

  def tuition(self, price):
    t = int(price) * int(self.credits)
    return t

    
stu_1 = Student("Daniel", "Balboa", "I", 18)

stu_1.fullname()
print(Student.fullname(stu_1))
print(stu_1.credits)
print(stu_1.tuition(250))