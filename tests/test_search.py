import unittest
from solve.arrays import binary_search


class SearchTests(unittest.TestCase):

    def test_found(self):
        values = [1, 3, 5, 7, 9]
        idx = binary_search(values, 5)
        self.assertIsNotNone(idx)
        self.assertEqual(values[idx if idx is not None else 0], 5)

    def test_found_first_index_zero(self):
        values = [10, 20, 30]
        idx = binary_search(values, 10)
        self.assertIsNotNone(idx)   # индекс 0 — корректный результат
        self.assertEqual(values[idx if idx is not None else 0], 10)

    def test_not_found(self):
        self.assertIsNone(binary_search([1, 3, 5], 4))

    def test_duplicates_any_index(self):
        values = [2, 2, 2, 2]
        idx = binary_search(values, 2)
        self.assertIsNotNone(idx)
        self.assertEqual(values[idx if idx is not None else 0], 2)

    def test_empty(self):
        self.assertIsNone(binary_search([], 1))


if __name__ == "__main__":
    unittest.main()