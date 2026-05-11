#magic mathod 연습
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        return False
    
p1 = Person("홍길동",15)
print(p1)

p2 = Person("홍길동",20)
print(p2)

print(f"{p1}과 {p2}: ",end="")

print("같은사람입니다") if p1==p2 else print("다른사람입니다")



# 학습내용 되돌아보기 
# 1-1
class TV:
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self,color):
        self.color = color

#1-2

class TV:
    cnt_products = 0

    def __init__(self, size):
        self.size = size
        TV.cnt_products += 1

main = TV(60)
print(TV.cnt_products)

#2
class Integer:
    def __init__(self,value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
    def  __sub__(self, other):
        return self.value - other.value
    
a = Integer(5)
b = Integer(3)

print(a+b) #8
print(a-b) #2

#3
class Student:
    def __init__(self,univ,name):
        self.univ = univ
        self.name = name
    
    def __str__(self):
        return f"대학: {self.univ} 이름: {self.name}"

print(Student("한국대학교","이성실"))

#4
class Student:
    def __init__(self,name,dept,mid,final):
        self.name = name
        self.dept = dept
        self.mid = mid
        self.final = final
        self.avg = (mid+final)/2
    
    def __str__(self):
        return f"학과: {self.dept} 이름: {self.name} 중간: {self.mid} 기말:{self.final}"
    
    def grade(self):
        self.gd = ""
        if self.avg >= 90:
            self.gd = "A"
        elif self.avg>=80:
            self.gd = "B"
        elif self.avg>=70:
            self.gd = "C"
        elif self.avg>=60:
            self.gd = "D"
        else:
            self.gd = "F"

        return f"학점: {self.gd}"
    

student1 = Student("김경철","기계학과",89,90)

print(student1)
print(student1.grade())

#5
class Car:
    def __init__(self,company,year,color):
        self.company = company
        self.year = year
        self.color = color
    def __str__(self):
        return f"자동차회사: {self.company}, 년식: {self.year}, 색상: {self.color}"
    def __eq__(self, value):
        if self.company == value.company and self.year == value.year and self.color == value.color:
            return True
        else:
            return False

mycar = Car("현대",2020,"검정")
yourcar = Car("기아",2021,"백색")

print(mycar)
print(yourcar)
print(mycar == yourcar)