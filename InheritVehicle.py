class Vehicle:
    def __init__(self,company,model,color,engine,fuel):
        self.c=company
        self.m=model
        self.co=color
        self.e=engine
        self.f=fuel
    def start_engine(self):
        print("ENGINE is started....")
    def change_gear(self):
        print("Changing the gear")
class Car(Vehicle):                         
    def open_sunroof(self):
         print("Car sunroof is opened...!!!")
    def show(self):
        print(f"car company :{self.c}\n car model : {self.m}")
c=Car("BMW","T5","MAROON","E2000","DIESEL")         
c.start_engine()
c.change_gear()
c.open_sunroof()
c.show()