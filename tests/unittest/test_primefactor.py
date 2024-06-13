import unittest

from src.primefactor.primefactor import PrimeFactor


class PrimeFactorTestCase(unittest.TestCase):

    def setUp(self):
        self.prime_factor = PrimeFactor()

    def test_primefactor_of_1(self):
        self.assertEqual([], self.prime_factor.of(1))

    def test_primefactor_of_2(self):
        self.assertEqual([2], self.prime_factor.of(2))


if __name__ == "__main__":
    unittest.main()
