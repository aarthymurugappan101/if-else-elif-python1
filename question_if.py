'''
Take in a user input and check if it is divisble by 2
if it is, print the sentence "It is an even number"
'''

usrInput = input("Please give me a number?")
usrInput = int(usrInput)

if usrInput%2 == 0:
    print("It is an even number")