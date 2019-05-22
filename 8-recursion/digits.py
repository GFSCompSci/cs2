def digit(n):
    if n < 10:
        return 1
    else:
        return 1 + digit(n/10)
