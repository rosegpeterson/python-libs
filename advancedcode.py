#!/opt/anaconda3/bin/python

###############################################################
# loop regex help count zip  range map filter lambda pickle 
# shelves numarray chain slice permutations 
# repeat power min map pow enumarate 
###############################################################

import sys
import os
import shelve
import pickle
import struct
import glob
import re
import datetime
from itertools import *

#loop
def loopsample():
   while True:
      reply = input('Enter value: ')
      if reply == 'stop':
        break
      try:
        print(reply.upper())
        if reply.isdigit():
            print("Invalid value")
        elif not reply.isdigit():
            print("bad")
        else:
            print("ok")
            pass # placeholder noyhing to do.
      except:
        print("exception")
        if '1'=='1':
            continue  #skip
   else:
       print("adios")

   items=["abc",111, (4,5), 2.01]
   test=[(4,5), 3.14]
   for x in ["abc","def"]:
      print(x, end=' ')
   for key in test:
      for item in items:
         if item ==key:
            print(key, "found")
            break
      else:
         print(key,"not found")

   for i in range(3):
      print(i,'xx')

   i=0
   X='spam'
   while i< len(X):
      print(X[i], end=' ')
      i += 1

   L= list(range(len(X)))
   print(L)

   for i in range(len(X)):
      S = X[1:] + X[:1]
      print(S, end=' ')

#loopsample()

#yield
def yieldsample():
   def nextSquare():
      i = 1;
      # An Infinite loop to generate squares 
      while True:
         yield i*i                
         i += 1  # Next execution resumes 
                  # from this point     
   for num in nextSquare():
      if num > 100:
         break   
      print(num)
   # first  i=1 -> yield 1*1 = 1  Next i=2
   # seconf i=2 -> 2*2 = 4        Next i=3
   # third  i=3 -> 3*3 = 9        Next i=4
   # four   i=4 -> 4*4 = 16       Next i=5
   # ....

   #Sample: function that produces or yields a sequence of values using yield method
   def fib(n): #fib function
      a, b, counter = 0, 1, 0
      while True:
         if ( counter > n):
            return
         yield a
         a, b = b, a + b
         counter += 1

   f = fib(2)
   print ("f=",f)
   while True:
      try:
         print (next(f), end=' ')
      except StopIteration:
         print ("end2\n")
         break

#yieldsample()

#Help and date: 
def helpsample():
   S="1"
   help(S.replace)
   
   x = datetime.datetime.now()
   print(x)  #2019-10-10 18:50:41.923265
   print(x.year)  #2019
   print(x.strftime("%A"))  #Thursday
   x = datetime.datetime(2020, 5, 17)
   print(x)  #2020-05-17 00:00:00
   print(x.strftime("%B"))  #may

#helpsample()

#regex
def regexsample():
   txt = "The rain in Spain"
   x = re.search("^The.*Spain$", txt)
   print(x) #  match='The rain in Spain'
   if re.search("^The.*Spain$", txt):
      print("ok")
   if re.search("^he.*Spain$", txt):
      print("ok")
   else:
      print("nok")
   x = re.findall("a", txt)
   print(x)  # a a
   str = "The rain in Spain"
   x = re.sub("\s", "9", str) 
   print(x)    #The9rain9in9Spain
   x = re.split("\s", str)
   print(x)   #['The', 'rain', 'in', 'Spain']

   list = ["guru99 get", "guru99 give", "guru Selenium"]
   for element in list:
      z = re.match("(g\w+)\W(g\w+)", element)
   if z:
      print((z.groups()))

list = ["guru99 get", "guru99 give", "guru Selenium"]
for element in list:
   print('Looking for  (g\w+)\W(g\w+) in "%s" ->' % (element), end=' ')
   z = re.match("(g\w+)\W(g\w+)", element)
if z:
   print((z.groups()))

   patterns = ['software testing', 'guru99']
   text = 'software testing is fun?'
   for pattern in patterns:
       print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
       if re.search(pattern, text):
           print('found a match!')
   else:
       print('no match')
   
   abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
   emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
   for email in emails:
       print(email)
   
   l=['a cat','a dog','a yacht','a cat']
   string='a cat'
   if string in l:
      print('found a cat in ', l)

   myStr = "this is this example....wow!!! this is really string"
   print(myStr)
   old="this"
   new="THIS"
   max=2
   print("replace old by new max2:",  myStr.replace(old, new, max))

   words = ['how', 'much', 'is[br]', 'the', 'fish[br]', 'no', 'really', 'si']
   print(words)
   c1='REPLACE1'
   c4='REPLACE2'
   c2='no'
   c3='si'
   newWord = map(lambda x: x if (x!=c2 and x!=c3) else \
             c1 if (x==c2) else c4, words) 
  
   # now join each character without space 
   print (''.join(newWord)) #howmuchis[br]thefish[br]REPLACE1reallyREPLACE2

   string="sample of string conversion number99"
   print("String: ", string)
   print(string.upper())
   print(string.capitalize())
   print(string.lower())
   print(":".join("Python"))
   print("split:", string.split(' '))

#regexsample()

#count
def countsamples():
   # vowels list
   vowels = ['a', 'e', 'i', 'o', 'i', 'u']
   # count element 'i'
   count = vowels.count('i')
   # print count
   print('The count of i is:', count)
   # count element 'p'
   count = vowels.count('p')
   # print count
   print('The count of p is:', count)
   #words
   sentence="rosarrosar"
   print('the ar:',sentence,sentence.count('ar'))
   #files
   file  = open('file.txt', 'r').read()
   count = file.count(sentence)
   print('File: ', file, ' number of A: ',file.count('A'))

#countsamples()

# #############################################
# itertools
# #############################################

#zip izip
def zipsample():
   #from itertools import zip
   
   Z= zip('abc', 'xyz')
   LZ = list(Z)
   print("LZ= ",LZ)  #LZ=  [('a', 'x'), ('b', 'y'), ('c', 'z')]

   # izip() -> p, q, =>(p[0], q[0]), (p[1], q[1]),
   # izip('ABCD', 'xy') --> Ax By
   # izip_longest() -> p, q, ->(p[0], q[0]), (p[1], q[1]),…
   # izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

#zipsample()


#range and iter
def rangesample():
   R = range(10)
   print("R= ",R)  # range(0, 10)
   I = iter(R)
   print("I=", next(I))  #0
   print("I=", next(I))  #1
   IL=list(R)
   print("IL=", IL)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   print("len=", len(R), "from: ", R[0], "to ", R[-1])  #len= 10 from:  0 to  9

   for i in range(5):
      print("range5=",i) #range5=0, ... range5=4

#rangesample()


#map
def mapsample():
   M= map(abs, (-1,0,3))
   print("next=", next(M))  # next=1
   print("next=", next(M))  # next=0
   print("next=", next(M))  # next=3

   M= map(abs, (-1,0,3))
   for x in M: print(x)   # 1 0 3

   Celsius = [39.2, 36.5, 37.3, 37.8]
   Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
   print("F=", Fahrenheit)
   #[102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
   C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
   print("C=", C)
   #[39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]

   counters = [1,2,3,4]
   def inc(x): return x + 10
   L=list(map(inc,counters))
   print(L)  #[11, 12, 13, 14]

#mapsample()


#filter
def filtersample():
   F = filter(bool, ['spam', '', 'ni'])  #bool return true if there is a value, no if ''
   FL=list(F)   
   print("FL=", FL)   #FL= ['spam', 'ni']  #filter the ''
   for x in FL:
      if bool(x): print(x)  #spam ni

   # filter
   L=list(filter((lambda x: x> 0), range(-5,5)))
   print("L=",L)  #L= [1, 2, 3, 4]

#filtersample()


# lambda see also in sortsample.py
def lambdasample():
   f = lambda x, y, z: x + y + z
   print(f(2,3,4))   # 2+3+4 = 9

   #It is a single expression anonymous function often used as inline function.  
   #A lambda form in python does not have statements as it is used to make new function object and then return them at runtime
   lambda s: s[:-ord(s[len(s) - 1:])]
   newWords = map(lambda x: str.replace(x, "[br]", "<br/>"), words)
   isequal = ( lambda a,b: a.upper() == b.upper() )

#lambdasample()

# Pickle and Shelves
class Person():
   def __init__(self, name, job=None, pay=0):
      self.name= name
      self.job = job
      self.pay = pay

   def lastName(self):
      return self.name.split()[-1]

   def giveRaise(self, percent):
      self.pay=int(self.pay * ( 1 + percent))

   
def shelvesample():
   #data 
   person1 = Person('salsa engineer 10')
   person2 = Person('tango doctor 50')
   # create persondb.bak  persondb.dat  persondb.dir
   db = shelve.open('persondb')  
   for obj in (person1, person2):
      db[obj.name] = obj   #key
   ld = len(db)
   print("Number of records ", ld, "\n")   # 2
   #read 
   lk = list(db.keys())
   print("Keys =", lk)   # Keys = ['salsa engineer 10', 'tango doctor 50']
   db.close()
   # open shelve
   try:
      dbr = shelve.open('persondb')
   except IOError:
      print ("Error open file", 'persondb')
      #sys.exit()

   # read shelve
   for key in sorted(dbr):
      print(key, '\t=>', key)

   integers = [1, 2, 3, 4, 5]
   #create  dump the integers list to a binary file called sfile.p
   with shelve.open('sfile.s', 'c') as sfile:  #'c' flag tells shelve to open the file for reading and writing
      sfile['ints'] = integers
   #read
   with shelve.open('sfile.s', 'r') as sfile:
      for key in sfile.keys():
         print(repr(key), repr(sfile[key]))  #ints, [1, 2, 3, 4, 5]

#shelvesample()

#pickle
def picklesample():
   integers = [1, 2, 3, 4, 5]
   #create  dump the integers list to a binary file called pfile.p
   with open('pfile.p', 'wb') as pfile:
      pickle.dump(integers, pfile)
   #read
   with open('pfile.p', 'rb') as pfile:
      integers = pickle.load(pfile)
      print("picke file=", integers)  #picke file= [1, 2, 3, 4, 5]
   
#picklesample()

#numpy array
def numpySample():
   import numpy as np
   # Creating a rank 1 Array
   arr = np.array([1, 2, 3])
   print("Array with Rank 1: \n",arr)   # [1 2 3]
 
   # Creating a rank 2 Array
   arr = np.array([[1, 2, 3],
                [4, 5, 6]])
   print("Array with Rank 2: \n", arr)  #[1 2 3] [4 5 6]]
 
   # Creating an array from tuple
   arr = np.array((1, 3, 2))
   print("\nArray created using "
         "passed tuple:\n", arr)        # [1 3 2]

   arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
   print("Initial Array: ")
   print(arr)

   sliced_arr = arr[:2]
                             #[[-1.   2.   0.   4. ]
                             # [ 4.  -0.5  6.   0. ]]
   sliced_arr = arr[:2, ::2]
                             #[[-1.  0.]
                             # [ 4.  6.]]
   print ("Array with first 2 rows and"
       " alternate columns(0 and 2):\n", sliced_arr)

   #operations
   # Defining Array 1
   a = np.array([[1, 2],
                 [3, 4]])
   # Defining Array 2
   b = np.array([[4, 3],
                 [2, 1]])
   # Adding 1 to every element
   print ("Adding 1 to every element:", a + 1)  #[[2 3]
                                                # [4 5]]
   # Subtracting 2 from each element
   print ("\nSubtracting 2 from each element:", b - 2)
                                               #[[ 2  1]
                                               #[ 0 -1]]
   # sum of array elements - Performing Unary operations
   print ("\nSum of all array elements: ", a.sum())  # 10
   # Adding two arrays - Performing Binary operations
   print ("\nArray sum:\n", a + b)  #  [[5 5]
                                    # [5 5]]

   # Square root of Array
   Sqrt = np.sqrt(a)
   print("\nSquare root of a elements: ", Sqrt)
                                    #[[1.         1.41421356]
                                    # [1.73205081 2.        ]]


#numpySample()

#chain
def chainsample():
   c= chain('ABC', 'DEF')
   print("chain:",c)
   for it in c:
      print(it)  # A B C D E F
   L1=[1,2,3]
   L2=['a','b','c']
   for i in chain(L1,L2):
      print("i=",i)  #i=1,i=2,i=3,i=a,i=b,i=c

   c= chain('ABC', 'DEF')
   for i,j in enumerate(c):
      print(i,j) #0 A -1 B -2 C -3 D -4 E -5 F

#islicesample()

def islicesample():
   def islice(iterable, *args):
   # islice('ABCDEFG', 2) --> A B
   # islice('ABCDEFG', 2, 4) --> C D
   # islice('ABCDEFG', 2, None) --> C D E F G
   # islice('ABCDEFG', 0, None, 2) --> A C E G
   s = slice(*args)
   it = iter(range(s.start or 0, s.stop or sys.maxsize, s.step or 1))
   nexti = next(it)
   for i, element in enumerate(iterable):
      if i == nexti:
         yield element
         nexti = next(it)

   l=islice('ABCDEFG',2)
   for i in l:
     print(i)  #A B
   l=islice('ABCDEFG',0,2)
   for i in l:
     print(i) #A B 
   l=islice('ABCDEFG',2,4)
   for i in l:
     print(i) #C D

#islicesample()

def permutasample():
   def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

   p=permutations('ABCD',2)
   c=1
   for i in p:
     print(i, c)  # ('A', 'B') 1    ('A', 'C') 2   ('A', 'D') 3   ...('D', 'C') 12
     c=c+1

#permutasample()


def repeatsample():
   def repeat(object, times=None):
      # repeat(10, 3) --> 10 10 10
      if times is None:
          while True:
             yield object
      else:
          for i in range(times):
             yield object
   r=repeat(10,3)
   print(r)  # 10 10 10  tres veces

   list(map(pow, range(10), repeat(2)))

   print('a'*3)  #'aaa'

   def repstr(string, length):
      return (string * length)[0:length]
   repstr("foobar", 14)

#repeatsample()

def power2():
    sum = 0
    resultado=[]
    for power in range(0, 9):
      sum += 2 ** power
      #print('Power ',   2 ** power, 'Sum', sum)
      #result=result + str(2 ** power) + " sum = " + str(sum) + "\n"
      resultado.append(str(2 ** power) + " sum = " + str(sum))
    return(resultado)

def power3():
    print([1<<exponent for exponent in range(9)])

def powandsumsample():
    sumtot=0
    for power in range(0, 9):
        x = int(math.pow(2,power)) # x = 2 to the power of 'power' var
        sumtot+=sum([x])
        print(x , sumtot)

def powsample():
    print(math.pow(10, 2))
    print(10. ** 2)
    # Using the power operator ** will be faster as it won’t have the overhead of a function call.


def minsample():
   print(min("hello world"))
      #' '
   print(min("helloworld"))
      #'d'
   print(min("helloworld21"))
      #'1'
   print(min(1,2,3))
      #1


def enumerasample():
   for i,v in enumerate(['a','b','c']):
     print(i,v)   # 0 a     1 b    2 c

def reducesample():
   from functools import reduce
   #maximum of a list of numerical values 
   f = lambda a,b: a if (a > b) else b
   seq = [ 1,4,6,1,0,88 ]
   print(reduce(f, seq))  # 6
   #Calculating the sum of the numbers from 1 to 100
   print(reduce(lambda x, y: x+y, range(1,101)))  #5050

#reducesample()


