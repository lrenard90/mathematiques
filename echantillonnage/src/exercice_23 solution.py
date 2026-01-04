from math import sqrt
import random
from typing import List, Callable, Any

# Yvan Monka solution
def jeu(N: int) -> int:
    results = [ random.randint(1, 5) for _ in range(N) ]
    return results.count(1) / N

def estim(N: int) -> float:
    c = 0
    for k in range(N):
        # For each iteration, simulate 1000 games to get a frequency
        f = jeu(100)
        if abs(f - 1/5) <= 1 / sqrt(100):
            c += 1
    return c/N

if __name__ == "__main__":
    result = estim(10000)
    print(f"{result:.2f}")