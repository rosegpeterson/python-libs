###############################################################
# object types in python
# mutuable:
#	• List
#	• Sets
#	• Dictionaries
#Immutable:
#	• Strings
#	• Tuples
#	• Numbers (int, float)
#	• Bool
#	• Unicode
###############################################################
import sys
import array
import string


# **********************************************
#Mutable Object Types
# **********************************************

# ---------------------------------------------
print("MANAGING LISTS")
# ---------------------------------------------

def listsample():
   numElem=12
   i=0
   L = [1,'a',1.6]
   print(L)
   
   myList=[]
   x = [0 for i in range(numElem)]
   for i in range(numElem):
      myList.append(i+1)
   assert len( myList) == numElem
   print ("list 1 =>", myList)
   
   #get multiple of 5
   fiveM = [x for x in myList if x % 5 == 0]
   print ("Multiple 5 = ", fiveM)
   
   # change value
   myList[1]=99
   print("my new list=>", myList)
   
   #nesting lists: 
   M= [ [1,2,3],[3,4,5]]  
   print(M)
   col2=[row[1] for row in M]  #-> get column 2
   print(col2)
   
   list = [ 'abcd', 786, 2.23, 'john', 70.2 ]
   tinylist = [123, 'john']
   print (list)
   print (list[0], list[1:3])  #-> abcd 786, 2.23
   print (list[0], list[1:4])  #-> abcd 786, 2.23 'john'
   print (list[0], list[2:4])  #-> abcd 2.23 'john'

   # modify list append to add/pop to delete/sort/reverse
   mylist=[1,4,2,7,3]
   print(mylist[1])  # 4
   print(mylist[:-1])  # 1,4,2,7  menos-1ultimo
   print(mylist[:-2])  # 1,4,2    menos-2ultimo
   print(mylist[::-1])  # 3,7,2,4,1
   print(mylist[-1])   # 3  ultimo
   #Return the third, fourth, and fifth item:
   print(mylist[3:5])   # 7,3
   #Return the second, third, fourth
   print(mylist[2:5])   # 2,7,3

   #change value
   mylist[2]=10
   print(mylist)

   #add item
   mylist.append('123')
   print(mylist)
   #Insert an item as the second position
   mylist.insert(1,100)
   print(mylist)  # 1,100,4,...

   #remove 4
   mylist.remove(4)
   print(mylist)  # 1,100,10,...
   #The pop() method removes the specified index, (or the last item if index is not specified)
   mylist.pop()
   print(mylist)  # 1,100,10,7,3  removed 123 was last one
   #The del keyword removes the specified index:
   del mylist[0]  # 100,10,...
   print(mylist)  # 100,10,7,3  removed 1 was 0 item
   mylist.clear()  # empty list
   del mylist # delte the list

   #Make a copy of a list with the copy() method:
   thislist = ["apple", "banana", "cherry"]
   mylist = thislist.copy()
   print(mylist)
  
   #Join two list:
   list1 = ["a", "b" , "c"]
   list2 = [1, 2, 3]
   list3 = list1 + list2
   print(list3)
   print(list2.sort())

   # To merge, sort, remove dups from 2 lists
   a = [13, 4, 8, 1, 1, 18]
   b = [10, 5, 7, 1, 4, 19, 1]
   ml=a + b
   print("merge list ", ml)  #[13, 4, 8, 1, 1, 18, 10, 5, 7, 1, 4, 19, 1]
   ndl=set(ml)
   print("removed dup and sort list ", ndl) #{1, 4, 5, 7, 8, 10, 13, 18, 19}
   print('list results {} {} = {}'.format(a,b,ndl))
	
   #append list2 to list1
   for x in list2:
      list1.append(x)
   print(list1)

   #extend() method to add list2 at the end of list1:
   list1.extend(list2)
   print(list1)

   #loop
   # break , continue, pass statement
   list=[1,2,3,4]
   print ("list=", list)
   it = iter(list)
   for x in it:
       print (x, end=" ")
   while True:
      try:
         print (next(it))
      except StopIteration:
         print ("end1\n")
         break

   #sort lists
   L2=['aB','BD','aa']
   sorted(L2, key=str.lower, reverse=True)
   print("L2=",L2)

   matrix = [[1,2,3],[4,6,5],[7,8,9]]
   print("matrix:", matrix[1], "and ",  matrix[1][1])  #  [4, 6, 5] and 6
   matrix[1][1]='10'
   print(matrix)  # [[1, 2, 3], [4, '10', 5], [7, 8, 9]]

   #index
   L3= ['sa','ta','fe']
   print(L3.index('sa'))  # 0 posion sa
   L3.insert(1,'ro')  
   L3.remove('ta')
   print(L3)   # ['sa', 'ro', 'fe']
   L3.pop(1)
   print(L3, L3.count('ro'))  # ['sa', 'fe'] 0

   #lists nested
   rec = {'name': 'bob',
          'jobs': ['dev','man'],
          'home': {'state':'wa', 'zip':98177}}
   print(rec['name'],rec['jobs'], rec['jobs'][1])  #bob ['dev', 'man'] man

listsample()


# ---------------------------------------------
print("MANAGING ARRAYS")
# ---------------------------------------------

def arraysample():
   numElem=12
   i=0

   myArray = array.array('i')
   myArray = array.array('i', (i+1 for i in range(numElem)))
   assert len(myArray) == numElem
   print ("array 1 =>", myArray)
   
   #get multiple of 5
   fiveM = [x for x in myArray if x % 5 == 0]
   print ("Multiple 5 = ", fiveM)
   
   # change value


# arraysample()

# ---------------------------------------------
print("MANAGING SETS")
# ---------------------------------------------

def setsample():
   x = set('abcd')   #{'a', 'c', 'b', 'd'}
   print(x)
   print(type(x))
   y = set('xycza')  #{'y', 'c', 'x', 'a', 'z'}
   print(y)
   S = set([1,3,2])  # {1, 2, 3}
   print(S)
   print(type(S))

   z = x.intersection(y)
   print("intersection x y",z)  # z= {'a', 'c'}
   z.add('foo')
   print("add foo to z ",z)     #{'a', 'foo', 'c'}

   y.remove('y')
   print("remove y from y ",y)   # {'c', 'x', 'z', 'a'}
   S.union([5,6])
   print("S union 5 6 ", S)     #{1, 2, 3}
   S1=S.union([5,6])
   print("S1 union 5 6 ", S1)     #{1, 2, 3, 5, 6}

   S.intersection((1,3,5))
   print("interesect S 1,3,5", S)  # {1, 2, 3}
   S2=S.intersection((1,3,5))
   print("interesect S2 1,3,5", S2)  # {1, 3}

   print("set:", x, y, z, x - y, x | y, x ^ y, x > y)

   if 'a' in x:
      print("a in x")

   mys = set('spam')
   print(mys)  # {'a', 's', 'm', 'p'}

   #create a ser
   thisset = {"apple", "banana", "cherry"}
   print(thisset)   # {'banana', 'apple', 'cherry'}
   for x in thisset:
      print(x)
   print("banana" in thisset)  #True
   print(len(thisset))

   #Add an item to a set, using the add() method:
   thisset = {"apple", "banana", "cherry"}
   thisset.add("orange")   #{'banana', 'orange', 'apple', 'cherry'}
   print(thisset)
   thisset.update(["orange", "mango", "grapes"]) 
   print(thisset)  #{'cherry', 'orange', 'banana', 'mango', 'grapes', 'apple'}
   thisset.remove("banana")
   print(thisset)  #{'cherry', 'orange', 'mango', 'grapes', 'apple'}
   thisset.discard("orange")
   print(thisset)  #{'mango', 'apple', 'grapes', 'cherry'}
   x = thisset.pop() #remove last item
   print(thisset)  #{'mango', 'apple', 'grapes'}
   thisset.clear()
   del thisset

   #join
   set1 = {"a", "b" , "c"}
   set2 = {1, 2, 3}
   set3 = set1.union(set2)
   print(set3)  #{1, 2, 3, 'a', 'c', 'b'}
   #The update() method inserts the items in set2 into set1:
   set1 = {"a", "b" , "c"}
   set2 = {1, 2, 3}
   set1.update(set2)
   print(set1)

# setsample()

# ---------------------------------------------
print("MANAGING DICTIONARY")
# ---------------------------------------------
def dictionarysample():
   from collections import defaultdict
   D= {'uno': '1', 'dos':'2','numero':1}
   D['numero'] += 1 
   print(D) # {'dos': '2', 'uno': '1', 'numero': 2}

   D={}
   D['name'] = 'salsa'
   D['color'] = 'red'
   print(D)          # {'name': 'salsa', 'color': 'red'}
   print(D['name'])
   for key, value in D.items() :
      print (key, value)
   print(D.items())
   print(D.keys())
   print(D.values())

   mydic = {}
   mydic['mykey1'] = 'myvalue1'
   mydic['mykey2'] = 'myvalue2'
   mydic['mykey3'] = 'myvalue3'
   for key, value in mydic.items() :
      print (key, value)
   # To print a specific key (for example key at index 1)
   print([key for key in mydic.keys()][1])  # => mykey2

   # To print a specific value (for example value at index 1)
   print([value for value in mydic.values()][1]) # => myvalue2

   # To print a pair of a key with its value (for example pair at index 2)
   print(([key for key in mydic.keys()][2], [value for value in mydic.values()][2])) #=> ('mykey3', 'myvalue3')

   # To print all pairs of (key, value) one at a time
   for e in range(len(mydic)):
       print(([key for key in mydic.keys()][e], [value for value in mydic.values()][e]))

   # To print all pairs (key, value) in a tuple
   print(tuple(([key for key in mydic.keys()][i], [value for value in mydic.values()][i]) for i in range(len(mydic))))

   # To print pair (key, value) for a key
   print(f'mykey1: {mydic["mykey1"]}')  #=> mykey1: myvalue1

   #dict sample
   myText="""This is a test to initaliza a dictionary"""
   words = myText.split()

   # 1
   d = {}.fromkeys(words,0)
   for w in words:
      d[w] += 1
   print('1. ',  d)

   # 2
   d = {}
   for w in words:
      d[w] = d.get(w,0) + 1
   print('2. ',  d)

   # 3
   d = defaultdict(int)
   for w in words:
      d[w] += 1
   print('3. ',  d)

   # construct dictionary whose values are lists.
   cities = {'San Francisco': 'US', 'London':'UK',
           'Manchester':'UK', 'Paris':'France',
           'Los Angeles':'US', 'Seoul':'Korea'}
   # => {'US':['San Francisco', 'Los Angeles'], 'UK':[,], ...}

   print "using collections.defaultdict()"
   d1 = defaultdict(list) # initialize dict with list
   for k,v in cities.items():
      d1[v].append(k)
   print(d1)

   print "using dict.setdefault(key, default=None)"
   d2 = {}
   for k,v in cities.items():
      d2.setdefault(v,[]).append(k)
   print(d2)

#dictionarysample()



# **********************************************
#Immutable Object Types
# **********************************************

# ---------------------------------------------
print("MANAGING STRINGS")
# ---------------------------------------------

def stringsample():
   S='hola' 
   sys.stdout.write('mystring ' + S + '\n')
   print("string 1 =>", S)
   print(S.find('a'))  #return position of a=3rd char

   S.replace('a','A')
   print(S) # no changes immutable
   T=S.replace('a','A')
   print(T)
   T=S.upper()
   print(T)
   print(S.isalpha()) 

   S='1,2,3' 
   S.split(',') # list
   print(S)
   print(S.isalpha()) 

   S='   h o l a   '
   print(S.rstrip())  # remove whitespace on right
   print(S.lstrip())  # remove whitespace on left

   #slicing strings: 1, 2 ... slice from beginning, -1, -2.... slices at the end
   S='spam'
   print(S, S[1:3], S[:-1], S[1:])   # S=spam => pa spa pam
   S = 'abcdefghijklmmop'
   print(S[1:10:2])  #skip items  bcdefghij -> skip 1 bdfhj
   S = "salsa"
   print(S[::-1])  # reverse aslas

   line = 'aa bb cc'
   col1=line[0:3]
   print(line, "col1=", col1)  # aa bb cc col1= aa
   cols=line.split()
   print(cols)  #['aa', 'bb', 'cc']

   # print  formats
   S= 'That is %d %s bird' % (1,'life')
   print(S)   #That is 1 life bird
   
   #convert string lowercase and reverse word
   print(" is_palindrome Deleved")
   word='Deleveled'
   reverse_word=(word[::-1])
   print (reverse_word.lower())
   if reverse_word.lower() == word.lower():
     print(word, "is _palindrome")
   else:
     print(word, "is NOT _palindrome")

   filedata = "uno,dos,tres"
   newdata=filedata.replace('uno', 'UNO')
   print(newdata)

#stringsample()

# ---------------------------------------------
print("MANAGING TUPLES")
# ---------------------------------------------
def tuplassample():
   T=(1,2,3,4,5,6)
   print("tuple=>",T)
   print(T[0])    # 1
   print(T[-1])   # 4
   print(T[2:5])   # 3,4,5
   #items from index -4 (included) to index -1 (excluded)
   print(T[-4:-1])   # 3,4,5

   #change
   try:
     T[1]=4  # ERROR
   except:
     print("no")

   #add element
   try:
      T[7] = "orange" # This will raise an error
   except Exception as e:
     print("no2",e)

   #convert the tuple into a list to make changes
   x = ("apple", "banana", "cherry")
   y = list(x)
   y[1] = "kiwi"
   x = tuple(y)
   print(x) #-> apple kiwi cherry
   print(len(x)) #-> apple kiwi cherry
   print(type(x))

   for z in x:
      print(z)

   if "apple" in x:
      print("Yes, 'apple' is in the fruits tuple")

   #Join two tuples:
   tuple1 = ("a", "b" , "c")
   tuple2 = (1, 2, 3)
   tuple3 = tuple1 + tuple2
   print(tuple3) # => ('a','b','c',1,2,3)

   mytuple = ( 'abcd', 786, 2.23, 'john', 70.2 )
   tinytuple = (123, 'john')
   print (mytuple)
   print (mytuple[0], mytuple[1:3], tinytuple * 2) #-> abcd (786,2,23) ((123, 'john', 123, 'john')

   #slices with tuplas:     
   #   1  2  3  4  5  6  7  8  9 10  11
   T= (9, 4, 1, 6, 7, 3, 8, 3, 4, 7, 12)
   len(t) # real (counting from 1)
   #Right Shift:
   t[1::] # new list = starts second element - starts counting from 0=(4, 1, 6, 7, 3, 8, 3, 4, 7, 12)
   T[2::] # new list = starts in the 3rd element =(1, 6, 7, 3, 8, 3, 4, 7, 12)
   t[1] # second element                         =(4)
   t[1:] # = t[1::]
   T[2:] # = t[2::]
   # Reverse Shift:
   T[::1] #   No changes
   T[::-1] #  reverse                            =(12, 7, 4, 3, 8, 3, 7, 6, 1, 4, 9)
   T[::-2]  # reverse starts with the third element  =(12,4,8,7,1,9)
   #Mixed:
   t[1::1]  # =(   4, 1, 6, 7, 3, 8, 3, 4, 7, 12)
   t[1::2]  #=(   4,     6,      3,      3,    7)
   t[2::1]  #=(        1, 6, 7, 3, 8, 3, 4, 7, 12)  
   t[2::2]  #=(        1,    7,      8,     4,     12)                 
   t[1::3]  #=(   4,         7,          3,         12)
   T[1:3]   #desde 2 Hasta el tercer  =(  4, 1)
   t[1:4]   #desde 2 Hasta el 4to desde 0=(   4, 1, 6)                             
   T[2:4]   #desde  3 hasta el 4 = (      1, 6)
  
# tuplassample()

# ---------------------------------------------
print("MANAGING NUMBERS")
# ---------------------------------------------

def numbersample():
   import math
   import random
   import decimal
   int = 10
   float = 15.20
   complex = 4.5e-7

   # OPERATORS
   a=1
   b=2
   print(a+b, a-b, b%a, a**b, 9//2)
   c=a+b
   c-=a
   c/=a
   print(c)
   a=60 #0011 1100
   b=13 #0000 1101
   print(a&b, a|b, a^b, ~a)
   y=bin(a)
   print(y)

   # in true if finds var in a sequence - not in
   # is if variable point to same object - is not
   if (a == 60) : print ("values a is ", a)

   # print(int(2.14), float(2), 28 % 5) # %=reminder
   print(10//4, 10/4)
   print(0b11111111, 0xFF, bin(255), hex(255))  #binary 255, hex
   print("math ops",math.pi, math.sqrt(122), sum((1,2,3)), min(3,2,4), round(2.55))
   print("closes number below value:", math.floor(2.5))
   print("truncate frac:",math.trunc(2.5))

   x = 1
   print("bitwise treats int as string of bin bits", x)
   y = x << 2
   # y = x & 1 or x | 2
   print("shift left 2 bits 0100", y)

   print("random: ", random.random(), random.randint(1,20), random.choice(["A", "b", "c"]))

   d= decimal.Decimal('3.141')
   print("d=", d)
   print(d+1)

   #booleans and none placeholder
   print(1>2, 2>1)  #False True
   X= None
   print(X)
   L = [None] * 5  
   print("list of 5 nodes=", L) #list of 5 nodes= [None, None, None, None, None]
   if type(L) == list:
      print("yes! is a list", type(L))

# numbersample()

