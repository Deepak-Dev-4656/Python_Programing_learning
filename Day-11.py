#===========list=============
numbers = [10,22,12,35,32,24]
name = ["mohan", "dev", "DeepakXdev", "mohit", "ronak"]
mixed = [10,"dev",23.2, 'rakhi',45,True,False,]

print(numbers[2:-2])
for i in name:
    print(i,end = " ,")
print()
mixed.append(111)
name.sort()
mixed.insert(2,0.98)
mixed.remove(45)
print(mixed)
print(name)
