import time
from listgen import listGen
from qsort import quicksort
from selsort import *

n = 100000

newlist = listGen(n)
print
start = time.clock()
selectionSort(newlist)
timeTotal = time.clock() - start
print "Selection sort took %f seconds to run." %(timeTotal)
print
newlist = listGen(n)
start = time.clock()
quicksort(newlist)
timeTotal = time.clock() - start
print "Quicksort took %f seconds to run." %(timeTotal)
