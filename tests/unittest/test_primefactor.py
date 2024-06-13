import unittest

from src.primefactor.primefactor import PrimeFactor


class PrimeFactorTestCase(unittest.TestCase):
    def test_primefactor_of_1(self):
        pf = PrimeFactor()
        self.assertEqual([], pf.of(1))

    def test_primefactor_of_2(self):
        pf = PrimeFactor()
        self.assertEqual([2], pf.of(2))


if __name__ == "__main__":
    unittest.main()
