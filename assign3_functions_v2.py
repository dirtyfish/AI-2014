#assign3_functions.py
import dataset5x5etc as data
numsamples=20

letters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#assumes they are both the length of set1
def getdeviation(set1,set2):
	result=0
	for j in range(len(set1)):
		result+=abs(set1[j]-set2[j])
	return result

#converts 
def getfilefromnum(num,samples=numsamples):
	num+=1
	xnum=num%samples
	if xnum==0:
		xnum=samples
		num-=samples
	result=letters[num/samples]+str(xnum)
	return result

#converts 
def gnff(mystr,samples=numsamples):
	result=int(mystr[1:])#last digits
	for x in range(len(letters)):
	   if letters[x]==mystr[0]:return x*samples+result-1

#converts 
def getnumfromfile(mystr,samples=numsamples):
	result=int(mystr[1:])#last digits
	for x in range(len(letters)):
	   if letters[x]==mystr[0]:return x*samples+result-1

def getscores(mystr,samples=numsamples):
	result=[]
	for x in range(len(letters)*samples):
		tmp=getdeviation(data.set5x5full20[gnff(mystr)], data.set5x5full20[x])
		#print tmp,getfilefromnum(x)
		result.append([tmp,getfilefromnum(x)])
	return sorted(result)




print "A5-A3:",getdeviation(data.set5x5full20[gnff('A5')],data.set5x5full20[gnff('A3')])
print "A1-A3:",getdeviation(data.set5x5full20[gnff('A1')],data.set5x5full20[gnff('A3')])
print getfilefromnum(9)
print getnumfromfile('B1')
print data.set5x5full20[gnff('A1')]
print data.set5x5full20[gnff('A9')]
print sorted([[4,3],3,2,5,[5,1], [2,11], [3,7], [1,9], [4,0]])
print data
print getscores('B8')#will only do two errors from a-z
                     # w1 matches best with u1
                     # m1 matches best with a1 !!