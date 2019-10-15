import sys
import timeit
import json
from operator import itemgetter

def usingsort():
   values_to_sort = [5, 2, 6, 1]
   values_to_sort.sort()
   print("sorted_values sort =>", values_to_sort)
usingsort()

def listorder():
  L1= [1,2,8] + [4,5,6]
  L2=['aB','BD','aa']
  L2sort=sorted(L2, key=str.lower, reverse=True)
  print("L1 => ", L1)
  print("L2 => ", L2, "sort = ", L2sort)
  return 0
listorder()

def listsortdup():
   GoT = ['Tony', 'Rocket', 'Scott', 'Steve', 'Rocket', 'Natasha', 'Tony']
   mylist = sorted(list(dict.fromkeys(GoT)), reverse=True)
   print(mylist)
listsortdup()

def sortbylen():
   words = ['banana', 'pie', 'Washington', 'book']
   print("sorted=> ", sorted(words, key=len))
sortbylen()

def reverseword():
   words = ['banana', 'pie', 'Washington', 'book']
   reverse_words= words[::-1]
   print("sorted reverse =>", sorted(reverse_words))
reverseword()

def usinglambda_list():
#A lambda is an anonymous function that: 
#Must be defined inline
#Doesn’t have a name
#Can’t contain statements
#Will execute just like a function
   words = ['banana', 'pie', 'Washington', 'book']
#x[::-1] is called on each element and reverses the word. That reversed output is then used for sorting, but the original words are still returned.
   print("lambda=>", sorted(words, key=lambda x: x[::-1], reverse=True))
usinglambda_list()

def usinglamdba_tupla():
   from collections import namedtuple
   StudentFinal = namedtuple('StudentFinal', 'name grade')
   bill = StudentFinal('Bill', 90)
   patty = StudentFinal('Patty', 94)
   bart = StudentFinal('Bart', 89)
   students = [bill, patty, bart]
   print("sorted lambdatupla=> ", sorted(students, key=lambda x: getattr(x, 'grade'), reverse=True))
usinglamdba_tupla()

def usinglambda_phrases():
#In this sample, a lambda is used to do the following:
#Split each phrase into a list of words
#Find the third element = [2], or word in this case
#Find the second letter [1] in that word
# => o (from rome) r (from around) a (fair) -> reverse 
   phrases = ['when in rome', 
              'what goes around comes around', 
              'all is fair in love and war'
             ]
   phrases.sort(key=lambda x: x.split()[2][1], reverse=True)
   print("usinglambda_phrases =>", phrases)
usinglambda_phrases()

def usinglamnda_sort():
   from collections import namedtuple
   Runner = namedtuple('Runner', 'bibnumber duration')
   runners = []
   runners.append(Runner('2528567', 1500))
   runners.append(Runner('7575234', 1420))
   runners.append(Runner('2666234', 1600))
   runners.append(Runner('2425234', 1490))
   runners.sort(key=lambda x: getattr(x, 'duration'))
   top_five_runners = runners[:2]
   print("top_two =>", top_five_runners)

#Alternatively, the runners could have been sorted using sorted() and using the same lambda: In this scenario with sorted(), the original list of runners is still intact and has not been overwritten. The impromptu requirement of finding every thirty-seventh person to cross the finish line can be accomplished by interacting with the original values:
   runners_by_duration = sorted(runners, key=lambda x: getattr(x, 'duration'))
   top_five_runners = runners_by_duration[:2]
   print("top_two_runners =>", top_five_runners)
   every_third_runners = runners[::3]
   print("every_third_runners =>", every_third_runners)
#which still contains the original order in which the runners 
usinglamnda_sort()

#sort reverse by col3 numeric -> $ sort -t" " -rnk3 filetosort.txt
def sortfile():
   with open('filetosort.txt') as f:
      lines = [line.split(' ') for line in f]

   output = open("filesorted.txt", 'w')
   for line in sorted(lines, key=itemgetter(2,1), reverse=True):
       output.write(' '.join(line))
   output.close()

sortfile()

def sortnodups():
   from collections import OrderedDict
   from itertools import repeat
   myList= [1,5,3,1,9,2,3,8]
   myList = sorted(set(myList))
   print("sortnodups() =>", myList)
#or
   myList= [1,5,3,1,9,2,3,8]
   unique_list = list(OrderedDict(zip(myList, repeat(None))))
   print("unique_list =>", unique_list)
sortnodups()

def manualsortdup():
  input=[1,5,3,1,9,2,3,8]
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  output.sort()
  print("manulsortdup=>", output)
manualsortdup()

def sorttwolists():
  a = [1, 2, 3, 4, 5]
  b = [1, 4, 9, 16, 15]
  c = list(set(a) | set(b))
  print("sorttwolists=>", c)
sorttwolists()

def sortjsonfile():
#Input with ', rather than "
#Clean repetitions
#sort output
   with open('file2.jsn', 'r') as f:
      f_json = f.read().replace('\'', '"')
      d = json.loads(f_json) 
   sorted_d = list(set([''.join(sorted(x, reverse=True)) for x in d]))
   print("sortjsonfile=>", sorted_d)
sortjsonfile()

def removedups():
   mylist=[10, 2, 45, 3, 5, 7, 2, 10, 45, 8, 10]
   listOfNums = list(set(mylist))
   print("removedups listOfNums =>", listOfNums)
   #remove duplicates from it and also want to keep the order of unique elements
   # Iterate over the original list and for each element
   # add it to uniqueList, if its not already there.
   uniqueList = []
   for elem in mylist:
        if elem not in uniqueList:
            uniqueList.append(elem)
   # Return the list of unique elements        
   print("removedups  uniqueList=>", uniqueList)
removedups() 


# What is more efficient => f2, f1 and f3
def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]

# manual vs built-in 
import sys
from operator import itemgetter
from itertools import groupby
import pandas as pd

mylist = [5, 4, 3, 2, 5, 1]

def sort_data(x):
   n = len(x)
   print(n)
   for i in range(n):
   # Traverse the list from 0 to n-i-1
      for j in range(0, n-i-1):
         # Swap if current element is greater than next
         # rev if x[j] < x[j+1]:
         if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
   return x

def remove_duplicates(items):
    unique = [] 
    for item in items: 
        if item not in unique: 
            unique.append(item) 
    return unique 

def sortAndUniq(n):
  output = []
  for x in n:
    if x not in output:
      output.append(x)
  output.sort()
  return output

print(mylist)
sl=sort_data(mylist)
print("Sorted list = ", sl)
nd=remove_duplicates(sl)
print("Sorted  and noduplist = ", nd)

myList = sortAndUniq(mylist)
print("sorted two ", myList)

myList = sorted(set(mylist))
print("sorted with set ", myList)

#Sort given list by frequency and remove duplicates
# initializing list 
test_list = [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5] 
# printing original list 
print("The original list : " + str(test_list)) 
# using sorted() + set() + count() 
res = sorted(set(test_list), key = lambda x: test_list.count(x)) 
ser = sorted(set(test_list), key = lambda x: test_list.count(x), reverse=True) 
# print result 
print("The list after sorting and removal : " + str(res)) 
print("The list after sorting and removal : " + str(ser)) 


#using panda
data = {"Name": ["James", "Alice", "Phil", "James"],
	"Age":  [24, 28, 40, 24],
	"Sex":  ["Male", "Female", "Male", "Male"]}
df = pd.DataFrame(data)
print("dataframe ", df)
df = df.drop_duplicates()
print(df)
df = df.sort_values('Age', ascending=False)
df = df.drop_duplicates(subset='Name', keep='first')
print(df)

#sort dictionari
mydict = {
    'id2': {'name': 'foo','age': 52,},
    'id2': {'name': 'salman','age': 52,},
    'id1':  {'name': 'jay','age':22,},
    'id3': {'name':'Ranveer','age' :26,},
    'id4': {'name': 'jay', 'age': 22,},
}
print("set dict=", set(mydict))

result = {}
for key,value in mydict.items():
   if value not in result.values():
      result[key] = value
print(result)
#then sort
for elem in sorted(result.items()) :
    print(elem[0] , " ::" , elem[1] )


