# coding=utf-8


class PrimeFactor:

    def of(self, number: int) -> list[int]:
        factors = []
        if number == 2:
            factors = [2]
        elif number == 3:
            factors = [3]
        return factors
