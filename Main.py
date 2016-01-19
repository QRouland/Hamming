from FileUtil import FileUtil
from Hamming import Hamming
from NoiseGenerator import NoiseGenerator

source = FileUtil.read("source.txt")

ham = Hamming()
emis = ""

while len(source) >= 4:
    mot = source[0:4]
    emis += ham.hamming(mot)
    source = source[4:]

FileUtil.write("emis.txt", emis)

recu = NoiseGenerator.convert(emis)

FileUtil.write("recu.txt", recu)