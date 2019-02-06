#!/usr/bin/python

import sys
import time

def ctime(n):
    n = n+1
    n = n+1
    return


def ntime(n):
    for i in range(1, n):
        num = i
    return

def n2time(n):
    for i in range(1, n):
      for j in range (1, n):
        num = i * j
    return



if __name__ == '__main__':
    args = sys.argv

    start_time = time.time()
    ctime(int(args[1]))
    print("Constant Time: --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    ntime(int(args[1]))
    print("O(n) Time: --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    n2time(int(args[1]))
    print("O(n^2): --- %s seconds ---" % (time.time() - start_time))
