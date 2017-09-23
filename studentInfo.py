def main():
  students = [
    Student("Larsson", 37),
    Student("BonJovi", 55),
  ]

  printHeader()
  selection = getUserSelection()
  if selection == 0:
    printStudentsByAge(students)
  elif selection == 1:
    pass
  elif selection == 2:
    pass
  else:
    print "SELECTION NOT RECOGNIZED"


class Student:
  def __init__(self, lastName, age):
    self.lastName = lastName
    self.age = age
    self.firstName = "JOHN"

  def assignRandomName(self):
    pass

  def assignRandomAge(self):
    self.age = random.randint(0,100)

  def assignRandomWeight(self, isMetric):
    pass

  def assignRandomHeight(self, isMetric):
    pass

inputQuestions = [ 
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 3",
  "For SUM of STUDENT AGES type 4",
  "For AVERAGE of STUDENT AGES type 5",
]

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  return input("Type selection and press enter:")

def printHeader():
    print("HEADER TEXT HERE")

def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in students:
    print student.lastName + ", " + student.firstName + ", " + str(student.age)

def printStudentsByLName(students):
  print ("----Students By -----")

def printStudentsByFName(students):
  print ("----Students By -----")

def printSumAge(students):
  print ("Answer:")

def printAvgAge(students):
  print ("Answer:")

def ageRange(studentA, studentB):
  return math.abs(studentA.age - studentB.age)


main()