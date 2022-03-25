import binascii
import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

def getRandomHex():
    hexList = [b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7' ,b'8', b'9', b'a', b'b',b'c',b'd',b'e',b'f']
    choice = random.choices(hexList, k=2)
    while choice == b'ff':
        choice = random.choices(hexList, k=2)
    return b''.join(choice)


def corruptJpeg(inputFileName, randomChance, iterations):
    f = open(inputFileName, 'rb')
    fileContents = f.read()
    f.close()
    fileContentsHex = binascii.hexlify(fileContents, '-')
    fileContentsSplit = fileContentsHex.split(b'-')


    for i in range(iterations):
        outputFileName = f"output_{i + 1}.jpeg"
        fOut = open(outputFileName, 'wb')
        for i in range(len(fileContentsSplit)):
            if fileContentsSplit[i] == b'ff' or (i > 0 and fileContentsSplit[i - 1] == b'ff'):
                fOut.write(binascii.unhexlify(fileContentsSplit[i]))
                continue

            if random.randint(1, randomChance) == 1:
                fOut.write(binascii.unhexlify(getRandomHex()))
            else:
                fOut.write(binascii.unhexlify(fileContentsSplit[i]))
        fOut.close()


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
    # inputFileName = "demo_images/test3.jpeg"
    # randomChance = 15000
    # iterations = 10

    # corruptJpeg(inputFileName, randomChance, iterations)




