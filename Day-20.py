# #==================Dictionary==================
# #characteristics of dictionary
# student = {
#     "name" : "deepak",
#     "age" : 18,
#     "course" : "python"
# }

# student["name"] = "dev"
# print(student)
# for i in student:
#     print(i)
# #----------------------------------------------
# #creating a dictionary
# #method 1
# student = {
#     "name" : "deepak",
#     "age" : 18,
#     "course" : "python"
# }
# # method 2
# student = dict(
#     name = "Deepaak",
#     age = 18
# )
# #----------------------------------------------
# #Accessing values

# students = dict(
#     name = "Deepak kumar",
#     age = 17
# )

# print(student["name"])
# for i in students:
#     print(i)

#----------------------------------------------
#using get()
student = {
    "name" : "deepak",
    "age" : 18,
    "course" : "python"
}

# print(student.get("name"))
# print(student["age"])
# print(student)

#--------------add items & delete
# student["city"] = "Godda"
# del student["city"]

# for i in student.items():
#     print(i, end = "\n")
# #----------print key values----------
# for key, value in student.items():
#     print(key,":",value)

def di(dis):
    for key,value in dis.items():
        print(key,":",value)

di(student)



# #------------find age----------------
# if "age" in student:
#     print("finded age: ",student["age"])
# #----------------------------------------------
# i = int(input("eneter your age: "))
# if i == student["age"]:
#     print("yes")
#------------------user input in dictionary-------------------
# std = {}
# std["name"] = input("Enter your name: ")
# std["age"] = int(input("Enter your age: "))
# std["course"] = input("Enter your course: ")

# def std_print(_std):
#     for key, value in _std.items():
#         print(key,"-->",value)
        

# std_print(std)

stu = {
    "name" : "deepak",
    "age" : 12,
    "bool" : True,
    "course" : "BCA"
}
ih = input("enter name: ")
if ih == stu["name"]:
    print("hello ",ih)
else:
    print("bye")