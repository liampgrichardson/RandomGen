import random
import bisect
from math import isclose


class RandomGen:
    def __init__(self, random_nums, probabilities):
        if not isinstance(random_nums, list) or len(random_nums) == 0:
            raise ValueError("random_nums must be a non-empty list")
        if not isinstance(probabilities, list) or len(probabilities) == 0:
            raise ValueError("probabilities must be a non-empty list")
        if len(random_nums) != len(probabilities):
            raise ValueError("random_nums and probabilities must be of equal length")
        if not isclose(sum(probabilities), 1.0):
            raise ValueError("probabilities must sum to 1.0")

        self._random_nums = random_nums
        self._probabilities = probabilities
        self._cumulative_probs = self.compute_cumulative_probabilities(self._probabilities)

    @staticmethod
    def compute_cumulative_probabilities(probabilities):
        cumulative_probs = []
        total = 0.0
        for p in probabilities:
            total += p
            cumulative_probs.append(total)
        return cumulative_probs

    def next_num(self):
        r = random.random()  # will be in the range [0.0, 1.0)
        index = bisect.bisect_left(self._cumulative_probs, r)
        return self._random_nums[index]
