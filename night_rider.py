# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

#var inits
pixel_index = 0
going_up = True

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def cycle(wait):

    global pixel_index
    global going_up

    #clear all (black)
    for i in range(num_pixels):
            #pixel_index = (i * 256 // num_pixels) + j
        pixels[i] = (0,0,0)#wheel(pixel_index & 255)
    pixels.show()

    #set pixel index to red
    pixels[pixel_index] = (225,0,0)
    pixels.show()

    #increment/decrement
    if going_up:
        pixel_index = pixel_index + 1
    else:
        pixel_index = pixel_index - 1

    #start back down
    if pixel_index > (num_pixels -2) and going_up:
        going_up = False
    
    #start back up
    if pixel_index ==  0 and going_up == False:
        going_up = True

    #print (pixel_index)

    time.sleep(wait)


while True:
    cycle(0.01)  # cycle with 1ms delay per step