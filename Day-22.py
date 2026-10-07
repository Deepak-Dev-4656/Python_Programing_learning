#====================fUnction calculator====================
def add(a,b):
    return a+b;
def subtraction(a,b):
    return a-b;
def multiplication(a,b):
    return a*b;
def divsion(a,b):
    return a/b;

print("1. ADDITION \n 2. subtraction \n3. multiplication \n 4,division")

choice = int(input("Enter your choice: "));
num1 = float(input("Enter your fridt digit: "))
num2 = float(input("Enter your second digit: "))

if choice == 1:
    print("result = ",add(num1,num2))
elif choice == 2:
    print("result = ", subtraction(num1,num2))
elif choice == 3:
    print("result = ",multiplication(num1,num2))
elif choice == 4:
    print("result = ",division(num1,num2))
else:
    print("invalid!")