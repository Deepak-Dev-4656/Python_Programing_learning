#========================sets====================
num = {12,34,54,23,23,12,45}
print(num)
fruits = {"apple", "banana", "mango"}
print(fruits)
numbers = set([1,2,4,2,56,23,23])
print(numbers)


for i in num:
    print(i)
#---------------------------------------
#Adding element
nums = {1,2,3,4,5}
print(nums.add(41))
#---------------------------------------
#update() method
print(nums)
d = nums.update([9,7,6,98])
print(nums)
#---------------------------------------
#REmoving elements
n  = {1,2,3,4,5,6,7,}
n.remove(4)
print(n)
#---------------------------------------
#discard method
na = {1,2,3,4,5,6,7,7}
na.discard(9)
print("na=:",na)
#---------------------------------------
#pop() method
nb = {1,23,4,5,6,7,8}
nb.pop()
print(nb)
print(4 in nb)
ns = int(input("Enter a number: "))
if ns in nb:
    print("set is find ",ns)
else:
    print("set is not found!")
#---------------------------------------
#lenth of set
nc = {1,2,3,4,5,6,7,8}
print(len(nc))
#---------------------------------------
#union of sets
a = {12,42,65,78,56}
b = {21,45,34,67,87}
result = a.union(b)
print(result)
#---------------------------------------
#intersection of seta
c = {12,44,24,35,65,76}
d = {12,654,78,35,65,34,656,34}
f = c.intersection(d)
print("intersection: ",f)
#---------------------------------------
#sets in data analytics
web_user = {"sudama","dev","rajiv","deepak"}
app_user = {"imrankhan","dev","sohan","rajiv"}
comn_user = web_user & app_user
print(comn_user)
