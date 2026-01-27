from abc import ABC, abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(self,r):
        pass

class SBI(RBI):

    def show(self):
        print("Hi, I am SBI")

    def roi(self,r):
        print(f"Rate Of Interest Given By SBI Is : {r}")

class HDFC(RBI):

    def show(self):
        print("Hi, I am HDFC")

    def roi(self,r):
        print(f"Rate Of Interest Given By HDFC Is : {r}")

s=SBI()
s.show()
s.roi(7.5)

h=HDFC()
h.show()
h.roi(8.2)