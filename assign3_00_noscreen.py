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

import pygame, os, random, copy
from pygame.locals import *
from math import sin

main_dir = os.path.split(os.path.abspath(__file__))[0]
black = (255,255,255) #almost white
white = (0,0,0)

letters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
imagenamelist=[]
bitmaplist=[]


def getrandomfilename():
    return letters[random.randint(0,len(letters)-1)]+str(random.randint(1,10))+".jpg"

def main():
    #initialize and setup screen
    pygame.init()
    mainClock = pygame.time.Clock()
    #screen = pygame.display.set_mode((640, 480), HWSURFACE|DOUBLEBUF)

    #load image and quadruple
    for x in range(5):
      imagename= os.path.join(main_dir, 'RESIZED_30x30',getrandomfilename())
      bitmap = pygame.image.load(imagename)
      
      #bitmap = pygame.transform.scale2x(bitmap)
      #bitmap = pygame.transform.scale2x(bitmap)

      imagenamelist.append(imagename)
      bitmaplist.append(bitmap)

    print imagenamelist
  

    #get the image and screen in the same format
    #if 0:#screen.get_bitsize() == 8:
        #screen.set_palette(bitmap.get_palette())
    if 1:
        print "converting"
        oldbitmap =bitmap
        #bitmap = bitmap.convert()

    #prep some variables
    anim = 0.0

    #mainloop
    
    stopevents = QUIT, KEYDOWN, MOUSEBUTTONDOWN
    frame=0

    while 1:
        #xblocks = range(00, 640, 30)
        #yblocks = range(00, 480, 30) 
        frame+=1
        #adjust=100-frame
        #if adjust<0:adjust=0

        #screen.fill(black)
        for e in pygame.event.get():
            if e.type in stopevents:
                return
        
       




     


        
        
        bitmap=bitmaplist[frame/10%5]
     
     
        
        
        if frame%10==0:
          
          
          nr=0
          bw9x9list=[]
          da9x9list=[]
          da30x30list=[]
          da30list=[]

          for x in range(30):
            da30list.append(0)

          for x in range(30):
            da30x30list.append(copy.deepcopy(da30list))

        if frame%10==0:
          bwcolorlist=[]
          nr=0
          for y in range(30):
              for x in range (30):
                  pickcolor=oldbitmap.get_at((x,y))
                  bwcolorlist.append(pickcolor[0])
                  da30x30list[nr/30][nr%30]=pickcolor[0]
                  #screen.set_at([300+x*2,200+y*2],(bwcolorlist[nr],bwcolorlist[nr],bwcolorlist[nr]))

                  nr+=1
          print bwcolorlist[0:40]
          #print da30list
          print da30x30list[0:2]



          #for x in range(9):
           # da9x9list.append([0,0,0,0,0,0,0,0,0])


          for y in range(9):
            for x in range(9):
                nr+=1
                sum=0
                for yy in range(10):
                    for xx in range(10):
                        num=x*10+y*900+xx+yy*90
                        sum+=bwcolorlist[num/10]
                bw9x9list.append(sum)
          print len(bw9x9list),bw9x9list
          print da9x9list


          if frame==100:return





        #pygame.display.flip()
        mainClock.tick(30)



if __name__ == '__main__': main()
