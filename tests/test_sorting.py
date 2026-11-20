import unittest
from solve.sorting import METHODS


class SortingTests(unittest.TestCase):

    def _check(self, method, original, descending):
        values = original[:]
        result = METHODS[method](values, descending)
        self.assertIsNone(result)
        self.assertEqual(values, sorted(original, reverse=descending))

    def test_all_methods(self):
        cases = {
            "repeats":   [3, 1, 3, -2, 0, 1],
            "single":    [5],
            "sorted_asc":[1, 2, 3, 4, 5],
            "reverse":   [5, 4, 3, 2, 1],
        }
        for method in METHODS:
            for name, original in cases.items():
                for descending in (False, True):
                    with self.subTest(method=method, case=name, desc=descending):
                        self._check(method, original, descending)


if __name__ == "__main__":
    unittest.main()