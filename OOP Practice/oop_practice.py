class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
            print("Hello, My name is",self.name)
      
        
student1=Student("Pooja",26)
student2=Student("Priya",23)
student1.introduce()   
student2.introduce()  
    

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
