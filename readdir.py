import sys
try:
   import os
except Exception as exc:
   print("Error import module: ", exc)
   sys.exit(1)


def direxist(dirname):
   if os.path.exists(dirname): 
      print('dir "%s" exists.' % dirname)
      return True
   else:
      print('dir "%s" does not exist ' % dirname)
      return False

def readdir(sPath):
   mydata=[]
   if direxist(sPath):
      try:
         for sChild in os.listdir(sPath):
            sChildPath = os.path.join(sPath,sChild)
            if os.path.isdir(sChildPath):
               readdir(sChildPath)
            else:
               print(sChildPath)
      except IOError:
         print('Error reading dir "%s" ' % sPath)
   return mydata

# call
DIRNAME="./"
mydata=readdir(DIRNAME)
print("data=>\n", mydata)
