import unittest
from solve.selection import statistic

class StatisticTestCase(unittest.TestCase):
    def test_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = statistic(arr, 4, 54)
        self.assertEqual(result, 3)

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            statistic([1, 2, 3], 0)

    def test_example_ranks(self):
        original = [12, 71, 35, 80, 61, 50, 87, 11, 20]
        expected = {1: 11, 4: 35, 9: 87}
        for k, exp in expected.items():
            with self.subTest(k=k):
                values = original[:]
                self.assertEqual(statistic(values, k, seed=1), exp)

    def test_single_element(self):
        self.assertEqual(statistic([7], 1, seed=1), 7)

    def test_small_sizes(self):
        for n in range(2, 6):
            original = list(range(n, 0, -1))  # обратный порядок
            for k in range(1, n + 1):
                with self.subTest(n=n, k=k):
                    values = original[:]
                    self.assertEqual(
                        statistic(values, k, seed=1),
                        sorted(original)[k - 1]
                    )

    def test_negatives_and_repeats(self):
        original = [-5, -5, 0, 3, -1, 3]
        for k in range(1, len(original) + 1):
            with self.subTest(k=k):
                values = original[:]
                self.assertEqual(
                    statistic(values, k, seed=1),
                    sorted(original)[k - 1]
                )

    def test_all_same(self):
        original = [4, 4, 4, 4]
        for k in range(1, 5):
            with self.subTest(k=k):
                values = original[:]
                self.assertEqual(statistic(values, k, seed=1), 4)

    def test_all_ranks_several_seeds(self):
        original = [5, -1, 2, 2]
        expected = sorted(original)
        for seed in (1, 2, 3):
            for k in range(1, len(original) + 1):
                with self.subTest(seed=seed, k=k):
                    values = original[:]
                    result = statistic(values, k, seed=seed)
                    self.assertEqual(result, expected[k - 1])
                    # состав не изменился
                    self.assertEqual(sorted(values), expected)

    def test_invalid_k_values(self):
        cases = [
            ([], 1),          # пустой список
            ([1, 2, 3], 0),
            ([1, 2, 3], -1),
            ([1, 2, 3], 4),
            ([1, 2, 3], 1.5),
            ([1, 2, 3], True),
        ]
        for values, k in cases:
            with self.subTest(values=values, k=k):
                with self.assertRaises(ValueError):
                    statistic(values, k, seed=1)


if __name__ == "__main__":
    unittest.main()