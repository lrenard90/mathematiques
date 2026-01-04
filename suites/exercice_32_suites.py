def seuil(a):
    n = 0
    while (n+2)/(n+1) > a:
        n = n + 1
    return n

print(seuil(1.01))