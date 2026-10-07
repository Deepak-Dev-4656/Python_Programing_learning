#====================Function===================
def addition(a,b):

    return a+b;

a=addition(2,3)
print(a)
#---------Dictionary print using Function----------------
student = {
    "name" : "deepak",
    "course" : "BCA",
    "age" : 12,
    "city" : "godda",
    "pass" : True
}
def Dictionary(dis):
    for key,value in dis.items():
        print(key,":",value)

Dictionary(student)
#-------------print array using function----------------------
a = [12,12,43,43,534,"deepak","mango"]


def view_array(arr):
    for i in arr:
        print(i, end = ", ")

view_array(a)

