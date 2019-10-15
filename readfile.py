import sys
try:
   import os
except Exception as exc:
   print("Error import module: ", exc)
   sys.exit(1)


def fileexist(filename):
   if os.path.exists(filename) and os.path.isfile(filename) and os.path.getsize(filename) > 0:
      print('file "%s" exists.' % filename)
      return True
   else:
      print('file "%s" does not exist or zero' % filename)
      return False

def readfile(filename):
   mydata=[]
   if fileexist(filename):
      try:
         f = open(filename, 'r')
         mydata = f.read()
         f.close()
      except IOError:
         print('Error reading file "%s" ' % filename)
   return mydata

def readfile2(filename):
   mydata=[]
   if fileexist(filename):
      try:
         with open(filename, "r") as f:
            mydata = f.read()
      except IOError:
         print('Error reading file "%s" ' % filename)
   return mydata


def readfile3(filename):
   mydata=[]
   if fileexist(filename):
      try:
         f = open(filename, "r")
         mydata = f.readline()
      except IOError:
         print('Error reading file "%s" ' % filename)
   return mydata
   

def readbinfile(filename):
   import struct
   packed = struct.pack('>i4sh',7,b'spam',8)  #create packed bin files
   try:
      f = open(filename,'wb')  #open wb write binary
      f.write(packed)
      f.close()
   except Exception as exc:
      print('Error reading file "%s" ' % exc)

   mydata=[]
   if fileexist(filename):
      try:
         mydata = open(filename, 'rb').read()  #read
         unpackedD = struct.unpack('>i4sh',mydata)  #unpacked bin files
         print("unpacked data=", unpackedD)
      except IOError:
         print('Error reading file "%s" ' % filename)
   return list(mydata)


def readunicodefile(filename):
   S = 'sp\xc4m'
   print("S non Ascii unicode text for sp\xc4m => ", S, "S[2]=", S[2])
   file = open(filename, 'w', encoding='utf-8')
   file.write(S)
   file.close()
   text=open(filename, encoding='utf-8').read()
   return text

def readjsonfile(filename):
   import json
   p = json.load(open(filename))
   #p = json.dumps(p)

   # some JSON:
   x =  '{ "name":"John", "age":30, "city":"New York"}'
   # parse x:
   y = json.loads(x)
   # the result is a Python dictionary:
   print(y["age"])

   Convert from Python to JSON:
   # a Python object (dict):
   x = {
     "name": "John",
     "age": 30,
     "city": "New York"
   }
   # convert into JSON:
   y = json.dumps(x)
   # the result is a JSON string:
   print(y)

   #Use the indent parameter to define the numbers of indents:
   json.dumps(x, indent=4)
   #Use the separators parameter to change the default separator:
   json.dumps(x, indent=4, separators=(". ", " = "))

   return p


# use call
FILENAME="./file.txt"
mydata=readfile(FILENAME)
print("data=>\n", mydata)

FILENAME="./file.bin"
mydata=readbinfile(FILENAME)
print("data=>\n", mydata)

FILENAME="./filedata.txt"
mydata=readunicodefile(FILENAME)
print("data=>\n", mydata)

FILENAME="./file.jsn"
mydata=readjsonfile(FILENAME)
print("data=>\n", mydata)

FILENAME1="./file1.txt"
FILENAME2="./file2.txt"
mydata=readzipfiles(FILENAME1,FILENAME2)
print("data=>\n", mydata)

