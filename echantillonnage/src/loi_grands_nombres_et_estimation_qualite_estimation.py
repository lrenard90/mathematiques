import random
from math import sqrt


def throw_dice(nb_experiences):
    return [random.randint(1, 6) for _ in range(nb_experiences)]


def count_success(results):
    return sum([1 for result in results if result in [1, 6]])


def estimate_experience(nb_experience, nb_experience_samples):
    frequences = [experience(nb_experience_samples) for _ in range(nb_experience)]
    seuil = 1 / (sqrt(nb_experience_samples))
    differences = [abs(frequence - 1/3) for frequence in frequences]
    print(f"Differences: {differences}")
    print(f"Proportion of cases where the difference is less than the threshold: {sum([1 for difference in differences if difference <= seuil]) / nb_experience}")

def main():
    experience(10)
    experience(100)
    experience(1000)
    experience(1000000)
    nb_experience = 100
    nb_experience_samples = 10000
    estimate_experience(nb_experience, nb_experience_samples)

def experience(nb_experiences):
    results = throw_dice(nb_experiences)
    print(results)
    successes = count_success(results)
    print(f"Number of successes: {successes}")
    frequence = successes / nb_experiences
    print(f"Probability of success: {frequence}")
    return frequence

    # Loi des grands nombres: la probabilité empirique converge vers la probabilité théorique

    # Estimation d'une probabilité: en répétant plusieurs fois une expérience aléatoire, on peut estimer la qualité de l'estimation de la probabilité
    # Probabilité thoérique: 1/3
    # Pour n suffisamment grand, la probabilité empirique converge vers la probabilité théorique
    # On veut calculer la proportion de cas où la fréquence p de l'expérience est suffisanmment proche de la probabilité théorique
    # Pour se faire, on va répéter plusieurs fois l"expérience et calculer la différence f-p entre la fréquence observée et la probabilité théorique
    # On veut minimiser cette différence. On va la comparer à 1/sqrt(n) pour n suffisamment grand

if __name__ == '__main__':
    main()