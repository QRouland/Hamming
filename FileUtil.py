import textwrap


class FileUtil:
    @staticmethod
    def read(filepath):
        """
        Lit le fichier entré en paramètre,
        le rammène à une longueur multiple de 4 et renvoie son contenu
        :param filepath: chemin du fichier source
        :return: contenu du fichier formatté
        """
        with open(filepath, 'r') as myfile:
            data = myfile.read().replace('\n', '').replace('\r', '')

        while len(data) % 4 != 0:
            data = data[:-1]

        return data

    @staticmethod
    def write(filepath, string):
        """
        Ecrit dans le fichier entré en paramètre, en le formattant
        :param filepath: chemin du fichier source
        :param string: Chaine a écrire dans le fichier
        """
        string = '\n'.join(textwrap.wrap(string, 90))

        with open(filepath, 'r') as myfile:
            myfile.write(string)


r = FileUtil.read("source.txt")