import numpy as np
from PIL import Image

#https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372


# def checkforpixels():
#     image = Image.open('Syngenta.bmp')

#     pix = image.load()


#     #image.convert("RGB")
#     imagerow, imagecol = image.size
#     greenpixel = 0


#     color1 = image.getpixel((0, 0))
#     print(color1)

#     color1 = image.getpixel((0, 0))
#     print(color1)

#     for i in range(0, imagerow):
#         for j in range(0, imagecol):
#             print(pix[i,j])
#             #imagecolorR, imagecolorG, imagecolorB = image.getpixel((i, j))
#             #if(imagecolorR != 0 and imagecolorG != 0 and imagecolorB != 0):
#             #    print(imagecolorR, imagecolorG, imagecolorB)
#             #if imagepixel != ('color1') and imagepixel != ('color2'):
#             #    greenpixel += 1

#     print(greenpixel)
img = Image.open("Syngenta.bmp")
I = np.asarray(img)
imgX, imgY = img.size


def teste():
    print("Abrindo a imagem...")
    img = Image.open("Syngenta.bmp")
    print("Ok!")
    print("Convertendo imagem para RGB...")
    rgb_im = img.convert('RGB')
    print("Ok!")
    imgX, imgY = rgb_im.size
    totalpixel = imgX * imgY
    imagepixel = []
    blackpixel = 0
    whitepixel = 0
    greenpixel = 0

    print("Contando número de pixels verdes...")
    for i in range(0, imgX):
        for j in range(0, imgY):
            imagepixel.append(rgb_im.getpixel((i, j)))
    whitepixel = imagepixel.count((255, 255, 255))
    blackpixel = imagepixel.count((0, 0, 0))
    greenpixel = totalpixel - whitepixel - blackpixel

    print('O número de pixels verdes do bitmap é:', greenpixel)


def converttobinary(message):
    return [format(i, "08b") for i in message]


def imagedecoder(image):
    binary = ""
    for value in image.size:
        for pixel in value:
            r, g, b = converttobinary(pixel)
            binary += r[-1]
            binary += g[-1]
            binary += b[-1]

    bytes = [binary[i: i + 8] for i in range(0, len(binary), 8)]

    hiddenmessage = ""
    for byte in bytes:
        hiddenmessage += chr(int(byte, 2))
        if hiddenmessage[-5:] == "####":
            break

    return hiddenmessage[-5:]


def main():
    teste()
    print(imagedecoder(img))


if __name__ == '__main__':
    main()
