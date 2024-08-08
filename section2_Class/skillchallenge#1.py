from random import choice
class Students:
    educational_platform = "Udemy"
    def __init__(self,name,age=23):
        self.age=age
        self.name=name
 
 
    def greeting(self):
        greetings=[
            '''Hi, I'm {}''',
            '''Hey there, my name is  {}''',
            '''Hi, Oh, my name is {}''',
        ]
        greet=choice(greetings)
        return greet.format(self.name)
 
def class_create(student_names):
    return [Students(name) for name in student_names]
 
 
   
name=["Abdul", "Hadi", "Shoaib", "ammad"]
for student in class_create(name):
    print(student.greeting())
 