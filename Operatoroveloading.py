class Product:
    def __init__(self,pname,pprice):
        self.name=pname
        self.price=pprice
    def __add__(self, other):
        total_price=self.price+other.price
        print(total_price)
p1=Product("TAB",12000)
p2=Product("Camera",22000)
p3=Product("Mobile",22000)
p1 + p2