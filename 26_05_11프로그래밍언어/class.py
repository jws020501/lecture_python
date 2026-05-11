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

