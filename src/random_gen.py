"""
random_gen.py

This module defines the RandomGen class, which generates random numbers based on
a user-defined discrete probability distribution.
"""

import random
import bisect
from math import isclose
from itertools import accumulate


class RandomGen:  # pylint: disable=too-few-public-methods
    """
    A generator that returns numbers from a predefined list based on their associated probabilities.
    """
    def __init__(self, random_nums: list[int], probabilities: list[float]):
        """
        Initialize the generator.

        Args:
            random_nums (List[int]): List of numbers to choose from.
            probabilities (List[float]): Corresponding probabilities for each number.

        Raises:
            ValueError: If input validation fails.
        """
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
        self._cumulative_probs = list(accumulate(self._probabilities))

    def next_num(self) -> int:
        """
        Returns a random number based on initialized probabilities.

        Returns:
            int: A randomly chosen number from 'random_nums'.
        """
        r = random.random()  # will be in the range [0.0, 1.0)
        index = bisect.bisect_left(self._cumulative_probs, r)
        return self._random_nums[index]
