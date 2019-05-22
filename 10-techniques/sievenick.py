
def sieve(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
        # Update all multiples of p
            for i in range(p ** 2, n, p):
                prime[i] = False
        p += 1
    return [2] + [p for p in range(3, n, 2) if prime[p]]
