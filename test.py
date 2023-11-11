import time
# import board
# import neopixel
import random
#from random import randint


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
#pixel_pin = board.D18


numPixels = 50



# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
#ORDER = neopixel.RGB

#pixels = neopixel.NeoPixel(
#    pixel_pin, numPixels, brightness=0.2, auto_write=False, pixel_order=ORDER
#)

r = 255
g = 0
b = 0
goingUp = True
modValue = 1


while True:



    for x in range(numPixels):
        

        # if goingUp:
        #     g = g + modValue
        # else:
        #     g = g - modValue

        # print(x)
        # if g > 255:
        #     goingUp = False
        #     g = g - modValue
        # elif  g < 0:
        #     goingUp = True
        #     g = g + modValue

        #print (random.randint(1, 100))

        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)

        #print(random.randint(3, 9))

 #       color = (r, g, b)
        
        print("(" + str(r) + "," + str(g) + "," + str(b) + ")")

  #      print(color)

   #     pixels[x] = color
    #    pixels.show()

        time.sleep(0.01)
    
    

    






