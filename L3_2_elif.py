mark = input("Enter your mark in the test -> ")

print ("\nYou have entered" , mark , "marks")
marks = int(mark)
grade = "F"
if marks >= 80:
  grade = "A"
elif marks >= 70:
  grade = "B"
elif marks >= 60:
  grade = "C"
elif marks >= 50:
  grade = "D"
# else
#   grade = "F"

print ("Your grade is " + grade)
