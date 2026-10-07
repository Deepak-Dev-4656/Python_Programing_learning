#============================recursion Basics===========================
# def count():
#     print("hello")
#     count()
# count()
#---------------------------------
# def countdown(n):
#     if n == 0:
#         return
#     print(n)
#     countdown(n-1)
    
# countdown(6)
#---------------------recursion VS loop-------------------
#USING LOOP
# for i in range(6):
#     print(i)

#using recursion
# def countdown(n):
#     if n == 0:
#         return
    
#     countdown(n-1)
#     print(n)  
# countdown(5)
#-----------------------sum of n number------------------
# def sum_n(n):
#     if n == 0:
#         return 1
#     return n + sum_n(n-1)

# print(sum_n(6))
#--------------------Factorial------------------------
# def Factorial(n):
#     if n == 1:
#         return 1
#     return n * Factorial(n-1)

# print(Factorial(5))

#-----------------power function------------------------
def power(base,exp):
    if exp == 0:
        return 1
    return base*power(base,exp-1)

print(power(3,4))