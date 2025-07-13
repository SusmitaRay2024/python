class Test:
    x = 5
    def __init__(self, a, b):
        self.a = a
        self.b = b
    #Instance method
    def show(self):
        print(self.a, self.b)
    @staticmethod
    def f2():
        print("Hello")
    @classmethod
    def f3(cls):
        print(cls.x)
        
        
t1 = Test(3,4)
t2 = Test(5,6)
t1.show()
t2.show()
Test.f3()
Test.f2()
t1.f2()
