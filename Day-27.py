#========================OOp introduction - class and object=========================
class student:
    pass

s1 = student();     #student --> class
                    #s1 --> object

print(type(s1))

s1.name = "Deepak";
s1.age = 23;
print(s1.age);
#creating a class
class student:
    pass;


#creating object
class student:
    pass;

s1 = student();
s2 = student();


#checking object type
class studentss:
    pass;

si = studentss();
print(type(si));

#adding data to object
class student_data:
    pass;

s1 = student_data();
s1.name = "deepak";
s1.Class = "ug";
s1.age = 23;
l = s1.course = "bca"
print(l)


#multiple object
class student:
    pass;

s1 = student();
s2 = student();
s1.name = "dev";
s2.name = "depak";
print(s1.name)
print(s2.name)

#frist  usefull class
class student:
    def show(self):
        print("student information")


s1 = student()
s1.show()

#student class Example 
class student:
    def show(self):
        print("name ",self.name)
        print("age ", self.age)

s1 = student();
s1.name = "deepak";
s1.age = 34;
s1.show()

class employee:
    def emp(self):
        print("name: ",self.name);
        print("sallary: ",self.sallary);

s1 = employee();
s1.name = "mukesh";
s1.sallary = "30LPA"
s1.emp();

#program mobile information
class mobile_shop:
    def display(self):
        print("Brand: ",self.brand);
        print("price: ",self.price);

s1 = mobile_shop();
s2 = mobile_shop();
s1.brand = "sumsung";
s1.price = 23000;
s2.brand = "AI+ Nova 2";
s2.price = 15000;
s1.display();
s2.display();

#program car information

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

