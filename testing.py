a=3
b=id(a)
b=id(b)
print id(a),a
print id(b),b

print b
print a



d=[]

c=[]

class ref:
    def __init__(self, obj): self.obj = obj
    def get(self):    return self.obj
    def set(self, obj):      self.obj = obj


e=ref(b)
print e.get();
print e.set(3);
print "eg",e.get();
print e
f=e
f=ref(a)
a=100
print f.get()

print 10>>3
print c
print (4<5)*3