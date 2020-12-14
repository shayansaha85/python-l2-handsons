import math


class sqroot:
    def sqroot(self,a):
        print(math.sqrt(a))


class addition:
    def add(self,a,b):
        print(a+b)


class subtraction:
    def sub(self,a,b):
        print(a-b)


class multiplication:
    def mult(self,a,b):
        print(a*b)


class division:
    def div(self,a,b):
        print(a/b)


class mathnew(sqroot, addition, subtraction, multiplication, division):
    def __init__(self):
        super()


m = mathnew()

m.sqroot(4)
m.add(4,5)
m.sub(5,8)
m.mult(5,6)
m.div(47,2)
