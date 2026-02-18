def suite(rang):
    if rang == 0:
        return 2
    return 0.2*suite(rang - 1) + 1

# Somme de U0 à Urang
def somme(rang):
    somme = 0
    for i in range(rang + 1):
        somme += suite(i)
    return somme

print("somme(10) = ", somme(10))