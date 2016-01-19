class FileRUtil:
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
