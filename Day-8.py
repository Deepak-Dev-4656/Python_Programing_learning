#===============String=================
name = "Deepak"
sub = "BCA"
message ="This is a string"

print(name)
print(name[0])
print(name.upper())
print(name[1:4])
print(name[0:])
print(name[:5])

print(message.split(","))
print(name+ " "+sub)
print(name*2)

print(message[::-1])
j = message.replace("string","python programaing language")
print(j)
print(message.find("string"))
print(message.find("This"))
text = input("Enter a string: ")
if text == text[::-1]:
    print("palindrom")
else:
    print("Not palindrom")