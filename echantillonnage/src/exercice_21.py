import random

def bille_roulette(nb_throws, success_condition):
  return [ random.randint(0, 36) for _ in range(nb_throws) ]

def count_successes(success_condition, throws_results):
    return len([ result for result in throws_results if success_condition(result) ])

def experience(nb_throws):
    throws = bille_roulette(nb_throws, lambda result: 1 <= result <= 12)
    nb_successes = count_successes(lambda result: 1 <= result <= 12, throws)
    print("Number of successes:", nb_successes)
    print("Frequence of successes:", nb_successes / nb_throws)

experience(1000)
experience(1000000)