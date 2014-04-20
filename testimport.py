#testimport.py
import a3_cleanup_fx as a3fx


#print whole set
for set in a3fx.returntotalset(9):
      print set

#extract part from total set
print a3fx.returntotalset(20)[a3fx.gnff('Z9')]

