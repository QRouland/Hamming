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
correct = ""

while len(recu) >= 7:
    mot = recu[0:7]
    correct += ham.correction(mot)
    recu = recu[7:]

FileUtil.write("correct.txt", correct)
message = ""

while len(correct) >= 7:
    mot = recu[0:7]
    message += ham.decode(mot)
    correct = correct[7:]

FileUtil.write("message.txt", message)