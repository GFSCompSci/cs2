from random import randint as rand

def listGen(n):
    randlist = []
    for i in range(n):
        randlist.append(rand(1,100))
    return randlist
