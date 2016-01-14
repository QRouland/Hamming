import random


class NoiseGenerator:
    @staticmethod
    def bool_random(proba):
        coefs = {True : proba, False: 100-proba}
        number = random.random() * sum(coefs.values())
        for k,v in coefs.items():
            if number < v:
                break
            number -= v
        return k

    @staticmethod
    def convert(string):
        s = list(string)
        i = 0
        while i < len(s):
            if NoiseGenerator.bool_random(1):
                s[i] = '1' if (s[i] == '0') else '0'

            i += 1

        return "".join(s)
