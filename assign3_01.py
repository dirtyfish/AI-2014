#!/usr/bin/env python

"""This examples demonstrates a simplish water effect of an
image. It attempts to create a hardware display surface that
can use pageflipping for faster updates. Note that the colormap
from the loaded GIF image is copied to the colormap for the
display surface.

This is based on the demo named F2KWarp by Brad Graham of Freedom2000
done in BlitzBasic. I was just translating the BlitzBasic code to
pygame to compare the results. I didn't bother porting the text and
sound stuff, that's an easy enough challenge for the reader :]"""

import pygame, os, random
from pygame.locals import *
from math import sin

main_dir = os.path.split(os.path.abspath(__file__))[0]
black = (255,255,255) #almost white

letters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
imagenamelist=[]
bitmaplist=[]


def getrandomfilename():
    return letters[random.randint(0,len(letters)-1)]+str(random.randint(1,10))+".jpg"

def main():
    #initialize and setup screen
    pygame.init()
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480), HWSURFACE|DOUBLEBUF)

    #load image and quadruple
    for x in range(5):
      imagename= os.path.join(main_dir, 'RESIZED_30x30',getrandomfilename())
      bitmap = pygame.image.load(imagename)
      bitmap = pygame.transform.scale2x(bitmap)
      bitmap = pygame.transform.scale2x(bitmap)

      imagenamelist.append(imagename)
      bitmaplist.append(bitmap)

    print imagenamelist
  

    #get the image and screen in the same format
    if screen.get_bitsize() == 8:
        screen.set_palette(bitmap.get_palette())
    else:
        bitmap = bitmap.convert()

    #prep some variables
    anim = 0.0

    #mainloop
    
    stopevents = QUIT, KEYDOWN, MOUSEBUTTONDOWN
    frame=0

    while 1:
        xblocks = range(00, 640, 24)
        yblocks = range(00, 480, 24) 
        frame+=1
        adjust=100-frame
        if adjust<0:adjust=0
        screen.fill(black)
        for e in pygame.event.get():
            if e.type in stopevents:
                return
        
        bitmapnr=-1
        if frame<150:
            for bitmap in bitmaplist:
                bitmapnr+=1
                anim = anim + 0.04
                for x in xblocks:
                    xpos = (x + (sin(anim+bitmapnr+adjust + x * .03) * 15)) + 0
                    for y in yblocks:
                        ypos = (y + (sin(anim+bitmapnr + y * .03) * 15)) + 0
                        screen.blit(bitmap, (x+130*bitmapnr, y+adjust), (xpos, ypos, 23,23))

        if frame>150:
            for bitmap in bitmaplist:
                bitmapnr+=1
                anim = anim + 0.04
                for x in xblocks:
                    xpos = x#(x + (sin(anim+bitmapnr+adjust + x * .03) * 15)) + 0
                    for y in yblocks:
                        ypos = y#(y + (sin(anim+bitmapnr + y * .03) * 15)) + 0
                        screen.blit(bitmap, (x+130*bitmapnr, y+adjust), (xpos, ypos, 25,25))


        if frame==300:
            screen = pygame.display.set_mode((640, 480), HWSURFACE|DOUBLEBUF|FULLSCREEN)


        
        #bitmap=bitmaplist[frame/100%5]
        #bitmap = pygame.transform.scale2x(bitmap)
        #screen.blit(bitmap, (200, 200), (0, 0, 240,240))

        xblocks = range(00, 640, 48)
        yblocks = range(00, 480, 48)
        bitmap=bitmaplist[frame/100%5]
        bitmap = pygame.transform.scale2x(bitmap)
        if 1:
           anim = anim + 0.04
           for x in xblocks:
                    xpos = x#(x + (sin(anim+bitmapnr+adjust + x * .03) * 15)) + 0
                    for y in yblocks:
                        ypos = y#(y + (sin(anim+bitmapnr + y * .03) * 15)) + 0
                        screen.blit(bitmap, (x+200, y+200), (xpos, ypos, 47,47))


        pygame.display.flip()
        mainClock.tick(30)



if __name__ == '__main__': main()
