import unittest
from solve.arrays import shuffle


class ShuffleTests(unittest.TestCase):

    def test_composition(self):
        original = [2, 2, -1, 5]
        values = original[:]
        result = shuffle(values, seed=1)
        self.assertIsNone(result)
        self.assertEqual(sorted(values), sorted(original))
        self.assertEqual(len(values), len(original))

    def test_empty(self):
        values = []
        self.assertIsNone(shuffle(values, seed=1))
        self.assertEqual(values, [])

    def test_single(self):
        values = [7]
        shuffle(values, seed=1)
        self.assertEqual(values, [7])

    def test_all_same(self):
        values = [3, 3, 3, 3]
        shuffle(values, seed=1)
        self.assertEqual(values, [3, 3, 3, 3])

    def test_reproducible(self):
        original = [1, 2, 3, 4, 5, 6, 7, 8]
        a = original[:]
        b = original[:]
        shuffle(a, seed=42)
        shuffle(b, seed=42)
        self.assertEqual(a, b)

    def test_does_not_require_change(self):
        # алгоритм имеет право оставить порядок прежним
        original = [1]
        values = original[:]
        shuffle(values, seed=1)
        self.assertEqual(sorted(values), sorted(original))


if __name__ == "__main__":
    unittest.main()