
greeting = ('enter name')

print('remember to have fun' , greeting, '!')

user = input("let's count numbers: ")


if user == "1":
        print("wrong way")
else:
        print("correct")



# if we need to calculate a num we need to get 2 num in the variable and add or sub or multiply
#first plese the num and the second num int
# answer

print("please enter your first number")
num1 = input()
num1 = int(num1)

print("please enter 2nd number")
num2 = input()
num2 = int(num2)

print("mul, add, sub, divid")
sub = input()

if sub == "mul":
        print(num1 * num2)
elif sub == "add":
        print(num1 + num2)

elif sub == "sub":
        print(num1 - num2)
elif sub == "divid":
        print(num1 / num2)
else:
        print("invalide operation enterted.")

"""

#this is broken down of the first part

print("please enter your second number... to add")
num2 = input()
num2 = int(num2)

answer = num1 + num2

print(answer)


print("please entre the first number to subract")
num1 = input()
num1 = int(num1)

print("please entre your second number")
num2 = input()
num2 = int(num2)

answer = num1 - num2

print(answer)


print ("please enter the number to multiply")
num1 = input()
num1 = int(num1)

print("please enter second numer to multiply")
num2 = input()
num2 = int(num2)

answer = num1 * num2

print(answer)

print ("please enter the number to divid")
num1 = input()
num1 = int(num1)

print("please enter second number to divid")
num2 = input()
num2 = int(num2)

answer = num1 / num2

print(answer)
"""
