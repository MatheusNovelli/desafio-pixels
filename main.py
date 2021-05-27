from PIL import Image


def checkforpixels():
    image = Image.open('Syngenta.bmp')

    pix = image.load()


    #image.convert("RGB")
    imagerow, imagecol = image.size
    greenpixel = 0


    color1 = image.getpixel((0, 0))
    print(color1)

    color1 = image.getpixel((0, 0))
    print(color1)

    for i in range(0, imagerow):
        for j in range(0, imagecol):
            print(pix[i,j])
            #imagecolorR, imagecolorG, imagecolorB = image.getpixel((i, j))
            #if(imagecolorR != 0 and imagecolorG != 0 and imagecolorB != 0):
            #    print(imagecolorR, imagecolorG, imagecolorB)
            #if imagepixel != ('color1') and imagepixel != ('color2'):
            #    greenpixel += 1

    print(greenpixel)

def teste():
    # The conversion should work equally with a bitmap
    img = Image.open("Syngenta.bmp")
    rgb_im = img.convert('RGB')
    x = 0
    imagepixel = []

    for i in range(rgb_im.size[x]):
        imagepixel.append(rgb_im.getpixel((i, x)))
        if x < 299:
            x += 1
    print(imagepixel)
    print(imagepixel.count((0, 0, 0)))


    ##first_row = [rgb_im.getpixel((i, 0)) for i in range(rgb_im.size[0])]
    # Count how many pixels are black. Note that jpg is not the cleanest of all file formats.
    # Hence converting to and from jpg usually comes with some losses, i.e. changes in pixel values.
    #print(first_row.count((255, 255, 255)))  # --> 628
    #len(first_row)  # --> 680

    #set(first_row)

def main():
    teste()

if __name__ == '__main__':
    main()