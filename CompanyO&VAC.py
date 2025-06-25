class Company:
    def __init__(self,cname,clocation,cmanager):
        self.cname=cname
        self.clocation=clocation
        self.cmanager=cmanager

class Employees:
    def __init__(self,eid,ename,eage,comp:Company):
        self.eid=eid
        self.ename=ename
        self.eage=eage
        self.ecompany=comp
    def showDetails(self):
        print(f"name:{self.ename}\nage:{self.eage}\ncompany:{self.ecompany.cname}\nlocation:{self.ecompany.clocation}")

com_obj=Company("MNC","KADAVANTHARA","RAHUL")
e=Employees(1001,"sam",28,com_obj)
e.showDetails()