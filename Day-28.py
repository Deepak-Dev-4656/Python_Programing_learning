#constructor with multiple parameters
# class student:
#     def __init__(self,name,age):
#         self.name = name;
#         self.age = age;

# s1 = student("deepaka",29);
# print(s1.name)
# print(s1.age)

#creating multiple object
# class student:
#     def __init__(self,name,age):
#         self.name = name;
#         self.age = age;

# s1 = student("Deepak",89);
# s2 = student("Rahul",57)

class student:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

s1 = student("Deepak",89);
s2 = student("Rahul",57)
print(s1.name)
print(s1.age)
class showroom:
    def display(self):
        print("brand_name: ",self.brand_name);
        print("color: ",self.color);
        print("price",self.price);

s1 = showroom();
s2 = showroom();
s1.brand_name = "toyota";
s1.color = "blue";
s1.price = 20000000;
s2.brand_name = "suzuki";
s2.color = "white";
s2.price = 1000000;

s1.display();
s2.display();
#%%
class student:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

    def display(self):
        print("usr name: ",self.name);
        print("user age: ",self.age);

s1 = student("Deepak",89);
s2 = student("Rahul",57)
s1.display();
s2.display()

class car:
    def __init__(self,Brand,color,price):
        self.Brand = Brand;
        self.color = color;
        self.price = price;

    def disply(self):
        print("car Brand name:",self.Brand);
        print("car color",self.color);
        print("car price",self.price);

s1 = car("suzuki","red",200000);
s2 = car("suzuki","blue",200000);
s3 = car("lamborghini","red",200000);
s1.disply();
s2.disply();
s3.disply();

#%%
class student:
    def __init__(self,name,age,course):
        self.name = name;
        self.age = age;
        self.course = course;

    def display(self):
        print("student name: ",self.name);
        print("student age: ",self.age);
        print("student course: ",self.course);

s1 = student("deepak",23,"BCA")
s2 = student("dev",21,"DIPLOM")
s1.display();
s2.display();


class Rectangle:
    def __init__(self,width,height):
        self.width = width;
        self.height = height;

    def display(self):
        print("Rectangle Area: ",self.width*self.height);

s1 = Rectangle(5,5);
s1.display();
