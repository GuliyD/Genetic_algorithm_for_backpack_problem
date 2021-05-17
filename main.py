from random import randint

BACKPACK = [[4, 12],
          [6, 3],
          [14, 3],
          [2, 12],
          [15, 14],
          [3, 15],
          [8, 12],
          [16, 3],
          [4, 1],
          [12, 10]]

MAX_WEIGHT = 68


class Genetic():
    def __init__(self, backpack: list, max_weight):
        self._backpack = backpack
        self._max_weight = max_weight
        self._chromosomes = []

    @property
    def backpack(self):
        return self._backpack

    @property
    def max_weight(self):
        return self._max_weight

    @property
    def chromosomes(self):
        return self._chromosomes

    def is_chromosome_overweighted(self, chromosome):
        weight = 0

        for i in range(len(self._backpack)):
            if chromosome[i] == 1:
                weight += self._backpack[i][0]

        if weight > self._max_weight:
            return True
        else:
            return False

    def create_chromosome(self):
        max_positive = randint(0, len(self._backpack))

        chromosome = [0 for i in self._backpack]
        chromosome_master = chromosome.copy()

        for i in range(max_positive):
            gen = randint(0, len(self._backpack) - 1)
            try:
                while chromosome[gen] == 1:
                    gen += 1
                else:
                    chromosome[gen] = 1

            except IndexError:
                gen = 0

                try:
                    while chromosome[gen] == 1:
                        gen += 1
                    else:
                        chromosome[gen] = 1
                except IndexError:
                    pass
            if self.is_chromosome_overweighted(chromosome):
                return chromosome_master
            chromosome_master = chromosome.copy()

        return chromosome_master

    def create_and_add_all_chromosomes(self):
        [self._chromosomes.append(self.create_chromosome()) for i in range(len(self._backpack))]


G = Genetic(BACKPACK, MAX_WEIGHT)
G.create_and_add_all_chromosomes()
print(G.chromosomes)
[print(G.is_chromosome_overweighted(i)) for i in G.chromosomes]
print(len(G.chromosomes))

