def suite(n):
    if n == 0:
        return 3
    return 2*suite(n-1) - 2

def rang_superieur_a_valeur(valeur):
    rang = 0
    terme = 0
    while terme < valeur:
        terme = suite(rang)
        rang += 1
    return rang - 1

print("Rang à partir duquel les termes de la suite sont strictement supérieurs à 10^20 :", rang_superieur_a_valeur(10**20))