# example script for using RandomGen class

from collections import Counter
from src.random_gen import RandomGen


def main():
    values = [-1, 0, 1, 2, 3]
    probs = [0.01, 0.3, 0.58, 0.1, 0.01]

    gen = RandomGen(values, probs)
    results = [gen.next_num() for _ in range(100)]

    counts = Counter(results)
    for val in values:
        print(f"{val}: {counts[val]} times")


if __name__ == "__main__":
    main()
