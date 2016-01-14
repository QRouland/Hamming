import sys


def parity(bits, param):
    pass


class Hamming:
    def encode(self, message):
        """
        Encode le message dans un fichier emis.txt
        :param message: Le message a encoder
        :return:
        """
        with open("emis.txt", "w") as f:
            while len(message) >= 4:
                mot = message[0:4]
                f.write(self.hamming(mot) + "\n")
                message = message[4:]

    def hamming(self, mot):
        """
        Retourne le mot de code (mot 4bits + les bits de parite)
        :param mot: Mot de 4 bits a encoder
        :return: le mot de code (mot 4bits + les bits de parite)
        """
        return "".join(
                [mot,
                 self.parite(mot, [0, 1, 2]),
                 self.parite(mot, [1, 2, 3]),
                 self.parite(mot, [0, 2, 3])])

    def parite(self, mot, indices):
        """
        Calcul la parite pour les bits correspondants aux indices dans le mot
        :param mot: Mot de code
        :param indices: Indice des bits ou effectuer la parite
        :return: parite pour les bits correspondants aux indices du mot
        """
        """Compute the parity bit for the given string s and indicies"""
        return str(sum([int(mot[i]) for i in indices if mot[i] == "1"]) % 2)


# Main

if __name__ == "__main__":
    input_string = input("LOL :")
    hamming = Hamming()
    hamming.encode(input_string)
