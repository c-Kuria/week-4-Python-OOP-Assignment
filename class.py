class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old and I'm a {self.gender}.")
        
p1 = Person("Brian", 20, "Male")
p1.introduce()