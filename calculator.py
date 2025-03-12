print("SIMPLE CALCULATOR") 
'\n'
#taking the users input
x = int(input("Enter your first number: "))
'\n'
print("Select an Operation from the options provided: ")
'\n'
print("1.Addition" '\n' "2.subtration" '\n' "3.multiplation" '\n' "4.Division")
operation = int(input("operation option: "))
'\n'
y = int(input("Enter your second: "))

#fuction to perform the arithemic operation
def add(x, y):
    return x + y
def subtrate(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y


if operation  == 1 :
    add(x,y)
    print(f"{x} + {y} = {add(x,y)}")
elif operation == 2:
    subtrate(x,y)
    print(f"{x} + {y} = {subtrate(x,y)}")
elif operation  == 3:
    multiply(x,y)
    print(f"{x} + {y} = {multiply(x,y)}")
elif operation == 4:
    divide(x,y)
    print(f"{x} + {y} = {divide(x,y)}")
else:
    print("PLEASE ENTER A VALID NUMBER FROM THE CHOOSES GIVEN ABOVE!!")
