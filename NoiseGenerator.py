import random


class NoiseGenerator:
    @staticmethod
    def bool_random(proba):
        """
        Genere un booleen aleatoire suivant la probabilite entree en parametre,
        plus elle sera grande, plus le resultat aura de chances d'etre True
        :param proba: Probablilite d'obtenir True (en %)
        :return: True ou False
        """
        coefs = {True: proba, False: 100 - proba}
        number = random.random() * sum(coefs.values())
        for k, v in coefs.items():
            if number < v:
                break
            number -= v
        return k

    @staticmethod
    def convert(string):
        """
        Ajoute du bruit dans une chaine de 0 ou 1
        :param string: chaine a convertir
        :return: chaine convertie
        """
        s = list(string)
        i = 0
        while i < len(s):
            if NoiseGenerator.bool_random(1):  # Définir ici le taux de probabilité de True (1%)
                s[i] = '1' if (s[i] == '0') else '0'

            i += 1

        return "".join(s)
