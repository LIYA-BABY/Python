def method_decorator(func):
    def wrapper(self,name):
        print("Before method execution")
        res=func(self,name)  
        print("After method execution")
        return res
    return wrapper
class MyClass:
    @method_decorator
    def say_hello(self,name):
        print(f"Hello!",name)

obj = MyClass()
obj.say_hello("HANNA")