"""
static method which is independent and not depedent on object 
which is access by directly class.


        @staticmethod
        methodname():
            pass 
"""

class Emplooye:
    language = "Python"
    salary = 1200000
    company = "Google"

    def get_info(self):
        print(f"The Language is {self.language}. Woqrk in {self.company} and Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")

dhvanit = Emplooye()
dhvanit.language = "React"

dhvanit.greet()
dhvanit.get_info()