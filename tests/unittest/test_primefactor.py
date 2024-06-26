import unittest

from src.primefactor.primefactor import PrimeFactor


class PrimeFactorTestCase(unittest.TestCase):

    def setUp(self):
        self.prime_factor = PrimeFactor()

    def test_primefactor_of_1(self):
        self.assertEqual([], self.prime_factor.of(1))

    def test_primefactor_of_2(self):
        self.assertEqual([2], self.prime_factor.of(2))

    def test_primefactor_of_3(self):
        self.assertEqual([3], self.prime_factor.of(3))

    def test_primefactor_of_4(self):
        self.assertEqual([2, 2], self.prime_factor.of(4))

    def test_primefactor_of_6(self):
        self.assertEqual([2, 3], self.prime_factor.of(6))

    def test_primefactor_of_9(self):
        self.assertEqual([3, 3], self.prime_factor.of(9))

    def test_primefactor_of_12(self):
        self.assertEqual([2, 2, 3], self.prime_factor.of(12))


if __name__ == "__main__":
    unittest.main()
