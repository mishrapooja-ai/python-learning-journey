class  Person:
    def __init__(self,name):
        self.name=name
    def display(self):
            print("Name",self.name)
class Student(Person):
    def __init__(self,name,course):
        super().__init__(name)
        self.course=course
    def show_course(self):
         print("Course",self.course)
student1=Student("Pooja","Python")
student1.display()
student1.show_course()

            