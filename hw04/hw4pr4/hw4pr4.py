''' Brian Richardson 
9/27/18
CSCI 203: 3 pm Tuesday  
Lab 4 extra credit
'''
from cs5png import *

def testBinaryImage():
    """ run this function to create an 8x8 alien image
        named binary.png
    """
    alien = "0"*8 + "11011011"*2 + "0"*8 + "00001000" + \
            "01000010" + "01111110" + "0"*8
    # this function is imported from cs5png.py
    numRows = 8
    numCols = 8
    binaryIm(alien, numCols, numRows)
    # that should create a file, binary.png, in this
    # directory with the 8x8 image...


def invert(pixel):
    """ invert takes in a pixel (an [R, G, B] list)
        and returns a new pixel to take its place!
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return [255 - red, 255 - green, 255 - blue]

def testImageProcessing():
    """ Run this function to read in the in.png image,
        change it, and write out the result to out.png.
    """
    imagePixels = getRGB('in.png')  # read in the in.png image
    print("The first two pixels of the first row are", end=' ')
    print(imagePixels[0][0:2])
    # remember that imagePixels is a list (the image)
    # of lists (each row) of lists (each pixel is [R, G, B])
    newPixels = [[invert(pixel) for pixel in row] for row in imagePixels]
    # now, save to the file 'out.png'
    saveRGB(newPixels, 'out.png')

def grayscale(pngName='demo.png'):
    def gray(pixel):
        val = int(0.3 * pixel[0]) + int(0.59 * pixel[1]) + int(0.11 * pixel[2])
        pixel[0], pixel[1], pixel[2] = val,val,val
        return pixel
    pixels = getRGB(pngName)
    newPixels = [[gray(pixel) for pixel in row] for row in pixels]
    saveRGB(newPixels, 'gray.png')

def flipVert(pngName='demo.png'):
    pixels = getRGB(pngName)
    newPixels = [[pixel for pixel in row] for row in pixels[::-1]]
    saveRGB(newPixels,'flipvert.png')

def flipHoriz(pngName='demo.png'):
    pixels = getRGB(pngName)
    newPixels = [[pixel for pixel in row[::-1]] for row in pixels]
    saveRGB(newPixels,'flipHoriz.png')

def mirrorVert(pngName='demo.png'):
    '''mirror over horizontal axis, giving an Up-Down mirror'''
    pixels = getRGB(pngName)
    newPixels = [[pixel for pixel in row] for row in \
                 pixels[0:len(pixels)//2] + pixels[-len(pixels)//2 - 1::-1]]
    saveRGB(newPixels,'mirrorVert.png')

def mirrorHoriz(pngName='demo.png'):
    '''mirror over vertical axis, giving a left-Right mirror'''
    pixels = getRGB(pngName)
    newPixels = [[pixel for pixel in \
                  row[0:len(row)//2] + row[-len(row)//2 - 1::-1]] \
                 for row in pixels]
    saveRGB(newPixels,'mirrorHoriz.png')

def blur(rate=5,pngName='demo.png'):
    '''Blurs picture by an inputted blur rate'''
    pixels = getRGB(pngName)
    selR = 0
    selC = 0
    newPixels = pixels
    for r in range(len(pixels)):
        if r%rate == 0:
            selR = r
        for c in range(len(pixels[r])):
            if c%rate == 0:
                selC = c
            newPixels[r][c] = pixels[selR][selC]
    saveRGB(newPixels,'blur.png')
