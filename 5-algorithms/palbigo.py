#!/usr/bin/python

def pal(n):
  ls = str(n)
  r = int(len(ls)/2)

  for x in range(1,r+1):
    if ls[x-1] != ls[len(ls)-x]:
      return False
  return True

highpal=0

for i in range(100, 999):
  for j in range (100,999):
    num = i * j
    if pal(num) == True and num > highpal:
      highpal = num
print(highpal)

