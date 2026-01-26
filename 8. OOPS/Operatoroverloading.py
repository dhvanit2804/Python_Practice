class Point:

    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y

    'Str Method is Called When we Print the object of class'
    def __str__(self):
        print("str called")
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,obj):
        print("Add called")
        x=self.x + obj.x
        y=self.y + obj.y
        return Point(x,y)
    
    def __sub__(self,obj):
        print("Sub called")
        x = self.x-obj.x
        y = self.y-obj.y
        return Point(x,y)

p1 = Point(10,20)
print(p1)

p2 = Point(30,40)
print(p2)

print(f"Addition Of Objects: {p1+p2}")
print(f"Subtraction Of Objects: {p1-p2}")