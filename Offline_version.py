import os
import binascii
import random


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

    if not os.path.exists("demo_outputs/inputFileName/"):
        os.makedirs("demo_outputs/inputFileName/")

    for i in range(iterations):
        outputFileName = f"demo_outputs/inputFileName/output_{i + 1}.jpeg"
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

def swapCorruptJpeg(inputFileName, randomChance, iterations):
    f = open(inputFileName, 'rb')
    fileContents = f.read()
    f.close()
    fileContentsHex = binascii.hexlify(fileContents, '-')
    fileContentsSplit = fileContentsHex.split(b'-')

    if not os.path.exists("demo_outputs/inputFileName/"):
        os.makedirs("demo_outputs/inputFileName/")

    for i in range(iterations):
        outputFileName = f"demo_outputs/inputFileName/output_{i + 1}.jpeg"
        fOut = open(outputFileName, 'wb')
        for i in range(len(fileContentsSplit)):
            if fileContentsSplit[i] == b'ff' or (i > 0 and fileContentsSplit[i - 1] == b'ff'):
                fOut.write(binascii.unhexlify(fileContentsSplit[i]))
                continue

            if random.randint(1, randomChance) == 1:
                randomIndex = random.randint(0, len(fileContentsSplit))
                while fileContentsSplit[randomIndex] == b'ff':
                    randomIndex = random.randint(0, len(fileContentsSplit))
                fOut.write(binascii.unhexlify(fileContentsSplit[randomIndex]))
            else:
                fOut.write(binascii.unhexlify(fileContentsSplit[i]))
        fOut.close()


#Modify variables here
inputFileName = "demo_images/test5.jpeg"
randomChance =35000
iterations = 10

#Use either functions here
corruptJpeg(inputFileName, randomChance, iterations)
#swapCorruptJpeg(inputFileName, randomChance, iterations)




