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


main_dir = os.path.split(os.path.abspath(__file__))[0]
black = (255,255,255) #almost white
white = (0,0,0)

letters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
imagenamelist=[]
bitmaplist=[]

def file30x30_2_dataset_as2d(filename):
  result=[]
  imagename= os.path.join(main_dir, 'RESIZED_30x30',filename)
  bitmap = pygame.image.load(imagename)
  da30list=[]
  da30x30list=[]


  #building 30x30 2d list
  for x in range(30):
       da30list.append(0)
  for x in range(30):
       da30x30list.append(copy.deepcopy(da30list))

  #filling list with bitmap values
  nr=0
  for y in range(30):
        for x in range (30):

             pickcolor=bitmap.get_at((x,y))
             da30x30list[nr/30][nr%30]=pickcolor[0]
             nr+=1


  return da30x30list






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


def filterdataset(set, filterlist):
   resultlist=[]
   rl=[]
   for x in range(len(set)):
      rl.append(0)
   for x in range(len(set)):
      resultlist.append(copy.deepcopy(rl))
  

   for x in range(len(set)):
      for y in range(len(set[x])):
        for value in filterlist:
          resultlist[x][y]+=(set[x][y]<value)

   return resultlist

def resize_dataset(dataset,size):
     setlength=len(dataset)
     dasizexsizelist=[]
     dasizelist=[]
     for x in range(size):
       dasizelist.append(0)
     for x in range(size):
       dasizexsizelist.append(copy.deepcopy(dasizelist))

     numlist=copy.deepcopy(dasizexsizelist)
     reslist=copy.deepcopy(dasizexsizelist)


     if len(dataset)==size:
      return dataset

     else:
      if len(dataset)<=size:
         #print "to big"
         for y in xrange(size):
           for x in xrange(size):
             reslist[y][x]=dataset[y*setlength/size][x*setlength/size]

      else:
         for y in xrange(setlength):
           for x in xrange(setlength):
              
              dasizexsizelist[y*size/setlength][x*size/setlength]+=dataset[y][x]
              numlist[y*size/setlength][x*size/setlength]+=1

         for y in range(size):
           for x in range(size):
              reslist[x][y]=dasizexsizelist[x][y]/numlist[x][y]

     return reslist
     #return [reslist,numlist]



print "hi this is not main"

if 1:
  def main():
    print "hi this is the alternative main"
    
    imagename= os.path.join(main_dir, 'RESIZED_30x30',getrandomfilename())
    print imagename
    
    mydataset=file30x30_2_dataset_as2d(imagename)
    print mydataset

    #resize dataset 
    my90x90set=resize_dataset(mydataset,90)
    my9x9set=resize_dataset(my90x90set,9)
    
    for fdat in filterdataset(resize_dataset(mydataset,90),[128]):
       print str(fdat)[1:270:3]

   
    #resizing to smaller dataset might give a blur effect
    #so you might wanna set filterlevel higher..
    print my9x9set
    for fdat in filterdataset(my9x9set,[180]):
         #print fdat
         print str(fdat)[1:27:3]


    

    
    fdataset=filterdataset(mydataset,[128])

    for underset in fdataset:
      #print str(underset)[1:80:3] for sending in facebook
     print str(underset)[1:90:3]




if __name__ == '__main__': main()
print __file__, "<---- avslutter"
