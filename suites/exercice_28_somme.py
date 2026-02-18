import re


def suite(n):
    if n == 0:
        return 1
    return 3 * suite(n - 1) - 1

def somme(rang_cible):
    somme = 0
    for n in range(rang_cible + 1):
        somme += suite(n)
    return somme

print(somme(14))