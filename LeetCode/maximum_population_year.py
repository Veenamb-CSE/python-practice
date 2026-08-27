class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_population = 0
        answer = 1950

        for year in range(1950, 2051):
            population = 0

            for birth, death in logs:
                if birth <= year < death:
                    population += 1

            if population > max_population:
                max_population = population
                answer = year

        return answer
        
