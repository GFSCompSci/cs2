class Hello:
    """A simple example class"""
    i = 0

    def __init__(self, x):
        self.data = ["I", "Love", "Classes!"]
        self.x = x

    def f(self):
        return 'Hello World!!!!!!!!!'

    def add(self):
        return self.x + 1

    def addi(self):
        return self.x + self.i

    def count(self):
        Hello.i += 1
        return Hello.i


object1 = Hello(3)
object2 = Hello(5)


print object1.count()
print object1.count()
print object1.count()
print object2.count()



# print x.f()
# print x.i
# print x.data
# print x.add()
# print x.addi()
