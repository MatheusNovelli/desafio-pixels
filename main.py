from PIL import Image

img = Image.open("Syngenta.bmp")
img = img.convert('RGB')
imgX, imgY = img.size
imagepixel = []


def checkforpixels():
    totalpixel = imgX * imgY

    for i in range(0, imgX):
        for j in range(0, imgY):
                imagepixel.append(img.getpixel((i, j))) #Pega as coordenadas do pixel e os insere em uma lista em formato RGB.
    #Conta as tuplas(RGB) que contém (255,255,255) e (0,0,0), que já são conhecidas por serem as cores branco e preto.
    whitepixel = imagepixel.count((255, 255, 255))
    blackpixel = imagepixel.count((0, 0, 0))
    greenpixel = totalpixel - whitepixel - blackpixel

    print('O número de pixels pretos do bitmap é:', blackpixel)
    print('O número de pixels brancos do bitmap é:', whitepixel)
    print('O número de pixels verdes do bitmap é:', greenpixel, '!!')


def converttobinary(message):
        return format(message, "08b")


def imagedecoder1():
    binary = ""
    for pixel in imagepixel:
        for value in pixel:
            rgb = converttobinary(value)
            binary += rgb[-1]

    allbytes = [binary[i: i + 8] for i in range(0, len(binary), 8)]
    hiddenmessage = ""
    for byte in allbytes:
        hiddenmessage += chr(int(byte, 2))

    print('Mensagem:', hiddenmessage)


def imagedecoder2():
    binary = ""
    for pixel in imagepixel:
        for value in pixel:
            rgb = converttobinary(value)
            binary += rgb[-1]
    intbinary = int(binary, 2)
    bytenumber = intbinary.bit_length() + 7//8
    binaryarray = intbinary.to_bytes(bytenumber, "big")

    hiddenmessage = binaryarray.decode()
    print(hiddenmessage)


def main():
    checkforpixels()
    imagedecoder1()
    #imagedecoder2()


if __name__ == '__main__':
    main()
