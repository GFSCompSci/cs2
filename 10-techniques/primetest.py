from primes import primecheck, sieve
import time

n = 1000000

print "Primechecking method"
start = time.clock()
for i in range(n+1):
    if primecheck(i): print i
timeTotalc = time.clock() - start
print

print
print "Sieve method"
start = time.clock()
primelist = sieve(n)
for i in primelist: print i
timeTotals = time.clock() - start
print
print
print "Primecheck took %f seconds to run." %(timeTotalc)
print "Sieve took %f seconds to run." %(timeTotals)
print
