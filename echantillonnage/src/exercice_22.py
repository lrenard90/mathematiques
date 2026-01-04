import random


def cartes(nb_throws):
    return [ random.randint(1, 12) for _ in range(nb_throws) ]

def count_successes(throws_results, success_condition):
    return len([ result for result in throws_results if success_condition(result) ])

def experience(nb_throws):
    throws = cartes(nb_throws)
    nb_successes = count_successes(throws, lambda result: result >= 10)
    print("Number of successes:", nb_successes)
    print("Frequence of successes:", nb_successes / nb_throws)

if __name__ == "__main__":
    experience(1000000)