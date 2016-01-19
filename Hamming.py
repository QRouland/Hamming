import sys


class Hamming:
    def hamming(self, mot):
        """
        Retourne le mot de code (mot 4bits + les bits de parite)
        :param mot: Mot de 4 bits a encoder
        :return: le mot de code (mot 4bits + les bits de parite)
        """
        return "".join(
                [mot,
                 self.parite(mot, [1, 2, 3]),
                 self.parite(mot, [0, 2, 3]),
                 self.parite(mot, [0, 1, 3]),
                 ])

    def parite(self, mot, indices):
        """
        Calcul la parite pour les bits correspondants aux indices dans le mot
        :param mot: Mot de code
        :param indices: Indice des bits ou effectuer la parite
        :return: parite pour les bits correspondants aux indices du mot
        """
        return str(sum([int(mot[i]) for i in indices if mot[i] == "1"]) % 2)


    def correction(self, mot):
        """
        Corrige le mot avec hamming
        :param mot: mot a corriger
        :return: mot corrige
        """
        # Calculate syndrome
        s = [
            (int(mot[1]) + int(mot[2]) + int(mot[3]) + int(mot[4])) % 2,
            (int(mot[0]) + int(mot[2]) + int(mot[3]) + int(mot[5])) % 2,
            (int(mot[0]) + int(mot[1]) + int(mot[3]) + int(mot[6])) % 2,
        ]

        b = 4 * s[2] + 2 * s[1] + s[0]

        if b not in [0]:
            SYNDROME_CHECK = [-1, 4, 5, 2, 6, 1, 0, 3]
            y = list(mot)
            y[SYNDROME_CHECK[b]] = str((int(y[SYNDROME_CHECK[b]]) + 1) % 2)
            mot = "".join(y)
        return mot

    def decode(self, mot):
        """
        Decode le mot
        :param mot: mot a decoder
        :return: mot decode
        """
        return mot[0:4]



