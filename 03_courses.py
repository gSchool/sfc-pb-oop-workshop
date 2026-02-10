"""
You are tasked with developing a system to manage a school's enrollment.
The system should allow for adding students to a course,
  calculating the average grade of the students,
  and determining the total number of students enrolled.
You will need multiple classes in order to accomplish this and one will utilize the other when being invoked.
See example:

course = Course("Math 101")
course.add_student(Student("Alice", 85))
course.add_student(Student("Bob", 92))

print(course.get_average_grade())  # Prints 88.5
print(course.get_total_students())  # Prints 2


Once your classes are complete, copy and paste the above example below them in order to test their functionality.
"""

"""
Write a class that meets these requirements.

Name:       Course

Required state:
   * course name, the name of the course

Behavior:
   * add_student(student)     # Add a Student to the Course
   * get_average_grade()      # Returns the average grade of all students in the course
   * get_total_students()     # Returns the total number of students enrolled in the course

"""

"""
Write a class that meets these requirements.

Name:       Student

Required state:
   * name, the name of the student
   * grade, the grade of the student

Behavior:
   * get_grade()          # Returns the grade of the student

Example:
   student = Student("Alice", 85)

   print(student.get_grade())    # Prints 85

"""

class Course:
  def __init__(self, course_name):
    self.course_name = course_name
    self.student = []
    self.student_grades = []
    self.get_grade = []
    self.grade_averages = 0

  def add_student(self, student): # Add a Student to the Course
   self.get_grade.append(student.grade) # save comment as below
   self.student.append(student.name) # student is instance of Student. Can access Student attributes with dot notation
   return self.student

  def get_average_grade(self): # Returns the average grade of all students in the course
   self.grade_averages = sum(self.get_grade)/len(self.get_grade)
   return self.grade_averages

  def get_total_students(self): # Returns the total number of students enrolled in the course
   return len(self.student)

class Student:
  def __init__(self, name, grade):
   self.name = name
   self.grade = grade

  def get_grade(self): # Returns the grade of the student
   return self.grade

course = Course("Math 101")
course.add_student(Student("Alice", 85))
course.add_student(Student("Bob", 92))
print(course.get_average_grade())  # Prints 88.5
print(course.get_total_students())  # Prints 2


student = Student("Alice", 85)
print(student.get_grade())    # Prints 85