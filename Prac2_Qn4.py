'''
Write a program that prompts the user for two integers. The 2 integers are added and
the result is displayed. Your program should also be able to determine if the 1 st integer
is divisible by the 2 nd integer.
'''
# Prompt user for first integer
# Prompt the user for second integer
# Added the two integers
# print sum of integer
# if 1st integer is divisible by 2nd integer
#   print yes it can

first_integer = int(input("Enter 1st: "))
second_integer = int(input("Enter 2nd: "))
sum_of_numbers = first_integer + second_integer
print(sum_of_numbers)

if first_integer % second_integer == 0:
    print("It is divisble")
else:
    print("It is not")
