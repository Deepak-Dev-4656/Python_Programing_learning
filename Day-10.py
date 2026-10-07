#================Revision + practice Day===============
#----------------------------
#print hello world
# print("hello world")
# #----------------------------
# #Add two number
# a = 12;
# b = 23;
# c = a + b;
# print("sum of two number: ", c);
# #----------------------------
# #Even odd
# num = int(input("Enter a number: "));
# if num % 2 != 0:
#     print("Odd number!")
# else:
#     print("Even number!")

# #----------------------------
# #positiv negative or zero
# numA = int(input("Enter a number: "))
# if numA > 0:
#     print("Number is a positive!")
# elif num < 0:
#     print("Number is a negative!")
# else:
#     print("Number is Zero!")

# #----------------------------
# #largest of two number
# num1 = int(input("Enter a frist number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print("frist number is largest: ",num1)
# else:
#     print("Second number is largest: ",num2)

#----------------------------
#Largest of three number
# num_1 = int(input("Enter a frist number: "))
# num_2 = int(input("Enter a second number: "))
# num_3 = int(input("Enter a third number: "))

# if num_1 > num_2 and num_1 > num_3:
#     print("number 1 is a largest number: ",num_1)
# elif num_2 > num_3:
#     print("Number 2 is a largest number: ",num_2)
# else:
#     print("third number is largest number: ",num_3)
# #----------------------------
# #table of a number 
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n*i)
# #----------------------------

# h = int(input("Enter a number: "))
# g = 0;
# for i in range(1, h+1):
#     g+=i
# print(g);

#----------------------------
#Reverse a string
# s = input("Enter a text: ")
# print(s[::-1])
# print(s == s[::-1])
#----------------------------
#count character in string
# a = input("Enter a sentence: ")
# count = 0
# for ch in a:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)

#----------------------------
#print star pattern
# for i in range(1, 7):
#     print("*"*i)

#----------------------------
#while loop counting
# i = 1
# while i <= 5:
#     print(i)
#     i+=1

#----------------------------
#use of break
# for i in range(1, 10):
#     if i == 6:
#         break
#     print(i)
    
#----------------------------
#use of continue
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

#----------------------------
#multipale input
a,b = map(int,input("abc").spli())
print(a+b)
