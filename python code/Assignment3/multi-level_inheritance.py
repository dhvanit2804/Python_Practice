class GrandParent:
    def gp(self):
        print("GrandParent Class")

class Parent(GrandParent):
    def p(self):
        print("Parent Class")

class Child(Parent):
    def c(self):
        print("Child Class")

obj = Child()
obj.gp()
obj.p()
obj.c()