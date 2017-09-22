def main():
  students = [
    Student("Larsson", 37),
    Student("BonJovi", 55),
  ]

  printHeader()
  selection = getUserSelection()

class Student:
  def __init__(self, lastName, age):
    self.lastName = lastName
    self.age = age
    self.firstName = "NONE SPECIFIED"

  def assignRandomName(self):
    pass

  def assignRandomAge(self):
    pass

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
  print inputQuestions[0]
  print inputQuestions[1]
  print inputQuestions[2]
  return input("Type selection and press enter:")


def printHeader():
    print("HEADER TEXT HERE")

def printStudentsByAge():
  print "----Students By Age-----"

def printStudentsLName():
  print "----Students By -----"

def printStudentsFName():
  print "----Students By -----"

def printSumAge():
  print "Answer:"

def printAvgAge():
  print "Answer:"

def ageRange(studentA, studentB):
  pass


main()