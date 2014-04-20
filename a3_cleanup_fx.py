#!/usr/bin/env python
#cleaned up image loading, resizing & filtering functions
#by Espen Haehre

import pygame, os, random, copy
from pygame.locals import *


main_dir = os.path.split(os.path.abspath(__file__))[0]


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

  def convert_2d_2_1d(dataset):
    result=[]
    for subset in dataset:
        for data in subset:
          result.append(data)
    return result






def getrandomfilename():
    return letters[random.randint(0,len(letters)-1)]+str(random.randint(1,10))+".jpg"
    
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




if 1:
  def main():
     
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
    #for fdat in filterdataset(my9x9set,[0,230,180,180]):
    for fdat in filterdataset(my9x9set,[0,190]):
         #print fdat
         print str(fdat)[1:27:3]


    

    
    fdataset=filterdataset(mydataset,[128])

    for underset in fdataset:
      #print str(underset)[1:80:3] for sending in facebook
     print str(underset)[1:90:3]




if __name__ == '__main__': main()
print __file__, "<---- avslutter"
