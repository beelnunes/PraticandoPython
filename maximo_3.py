def maximo(n,p,q):
    if (n > p) and (n > q):
        return n
    if (p > n) and (p > q):
        return p
    if (q > p) and (q > n):
        return q
    if (p == q) and (q == n):
        return n

a = maximo(7,7,7)
b = maximo(0,-1,-4)

print(a,b)
