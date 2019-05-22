def hashkey(key):
    hashsum = 0
    for letter in key:
        hashsum += ord(letter)
    hashkey = hashsum % 26
    return hashkey

def createtable(n):
    hashtable = [''] * n
    return hashtable

hashtable = createtable(26)
print hashtable

key = 'abc'
value = 'xyz'
hashtable[hashkey(key)] = value

print hashtable[hashkey(key)]
print hashtable
