class FileReader:
    def __init__(self, filepath):
        with open(filepath, 'r') as myfile:
            self.data = myfile.read().replace('\n', '').replace('\r', '')

        while len(self.data) % 4 != 0:
            self.data = self.data[:-1]