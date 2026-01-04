from math import sqrt
import random
from typing import List, Callable, Any

class GamesResult:
    def __init__(self, results: List[int], success_condition: Callable[[int], bool]) -> None:
        self.results = results
        self.success_condition = success_condition

    def nb_successes(self) -> int:
        return len([ result for result in self.results if self.success_condition(result) ])
    
    def nb_throws(self) -> int:
        return len(self.results)
    
    def frequence_successes(self) -> float:
        return self.nb_successes() / self.nb_throws()
    
    def estimation_dispersion(self) -> float:
        return abs(1/5 - self.frequence_successes())
    
    def is_estimation_quality_good(self) -> bool:
        return self.estimation_dispersion() <= 1 / sqrt(self.nb_throws())
    
    def __str__(self) -> str:
        return f"GameResult(successes: {self.nb_successes()}, throws: {self.nb_throws()}, frequency: {self.frequence_successes():.3f}, estimation_dispersion: {self.estimation_dispersion():.3f}, estimation_quality: {self.is_estimation_quality_good()})"

# 1/5 chance of success
def games(nb_games: int) -> List[int]:
    return [ random.randint(1, 5) for _ in range(nb_games) ]

def compute_game_results(nb_experiences: int, nb_lancers: int) -> List[GamesResult]:
    gamesResults = [ GamesResult(games(nb_lancers), lambda result: result == 1) for _ in range(nb_experiences) ]
    return gamesResults

if __name__ == "__main__":
    game_results: List[GamesResult] = compute_game_results(10000, 100)
    for game_result in game_results:
        print(game_result)
    good_results: List[GamesResult] = [ game_result for game_result in game_results if game_result.is_estimation_quality_good() ]
    print(len(good_results) / len(game_results))