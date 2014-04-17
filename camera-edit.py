#!/usr/bin/env python

# 1. Basic image capturing and displaying using the camera module

import pygame
import pygame.camera
from pygame.locals import *

red=(255,0,0,255)
blue=(0,0,255,255)
black=(0,0,0,255)
xposi=0
yposi=0

class VideoCapturePlayer(object):

   size = ( 160, 120 )
   screensize=(640,480)
   frames=0
   xposi=0
   yposi=0
   def __init__(self, **argd):
       self.__dict__.update(**argd)
       super(VideoCapturePlayer, self).__init__(**argd)

       # create a display surface. standard pygame stuff
       self.display = pygame.display.set_mode( self.screensize, 0 )

       # gets a list of available cameras.
       self.clist = pygame.camera.list_cameras()
       if not self.clist:
           raise ValueError("Sorry, no cameras detected.")

       # creates the camera of the specified size and in RGB colorspace
       self.camera = pygame.camera.Camera(self.clist[0], self.size, "RGB")

       # starts the camera
       self.camera.start()

       self.clock = pygame.time.Clock()

       # create a surface to capture to.  for performance purposes, you want the
       # bit depth to be the same as that of the display surface.
       self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

   def get_and_flip(self):
       # if you don't want to tie the framerate to the camera, you can check and
       # see if the camera has an image ready.  note that while this works
       # on most cameras, some will never return true.
       self.frames+=1
       if 0 and self.camera.query_image():
           # capture an image

           self.snapshot = self.camera.get_image(self.snapshot)
       self.snapshot = self.camera.get_image(self.snapshot)
       
       #self.snapshot = self.camera.get_image()

       # blit it to the display surface.  simple!
       #self.display.blit(self.snapshot, (0,0))
       self.display.fill(black)
       if 1:
         countdots=0
         sumdots=[0,0]
         for y in range(0,120,2):
               for x in range(0,160,2):
                getcolor=self.snapshot.get_at((0+x, 0+y))
                if getcolor[0]-30>getcolor[1] and getcolor[0]-30>+getcolor[2]:
                  getcolor=blue #switching reds to blue
                  countdots+=1
                  sumdots[0]+=x
                  sumdots[1]+=y


                self.display.set_at([640-x*4,0+y*4],getcolor)
       sumdots[0]/=countdots+(countdots==0)#average and no zeroes
       sumdots[1]/=countdots+(countdots==0)#average and no zeroes
       sumdots[0]<<=3
       sumdots[1]<<=3
      

       self.xposi=7*self.xposi+sumdots[0]
       self.yposi=7*self.yposi+sumdots[1]
       self.xposi>>=3
       self.yposi>>=3
       
       self.display.blit(self.snapshot, (self.screensize[0]+self.size[0]*2-self.xposi-self.size[0]/2,-self.size[1]*2+self.yposi-self.size[1]/2))
       pygame.display.flip()

   def main(self):
       going = True
       while going:
           events = pygame.event.get()
           for e in events:
               if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                   going = False



           self.get_and_flip()
           
           self.clock.tick()
           #print (self.clock.get_fps())

def main():
    pygame.init()
    pygame.camera.init()
    VideoCapturePlayer().main()
    pygame.quit()

if __name__ == '__main__':
    main()
