###############################################################
# write read sort : dir files json-files
###############################################################

import sys
try:
   import os
   from itertools import izip
   from itertools import izip_longest
except Exception as exc:
   print("Error import module: ", exc)
   sys.exit(1)

#read dir
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

# read file
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

   # read using itertools zip
   fileName1="test1"
   fileName2="test2"

   def read_zip(fileName1,fileName2):
      with open(fileName1) as textfile1, open(fileName2) as textfile2:
         textFiles= izip_longest(textfile1, textfile2)
         for x, y in textFiles:
            if x: x = x.strip()
            if y: y = y.strip()
            print("{0}\t{1}".format(x, y))

   # manual read line by line
   def read_file(file1,file2,line1,line2):
      if line1:
         line1 = file1.readline()
       if line2:
          line2 = file2.readline()
       if line1 or line2:
          print("Line1 = ", line1, "Line2: ", line2)
          read_file(file1,file2,line1,line2)
       else:

          return(0)
   def callreadfile():
      try:
         file1 = open(fileName1, 'r')
         file2 = open(fileName2, 'r')
         print('Printing content of files')
         read_file(file1,file2,1,1)
         file1.close()
         file2.close()
      except IOError:
         print ("Error opening file(s)", fileName1, fileName2)
         return 1
      print('Printing content of files - zip option')
      read_zip(fileName1,fileName2)

#write a file
def writefile(filename):
   mydata="1,6,1,8,43,2,3"
   try:
      f = open(filename, 'w')
      f.write(mydata)
      f.close()
   except IOError:
      print('Error writing file "%s" ' % filename)
   return mydata

# use call
FILENAME="./file.out"
mydata=writefile(FILENAME)
print("data=>\n", mydata)

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

#sort file
def sortfile():
   infilename="./foo.in"
   outfilename="./foo.out"
   outfilename1="./foo1.out"

   #manual
   with open(infilename, 'r') as fin, open(outfilename, 'w') as fout:
       lines = fin.readlines()
       numbers = sorted(int(n) for n in lines)
       lines_read = set() # holds lines already read
       for line in numbers:
          if line not in lines_read: # not a duplicate
             fout.write(str(line)+'\n')
             lines_read.add(line)

   #using builtin
   uniqlines = sorted(set(open(infilename).readlines()), key = int)
   outfile = open(outfilename1, "w")
   outfile.write(str(uniqlines))
   outfile.close()

   #from cml-> sort <file name> | uniq
   #saving file in list and sorting list
   GoT = ['Tony', 'Rocket', 'Scott', 'Steve', 'Rocket', 'Natasha', 'Tony']
   mylist = sorted(list(dict.fromkeys(GoT)), reverse=True)
   print(mylist)

