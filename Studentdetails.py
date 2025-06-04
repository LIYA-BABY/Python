class Student:
    def __init__(self, name, address, classroom, dob, admissionnumber):
        self.n = name
        self.ad = address
        self.d = dob
        self.c = classroom
        self.m = {}  ##marksheet - dictionary##
        self.a = admissionnumber

    def UpdateClassroom(self, newClassroom):
        self.c = newClassroom

    def UpdateAddress(self, newAddress):
        self.ad = newAddress

    def AddSubject(self, subjectName, marks):
        self.m[subjectName] = marks

    def AddSubject(self, subjectName, marks=0):
        self.m[subjectName] = marks

    def UpdateScore(self, subject, newMarks):
        self.m[subject] = newMarks

    def __str__(self):
        return f" Name : {self.n}\n Address : {self.ad}\n Dob : {self.d}\n Addmission NO : {self.a}\n Class : {self.c}\n Marksheet :{self.m} \n"


S = Student("ANJU", "adivadu", "18", 1223, "BCA")
print(S)
# S.UpdateClassroom('ABC')
# print(S)
# S.UpdateAddress('QAW')
# print(S)
# S.AddSubject('ENGLISH')
# print(S)
