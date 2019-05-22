allnums = range(1,100)
print allnums

evennums = range (2,100,2)
print evennums

oddnums = set(allnums) - set(evennums)
print oddnums

oddnums = list(oddnums)
print oddnums

newall = set(oddnums) | set(evennums)
print newall

print list(newall)
