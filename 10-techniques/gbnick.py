import time

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

start = time.clock()

maxnum = 10000
allnum = range(3,maxnum,2)
primenum = primes(maxnum)
comp = list(set(allnum) - set(primenum))
comp.sort()


for i in comp:
    answer = i
    conj = False
    top = int((i/2)**0.5)+1
    for j in range(1,top):
        sqr = 2*(j**2)
        if (i - sqr) in primenum:
            conj = True
            break
    if conj == False: break

print answer

timeTotal = time.clock() - start

print "Program took %f seconds to run." %(timeTotal)
