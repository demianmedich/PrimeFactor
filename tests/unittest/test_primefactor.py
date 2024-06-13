import unittest

from src.primefactor.primefactor import PrimeFactor


class PrimeFactorTestCase(unittest.TestCase):
    def test_primefactor_of_1(self):
        pf = PrimeFactor()
        self.assertEqual([], pf.of(1))

    def test_primefactor_of_n(self):
        pf = PrimeFactor()

        expected_pairs = (
            (2, [2]),
            (3, [3]),
            (4, [2, 2]),
            (5, [5]),
            (6, [2, 3]),
            (7, [7]),
            (8, [2, 2, 2]),
        )

        for n, primes in expected_pairs:
            self.assertEqual(primes, pf.of(n))


if __name__ == "__main__":
    unittest.main()
