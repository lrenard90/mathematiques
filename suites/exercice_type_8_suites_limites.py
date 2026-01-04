def suite_recurrente(n):
    if n == 0:
        return 2
    return 0.9*suite_recurrente(n-1) + 1

rang = 0
terme = 0
while terme < 8:
    terme = suite_recurrente(rang)
    print(f"U({rang}) = {terme}")
    rang += 1
    
print("Rang à partir duquel les termes de la suite sont strictement supérieurs à 8 :", rang - 1)