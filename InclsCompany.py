class Employees:
    class Company:   
        def __init__(self, cname, clocation, cmanager):
            self.cname = cname
            self.clocation = clocation
            self.cmanager = cmanager
    def __init__(self,eid,ename,eage,cname,cman,cloc):
        self.eid=eid
        self.ename=ename
        self.eage=eage
        self.ecompany=Employees.Company(cname,cman,cloc) 
    def showDetails(self):
        print(f"name:{self.ename}\nage:{self.eage}\ncompany:{self.ecompany.cname}\nlocation:{self.ecompany.cmanager}")
e=Employees(1001,"sam",28,"MNC","KADAVANTHARA","RAHUL")
e.showDetails()