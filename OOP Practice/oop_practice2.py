class Person:
    def walk(self):
        print("Person is Walking") 
class Teacher(Person):
    def teach(self):
        print("Teacher is Teaching") 
teacher1=Teacher()
teacher1.walk() 
teacher1.teach()              