###############################################################
# write read sort : dir files json-files
###############################################################

import sys
try:
   import os
   from itertools import *
except Exception as exc:
   print("Error import module: ", exc)
   sys.exit(1)

DIRNAME="./"
FILENAME="file.txt"

#*********************************************
#read dir
#*********************************************
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

def deldir(dirname):
   os.rmdir("myfolder")

# call
#mydata=readdir(DIRNAME)
#print("data=>\n", mydata)

#*********************************************
#read file
#*********************************************

def fileexist(filename):
   if os.path.exists(filename) and os.path.isfile(filename) and os.path.getsize(filename) > 0:
      print('file "%s" exists.' % filename)
      return True
   else:
      print('file "%s" does not exist or zero' % filename)
      return False

def readwith(filename):
   with open(filename, "r") as fp:
     fileData = fp.read()
     print(fileData)

def readfile(filename):
   if fileexist(filename):
      try:
         f = open(filename, "r")
         print("file => ", f.read())
      except:
         print("error open a file")
      f.close()
 
def readfilepartial(filename):
   if fileexist(filename):
      try:
         f = open(filename, "r")
         print("file partial => ", f.read(5))  #file partial =>  A B D
      except:
         print("error open a file")
      f.close()

def readfilelines(filename):
   if fileexist(filename):
      try:
         f = open(filename, "r")
         print("file lines => ", f.readline())  #read first line =>  A B D 1 4 H f A
         print("file lines => ", f.readline())  #read scond line =>  1 2 3 8 1 4 6 3
      except:
         print("error open a file")
      f.close()
      # or read line by line
      f = open(filename, "r")
      for x in f:
        print("line=", x)

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
      f = open(filename,'wb')  #open wb binary
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

def readbinfile_2():
   import struct
   packed = struct.pack('>i4sh',7,b'spam',8)  #create packed bin files
   print(packed)  # 10 bytes
   file = open('data.bin','wb')  #open wb write binary
   file.write(packed)
   file.close()
	
   data = open('data.bin', 'rb').read()  #read
   print("data=", data)
   print("data 4-8=",data[4:8])
   lista=list(data)
   print("list data=",lista)
	
   unpackedD = struct.unpack('>i4sh',data)  #unpacked bin files
   print("unpacked data=", unpackedD)

def readunicodefile(filename):
   S = 'sp\xc4m'
   print("S non Ascii unicode text for sp\xc4m => ", S, "S[2]=", S[2])
   file = open(filename, 'w', encoding='utf-8')
   file.write(S)
   file.close()
   text=open(filename, encoding='utf-8').read()
   return text

def readunicodefile2(filename):
   S = 'sp\xc4m'
   print("S non Ascii unicode text for sp\xc4m => ", S, "S[2]=", S[2])
   file = open('unidata.txt', 'w', encoding='utf-8')
   file.write(S)
   file.close()
   text=open('unidata.txt', encoding='utf-8').read()
   print("decode UTF-8 text =>", text)
   print("len(text=>", len(text))

def charfile():
   file = open('data.txt')
   while True:
      char = file.read(1)
      if not char: break  #EOF
         print(char)
   file.close()
	
   file = open('data.txt')
   while True:
      line = file.readline()
      if not line: break  #EOF
         print(line.rstrip())
      next(file)
   file.close()
	
   print(" --- \n")
   print(open('data.txt').read())
   print(sys.path)
   L = [line.upper() for line in open('data.txt')]
   print("L=", L)
   L = [line.split() for line in open('data.txt')]
   print("L=", L)
   L = [line.rstrip() for line in open('data.txt') if line[0] == 'Hola']
   print("L=", L)
   L=sorted(open('data.txt'))
   print("L=", L)
   L=list(enumerate(open('data.txt')))
   print("L=", L)
   N=max(open('num.txt'))
   print("N=",N)




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

   #Convert from Python to JSON:
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

reajson2():
   name = dict(fisrt='bob', last='pet')
   rec = dict(name=name, job=['dev','mgr'], age=40)
   print("\nname:", name,"\nrec", rec)
   J=json.dumps(rec)
   print(J)
   O = json.loads(J)
   print(O)
   	
   p = json.load(open('testjson.txt'))
   print("\n p=>", p)
	
   myfile = open("data.txt")
   try:
      print("si")
   finally:
      myfile.close()
	
# Json file: testjson.txt
#	{
#	    "job": [
#	        "dev",
#	        "mgr"
#	    ],
#	    "mame": {
#	         "last": "pet",
#	         "first": "salsa"
#	    },
#	    "age": 20


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

#*********************************************
#write and create a file
#*********************************************
def writefile(filename):
   mydata="1,6,1,8,43,2,3"
   try:
      f = open(filename, 'w')
      f.write(mydata)
      f.close()
   except IOError:
      print('Error writing file "%s" ' % filename)
   f = open(filename, 'r')
   dataread=f.read()
   print(dataread)  #1,6,1,8,43,2,3
   f.close()

#*********************************************
#delete file
#*********************************************
def deletefile(filename):
   if os.path.exists(filename):
      os.remove(filename)
   else:
      print("The file does not exist")

# use call
#writefile(FILENAME)

#######################################################
#  File sample scripts
#######################################################

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
   print("cat sorted file :", infilename,  outfilename1)

   #from cml-> sort <file name> | uniq
   #saving file in list and sorting list
   GoT = ['Tony', 'Rocket', 'Scott', 'Steve', 'Rocket', 'Natasha', 'Tony']
   mylist = sorted(list(dict.fromkeys(GoT)), reverse=True)
   print(mylist)

#Create and Print content of file
	
def print_content_file(sFileName):
	   print('Creating file "%s"' % sFileName, '\n')
	   f = open('sFileName','w')  # write mode
	   f.write('Hola,1 \n')
	   f.write('Salsa,2 \n')
	   f.write('Alo,2 \n')
	   f.write('Tango,2 \n')
	   f.close()
	
	   print('\nPrinting content of file "%s"' % sFileName)
	   try:
	       f = open('sFileName', 'r')
	   except IOError:
	       print ("Error opening file", sFileName)
	       return 1
	  
	   text = f.read()
	   #line = f.readLine()
	   print(text)
	   ts= text.split()
	   print(ts)
	   f.close()
	
	   print('\n Printing split lines of file "%s"' % sFileName)
	   for line in  open('sFileName','r'):
	       print("line",line)
	       parts = line.split(',')
	       print('First: "%s"' % parts[0])

print_content_file("fileN.txt")

Find in files
import os
import sys
import fileinput

# search for word line by line in a file and replace it if found in the same file
def search_replace():
    print ("Text to search for:")
    textToSearch = input( "> " )

    print ("Text to replace it with:")
    textToReplace = input( "> " )

    print ("File to perform Search-Replace on:")
    fileToSearch  = input( "> " )

    tempFile = open( fileToSearch, 'r+' )
    for line in fileinput.input( fileToSearch ):
        if textToSearch in line :
            print('Match Found', textToSearch, 'in', line)
            tempFile.write( line.replace( textToSearch, textToReplace ) )
        else:
            print('Match Not Found', textToSearch, 'in', line)
    tempFile.close()

    input( '\n\n Press Enter to exit...' )
# search_replace()


# search for word in a file and replace it if found in the same file
def read_in_file():
    # Read in the file
    with open('file.txt', 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('HI', 'hi')

    # Write the file out again
    with open('file.txt', 'w') as file:
      file.write(filedata)
read_in_file()


