'''
The following table illustrates the cutoff scores for the various academic grades in a school. Write a program that will prompt the student for his score and your program should display his grade.
'''

# Request input from user
usrInput = float(input("Enter your score:"))
# Implement your logic her
for e in range(1):
    if usrInput >= 80:
        grade = "A"
    elif usrInput >= 70:
        grade = "B"
    elif usrInput >= 60:
        grade = "C"
    elif usrInput >= 50:
        grade = "D"
    else:
        grade = "F"
# Print out the output
print("Your grade is",grade)