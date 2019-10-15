import sys
try:
   import os
except Exception as exc:
   print("Error import module: ", exc)
   sys.exit(1)


def writefile(filename):
   mydata="1,6,1,8,43,2,3"
   try:
      f = open(filename, 'w')
      f.write(mydata)
      f.close()
   except IOError:
      print('Error writing file "%s" ' % filename)
   return mydata

# call
FILENAME="./file.out"
mydata=writefile(FILENAME)
print("data=>\n", mydata)

