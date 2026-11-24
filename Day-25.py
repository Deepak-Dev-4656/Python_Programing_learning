# balance = 500
# try:
#     user_amount = int(input("Enter your amount: "))
#     if user_amount>balance:
#         print("insufficient Balance")
#     else:
#         print("Transation successful")
# except valueError:
#     print("invalid error")


# #program 1 safe Division

# try: 
#     num1 = int(input("Enter frist number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1/num2
#     print("Result: ",result)

# except ZeroDivisionError:
#     print("cannot divide by zero")

# except ValueError:
#     print("Enter number only")
#7295956964
# #program 3 
# number = [12,34,54,5,5345,24,32445,34,32,3445,6,6]
# try:
#     number1 = int(input("Enter index: "))
#     print(number[number1])
# except IndexError:
#     print("Index out of range")

# except ValueError:
#     print("Enter integer only")

#handle keyError in a dictionary

students = {
    "name" : "deepak",
    "age" : 12,
    "course" : "bca"
}

try:
    nam = input("Enter key name(name, age, course): ")
    print(students[nam])
except KeyError:
    print("sahi key dale")
except ValueError:
    print("yor input is no avl")


