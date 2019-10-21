import sys

#sort dictionary
mydict = {
    'id2': {'name': 'foo','age': 52,},
    'id2': {'name': 'salman','age': 52,},
    'id1':  {'name': 'jay','age':22,},
    'id3': {'name':'Ranveer','age' :26,},
    'id4': {'name': 'jay', 'age': 22,},
}
print("original mydict =>")
for key, value in mydict.items() :
   print (key, value)

#remove dups in values
nodupdict = {}
for key,value in mydict.items():
   if value not in nodupdict.values():
      nodupdict[key] = value
print("nodupdict values =>")
for key, value in nodupdict.items() :
   print (key, value)

#remove dups in keys => dict don't have dup keys
nodupdict = {}
for key,value in mydict.items():
   if key not in nodupdict.items():
      nodupdict[key] = value
print("nodupdict keys =>")
for key, value in nodupdict.items() :
   print (key, value)

#then sort
print("sorted dict =>")
for elem in sorted(nodupdict.items()) :
    print(elem[0] , " ::" , elem[1] )

# Dict with lists
mydictlist = {
    'id2': [{'name': 'foo','age': 52,},
           {'name': 'salman','age': 52,}],
    'id1': {'name': 'jay','age':22,},
    'id3': {'name':'Ranveer','age' :26,},
    'id4': {'name': 'jay', 'age': 22,},
}
print("mydictlist =>")
for key, value in mydictlist.items() :
   print (key, value)

mylistdict = {
   'key1': ['1','3','4'],
   'key2': ['a','c','b']
}
print("mylistdict =>")
for key, value in mylistdict.items() :
   print (key, value)

#adding
mylistdict.setdefault('jay', []).append('52')
mylistdict.setdefault('jay', []).append('62')
mylistdict.setdefault('salmon', []).append('22')
mylistdict.setdefault('salsa', []).append('2')
print("new mylistdict =>")
for key, value in mylistdict.items() :
   print (key, value)
"""
jay ['52', '62']
salmon ['22']
salsa ['2']
"""
print("jay = ", mylistdict['jay'])
print("jay second value = ", mylistdict['jay'][1])

