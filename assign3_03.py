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
red = (255,0,0) #red
green = (0,255,0) 
blue = (0,0,255) 

letters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nletters=26
nset=20
vocals= ['A','E','I','O','U','Y']
imagenamelist=[]
bitmaplist=[]
avgcolorlist=[]
cacl=[]

def wasvocal(letter):  #not in use
    for vocal in vocals:
        if letter==vocal:return true
    else:return false

def randomcolor():
    #random.randint(0,255)
    #random.randint(0,255)
    #random.randint(0,255)
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))


def getrandomfilename():
    return letters[random.randint(0,26)]+str(random.randint(1,10 ))+".jpg"

def getfilename(ch,numb):
    return letters[ch]+str(numb)+".jpg"

def main():
    #initialize and setup screen
    pygame.init()
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480), HWSURFACE|DOUBLEBUF)

    #load image and quadruple
    for c in range(0,nletters):
        for x in range(1,nset+1):
          imagename= os.path.join(main_dir, 'RESIZED_30x30',getfilename(c,x))
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
        xblocks = range(00, 120, 24)
        yblocks = range(00, 120, 24) 
        frame+=+20
        adjust=100-frame
        if adjust<0:adjust=0
        screen.fill(black)
        for e in pygame.event.get():
            if e.type in stopevents:
                return
        
        bitmapnr=-1
        if frame<200:
            for bitmap in bitmaplist:
                bitmapnr+=1
                anim = anim + 0.04
                for x in xblocks:
                    xpos = (x + (sin(anim+bitmapnr+adjust + x * .03) * 15)) + 0
                    for y in yblocks:
                        ypos = (y + (sin(anim+bitmapnr + y * .03) * 15)) + 0
                        screen.blit(bitmap, (x+130*bitmapnr, y+adjust), (xpos, ypos, 23,23))

        if frame>200:
            for bitmap in bitmaplist:
                bitmapnr+=1
                anim = anim + 0.04
                for x in xblocks:
                    xpos = x#(x + (sin(anim+bitmapnr+adjust + x * .03) * 15)) + 0
                    for y in yblocks:
                        ypos = y#(y + (sin(anim+bitmapnr + y * .03) * 15)) + 0
                        screen.blit(bitmap, (x+130*bitmapnr, y+adjust), (xpos, ypos, 25,25))


        
        #bitmap=bitmaplist[frame/100%5]
        #bitmap = pygame.transform.scale2x(bitmap)
        #screen.blit(bitmap, (200, 200), (0, 0, 240,240))

        xblocks = range(00, 240, 48)
        yblocks = range(00, 240, 48)
        bitmap=bitmaplist[frame/100%520-1]
        imagename=imagenamelist[frame/100%520-1]
        bitmap = pygame.transform.scale2x(bitmap)
        if 1:
           #anim = anim + 0.04
           for x in xblocks:
                    xpos = x#(x + (sin(anim+bitmapnr+adjust + x * .03) * 15)) + 0
                    for y in yblocks:
                        ypos = y#(y + (sin(anim+bitmapnr + y * .03) * 15)) + 0
                        screen.blit(bitmap, (x+200, y+200), (xpos, ypos, 47,47))






         

        xblocks = range(00, 240, 48)
        yblocks = range(00, 240, 48)    
        count=0
        avgcolor=[0,0,0]
        sumcolor=[0,0,0]
        sumcolorlist=[]
        #for x in range(500):
         # sumcolorlist.append(0)
        if frame%100==0:avgcolorlist=[]
        for x in xblocks:
                xpos = x#(x + (sin(anim+bitmapnr+adjust + x * .03) * 15)) + 0
                for y in yblocks:
                        ypos = y#(y + (sin(anim+bitmapnr + y * .03) * 15)) + 0   

                        
                        for offset in range(4,44,4): #define scan area
                          
                          if frame%100==0:
                                         
                            count+=1
                            pickcolor=screen.get_at((200+x+offset, 200+y+offset)) #one diagonal
                            
                            sumcolor[0]+=pickcolor[0]
                            #sumcolor[1]+=pickcolor[1]
                            #sumcolor[2]+=pickcolor[2]
                            pickcolor=screen.get_at((200+x+48-offset, 200+y+offset)) #other diagonal
                            sumcolor[0]+=pickcolor[0]
                            #sumcolor[1]+=pickcolor[1]               #we dont need more than grayscale info
                            #sumcolor[2]+=pickcolor[2]               #since r=g=b, only one is needed
                          justacolor=randomcolor()
                          screen.set_at((200+x+offset, 200+y+offset), justacolor) 
                          
                          screen.set_at((200+x+48-offset, 200+y+offset), justacolor)
                            
                        if frame%100==0:
                            sumcolorlist.append(sumcolor[0])
                            sumcolor[0]=0




                           
        if frame%100==0:
            #avgcolor[0]=sumcolor[0]/count/2
            #avgcolor[1]=sumcolor[1]/count
            #avgcolor[2]=sumcolor[2]/count
            for sumcolor in sumcolorlist:
                avgcolorlist.append(5*sumcolor/count)
            #print sumcolorlist
           
            print avgcolorlist,","
            

        if frame%100<3:
          for y in range(200,440):
            for x in range(200,440): 
              screen.set_at((x, y), red)

        pygame.draw.rect(screen, blue, [200,200,240,240], 1)
        

        if frame%100>50:
          pygame.draw.rect(screen, blue, [200,200,240,240], 0)
        
          count=-1
          for x in range(5):
            for y in range(5):
                count+=1

                #if frame%100==51:print cacl
                try:
                  uc=avgcolorlist[count]+25
                except:
                  uc=5*count
                usecolor=(uc*2,uc*2,uc*2)
                pygame.draw.rect(screen, red, [200+x*48,200+y*48,47,47],0)
                pygame.draw.rect(screen, usecolor, [200+x*48,200+y*48,47,47], 0)







        pygame.display.flip()
        mainClock.tick(60)



if __name__ == '__main__': main()
pygame.quit()