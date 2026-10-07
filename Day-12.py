#==================List program=====================
numbers = [10,22,12,35,32,24]
name = ["mohan", "dev", "DeepakXdev", "mohit", "ronak"]
mixed = [10,"dev",23.2, 'rakhi',45,True,False,]

#----------------------------------------------------
#1. sum of element in a list
"""
The sum function is used to calculate the total of 
all numbers in a list 
"""
# sum_num = sum(numbers)
# print("sum = ",sum_num)
#----------------------------------------------------
#maximum element in a list
"""the max() function returns  the largest value fromk
the list"""

# max_num = max(numbers)
# print("maximum number = ",max_num)
#----------------------------------------------------
#minimum element in a list
"""The min() function returns the smalest value from 
the list"""
# min_num = min(numbers)
# print("minimum number = ",min_num)
#----------------------------------------------------
#Search an element in a list
""" We can check whether an element exists in a list using the in keyword"""

# search = int(input("enter a number: "))
# if search in numbers:
#     print("number find", search)
# else: 
#     print("number not found!")
#----------------------------------------------------
#5. searching Element with index
"""we can also find position of on element using the index() method"""

print("Element position",numbers.index(22))

