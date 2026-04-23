class Demo:
    def add(self, a=None, b=None, c=None):
        if a and b and c:
            return a+b+c
        elif a and b:
            return a + b
        else:
            return a
        
obj = Demo()
print(obj.add(10, 20, 30))
print(obj.add(10, 20))
print(obj.add(10))