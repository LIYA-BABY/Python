class A:
    def fun1(self):
        print("function 1 working")
    def fun(self):
        print("Funtion 2 working")
class B(A):
    def fun3(self):
        print("function 3 working")
    def fun(self):
        print("Funtion 4 working") 

b=B()
b.fun1()
b.fun3()
b.fun()