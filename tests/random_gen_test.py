"""
Unit tests for the RandomGen class.
"""

import unittest
from collections import Counter
from src.random_gen import RandomGen


class TestRandomGen(unittest.TestCase):
    """Tests for the RandomGen class."""

    def test_basic_distribution(self):
        """Check that generated numbers roughly match the given probabilities."""
        nums = [-1, 0, 1, 2, 3]
        probs = [0.01, 0.3, 0.58, 0.1, 0.01]
        gen = RandomGen(nums, probs)

        results = [gen.next_num() for _ in range(10000)]
        counts = Counter(results)

        for num, prob in zip(nums, probs):
            observed_ratio = counts[num] / 10000
            self.assertAlmostEqual(observed_ratio, prob, delta=0.03)

    def test_empty_input_raises(self):
        """Empty input lists should raise ValueError."""
        with self.assertRaises(ValueError):
            RandomGen([], [])

    def test_mismatched_lengths_raises(self):
        """Mismatched input list lengths should raise ValueError."""
        with self.assertRaises(ValueError):
            RandomGen([1, 2], [0.5])

    def test_more_probs_than_values_raises(self):
        """More probabilities than values should raise ValueError."""
        with self.assertRaises(ValueError):
            RandomGen([1], [0.5, 0.5])

    def test_probabilities_sum_greater_than_one_raises(self):
        """Probabilities summing to more than 1.0 should raise ValueError."""
        with self.assertRaises(ValueError):
            RandomGen([1, 2], [0.5, 0.6])

    def test_probabilities_sum_less_than_one_raises(self):
        """Probabilities summing to less than 1.0 should raise ValueError."""
        with self.assertRaises(ValueError):
            RandomGen([1, 2], [0.3, 0.6])  # sum = 0.9 < 1.0

    def test_single_value_always_returns_that_value(self):
        """A generator with one value and probability 1.0 should always return that value."""
        gen = RandomGen([42], [1.0])
        for _ in range(10):
            self.assertEqual(gen.next_num(), 42)


if __name__ == '__main__':
    unittest.main()
