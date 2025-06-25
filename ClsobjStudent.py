class Student:
    school="ASK HSS"
    def __init__(self,roll,studyclass,name,age,teacher):
        self.rollno=roll
        self.studycls=studyclass
        self.name=name
        self.age=age
        self.teacher=teacher
    def display(self):
        print(f'rollno:{self.rollno} study in class :{self.studycls} with name:{self.name} '
              f'and age:{self.age},and the class teacher is:{self.teacher} in the school is named as {self.school}\n') 
    def set_marks(self,english,maths,malayalam,science):
        self.eng=english
        self.maths=maths
        self.malayalam=malayalam
        self.science=science
    def get_average(self):
        return(self.eng+self.maths+self.malayalam+self.science)/4

s1=Student(roll=10,studyclass="5th",name="John",teacher="Asif",age=10)
s1.display()
s1.set_marks(english=80,maths=45,malayalam=90,science=75)
print(f" Average mark of {s1.name} is ",s1.get_average())

print("-----------------------------------------------------------------")


s2=Student(15,"6th","Akash",17,"Roshin")
s2.display()
s2.set_marks(english=90,maths=95,malayalam=70,science=85)
print(f" Average mark of {s2.name} is",s2.get_average())