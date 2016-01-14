class FileReader:
    def __init__(self, filepath):
        """
        Constructeur de la classe, lit le fichier entre en parametre,
        le rammene a une longueur multiple de 4 et place son contenu dans l'attibut data
        :param filepath: chemin du fichier source
        :return: contenu du fichier formatte dans data
        """
        with open(filepath, 'r') as myfile:
            self.data = myfile.read().replace('\n', '').replace('\r', '')

        while len(self.data) % 4 != 0:
            self.data = self.data[:-1]