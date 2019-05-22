val1 = input("Enter first number: ")
val2 = input("Enter second number: ")
if (val2 > val1): val1, val2 = val2, val1

print "a = %i b = %i" %(val1, val2)

print "Divide and conquer!"

a = val1
b = val2

while (b !=0): a, b = b, a%b

print "GCD is %i" %a
