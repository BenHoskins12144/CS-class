import board
import neopixel
import time


pixels = neopixel.NeoPixel(board.GP0, 20)


#colors=[(50,0,53),(35,5,57),(0,0,50),(0,50,0),(50,27,0),(50,5,0),(50,0,0)]
colors=[(50,0,0),(50,5,0),(50,27,0),(0,50,0),(0,0,50),(35,5,57),(50,0,53)]

for i in range(7):
    for j in range(i):
        pixels[j]=colors[6-i]
        time.sleep(.50)
  
#pixels[13] = (50,0,53)
#pixels[14] = (35,5,57)
#pixels[15] = (0,0,50)
#pixels[16] = (0,50,0)
#pixels[17] = (50,27,0)
#pixels[18] = (50,5,0)
#pixels[19] = (50,0,0)


  
#for i in range(1 ,20,2):
#  pixels[i] = (0,0,50)
#  time.sleep(.25)
