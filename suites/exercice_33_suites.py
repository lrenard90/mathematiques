def u(u0, n):
    u = u0
    for i in range(n):
        u = 0.9 * u + i
    return u

def superieur_100(u0):
    u = u0
    i = 0
    while u < 100:
        u = 0.9 * u + i
        i += 1
    return i

print(u(5, 0))
print(u(5, 7))
print(u(5, 10))
print(superieur_100(3))