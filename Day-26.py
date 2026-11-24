#==============Fiile handling=====================
"""1. File handling allows a python program to store permanentaly in a file
"""
    #without file handling
name = "Deepak"
    #when program closes:
    #data is lost

    #with file handling
file = open("names.txt","w")
file.write("Deepak")

"""
2. Why use file handling
    saving student record
    saving password
    storing logs
    storing reports
    Database(basic level)

3. Types of files
    text file
        student.txt
        notes.txt
        data.txt
        store normal text.
    Binary file
        image.jpg
        video.mp4
        song.mp3
        --store binary data for
          day-26focus on text file

4. opening a file
Syntax :
    open(filename,mode)
Example:
    file = open("student.txt","r")

5. File mode(r)
    r       read
    w       write
    a       append
    x       creat new file
    most important
    r ---> Read
    w ---> write

"""
#7. write mode
file = open("names.txt","w")
file.write("name: Deepak\nage: 18\n")
file.close()


#6. read mode
file = open("names.txt","r")
data = file.read()
print(data)
# student = {
#     "name" : "Deepak",
#     "age" : 18,
#     "course" : "BCA"
# }

# lst = [12,34,True,"Dev"]
#Better Method: with

with open("names.txt","w") as file:
    file.write("python ||")
    file.write("java ||")
    file.write("c++\n")

with open("names.txt","r") as file:
    print(file.read())


with open("names.txt","w") as file:
    name = input("Enter your course name:")
    agea = int(input("Enter you age: "))
    file.write(f"Course: {name}\n")
    file.write(f"Age: {agea}")


with open("names.txt","r") as file:
    print(file.read())
    