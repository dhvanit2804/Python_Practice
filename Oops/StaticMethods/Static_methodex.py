class Sample:  # Sample is a class name 
    def display(self):  # display is a method   and self is a keyword 
        print("Hello")
        
    @staticmethod
    def output():
        print("Output Method")

    @staticmethod
    def demo():
        print("demo method this is ")

# obj creation 
obj = Sample() 
obj.display() 

Sample.output()
Sample.demo()