#!/usr/bin/env python

# 1. Basic image capturing and displaying using the camera module

import pygame, math
import pygame.camera
from pygame.locals import *

red=(255,0,0,255)
blue=(0,0,255,255)
black=(0,0,0,255)
BLACK=(222,112,62,255)
xposi=0
yposi=0
screensize=(640,480)
WINDOWHEIGHT=screensize[1]
WINDOWWIDTH=screensize[0]
camzoom= 1000
odistance=100


#pos3d = [WINDOWWIDTH/2+100,WINDOWHEIGHT/2+100,camzoom]
#pos3d2 = [WINDOWWIDTH/2+100,WINDOWHEIGHT/2+100,camzoom/2]
#pos2d = [WINDOWWIDTH/2,WINDOWHEIGHT/2]



def v3ds(a3dpos):  #now equal to v3dr
    #diffx=a3dpos[0]  #-WINDOWWIDTH/2
    #diffy=a3dpos[1]  #-WINDOWHEIGHT/2
    diffxf=1.0*camzoom*a3dpos[0]/(a3dpos[2]+camzoom)
    diffyf=1.0*camzoom*a3dpos[1]/(a3dpos[2]+camzoom)
    returnpos=[int(WINDOWWIDTH/2+diffxf), int(WINDOWHEIGHT/2+diffyf)]
    #print returnpos
    return returnpos




class VideoCapturePlayer(object):

   size = ( 160, 120 )
   screensize=(640,480)
   frames=0
   xposi=0
   yposi=0
   distance=100
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

   def create3dsph(self,position,rad,height,stepsrad,steph):
    fpos=[0,0,0]
    tpos=[0,0,0]
    twist=0
    degrees=360
    dataset=[]


    for y in range(steph):
        getheight=height/(steph-1)*y
        #insin=(y-(steph+1)/2)
        k=2.0*y/(steph-1)-1 #ra #dius av kulesnitt
        radius=rad*math.cos((math.asin(k))) #radius av kulesnitt
        dataset.append([getheight,radius])
        #radius=rad*math.sin(insin)
        #getheight=y*30
        for x in range(stepsrad):
          
              #draw circles
          fpos[0]=position[0]+radius*math.cos(math.radians(degrees*x/stepsrad+twist))
          fpos[1]=position[1]+getheight
          fpos[2]=position[2]+radius*math.sin(math.radians(degrees*x/stepsrad+twist))
          tpos[0]=position[0]+radius*math.cos(math.radians(degrees*(x+1)/stepsrad+twist))
          tpos[1]=position[1]+getheight
          tpos[2]=position[2]+radius*math.sin(math.radians(degrees*(x+1)/stepsrad))
          pygame.draw.line(self.display, BLACK, v3ds(fpos),v3ds(tpos))
    for y in range(len(dataset)-1):
       getheight=dataset[y][0]
       radius=dataset[y][1]
       getheight2=dataset[y+1][0]
       radius2=dataset[y+1][1]
       for x in range(stepsrad):
          fpos[0]=position[0]+radius*math.cos(math.radians(degrees*x/stepsrad+twist))
          fpos[1]=position[1]+getheight
          fpos[2]=position[2]+radius*math.sin(math.radians(degrees*x/stepsrad+twist))
          tpos[0]=position[0]+radius2*math.cos(math.radians(degrees*x/stepsrad+twist))
          tpos[1]=position[1]+getheight2
          tpos[2]=position[2]+radius2*math.sin(math.radians(degrees*x/stepsrad+twist))
          pygame.draw.line(self.display, BLACK, v3ds(fpos),v3ds(tpos))
    return 

   def get_and_flip(self):
       # if you don't want to tie the framerate to the camera, you can check and
       # see if the camera has an image ready.  note that while this works
       # on most cameras, some will never return true.
       odistance=self.distance
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
                if getcolor[0]-50>getcolor[1] and getcolor[0]-50>+getcolor[2]:
                  getcolor=blue #switching reds to blue
                  countdots+=1
                  sumdots[0]+=x
                  sumdots[1]+=y


                self.display.set_at([640-x*4,0+y*4],getcolor)
       sumdots[0]/=countdots+(countdots==0)#average and no zeroes
       sumdots[1]/=countdots+(countdots==0)#average and no zeroes
       sumdots[0]<<=3
       sumdots[1]<<=3
      

       self.xposi=15*self.xposi+sumdots[0]
       self.yposi=15*self.yposi+sumdots[1]
       self.xposi>>=4
       self.yposi>>=4
       
       if countdots<6:
        countdots=0
       else:

         if countdots<60:countdots=60
         if countdots>500:countdots=500
         distance=(odistance*9+400/math.sqrt(countdots+1))/10
         self.distance=odistance=distance
         #self.display.blit(self.snapshot, (self.screensize[0]+self.size[0]*2-self.xposi-self.size[0]/2,-self.size[1]*2+self.yposi-self.size[1]/2))
         
         self.create3dsph([3*(self.screensize[0]+self.size[0]*2-self.xposi-self.size[0]/2)-WINDOWWIDTH/2,3*(-self.size[1]*2+self.yposi-self.size[1]/2)-WINDOWHEIGHT/2,5000-100*distance],200,200,9,9)
       distance=400/math.sqrt(countdots+1)
       if self.frames%30<2:print self.frames, countdots, "Distance:", int(distance)," cm"
       pygame.display.flip()
       self.frames+=1

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
