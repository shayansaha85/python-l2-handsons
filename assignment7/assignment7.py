class First(object):
    def method1(self):
        print("first")

class Second(First):
    def method1(self):
        print("second")

class Third(First):
    def method1(self):
        print("third")

class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print("that's it")

f = Fourth()
f.method1()