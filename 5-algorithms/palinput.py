#!/usr/bin/python

def pal(n):
  ls = str(n)
  r = int(len(ls)/2)

  for x in range(1,r+1):
    if ls[x-1] != ls[len(ls)-x]:
      return False
  return True

highpal=0

n = int(raw_input("Input range:"))

for i in range(1, n):
  for j in range (1, n):
    num = i * j
    if pal(num) == True and num > highpal:
      highpal = num
print(highpal)
