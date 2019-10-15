
#using mdules
import sys

#Modules
#import mymodules
#mymodules.mod1('hi')

#from mymodules import mod1
#print(mod1,a)
#del mod1

#from mymodules import reload
#reload(mod1)
#print(x)

#Using namespaces and scopes
#local
def times(x,y):
   return x * y

def func():
   X=88
   print(X)

X=99
func()
print(X)

#global
X=99
def func():
   global X
   X=88
   print(X)
func()
print(X)


#recursive
def mysum(L):
   if not L:
      return 0
   else:
      return L[0] + mysum(L[1:])  #recursive -1 arg

S= mysum([1,5,6])
print(S)

#better to move it to loops
L=[1,2,3,]
sum = 0
while L:
   sum += L[0]
   L = L[1:]
print(sum)


#using arguments
def f1(a,b):
   print('Argument = ', a)
   a = 99
   print('Argument new= ', a)
   return a
	
def f2(*args): 
   print(args)
#no sure how many args passed 
#or want to pass a stored list/tuple to a funtion

def f3(**kargs): 
   print(kargs)
#not sure how many keys args will be passed, 
#or pass a dict as keyword arg

def listarg():
   sys.argv  # -> list of args
   len(sys.argv)  # -> number of args
   sys.argv[0] 
   for i in sys.argv:
     print(i)

# receive by input the number of items, default = 25
numElem=25
numInter=5
if (len(sys.argv) > 1):
   for i in sys.argv:
      numElem=i
print ("Number of elements  ->", numElem)

def mymain(argv):
   grammar = "kant.xml"
   try:
      opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("=h", "--help"):
         usage()
         sys.exit()
      elif opt == "'-d'":
         global _debug
         _debug = 1


#Redefine arguments
def f(x = 100, y = 100): 
   return(x+y, x-y) 
x, y = f(y = 200, x = 100) 
print(x, y) 
#=- 300 -100

#Postional args
def f(*args): print(args)
f()
f(1)
f(1,2)

def f(**args): print(args)
f()
f(a=1,b=2)

#Arg sampples
def min1(*args):
    res = args[0]
    print(res)  #first arg = 3
    for arg in args[1:]:
        print(arg)
        if arg < res:
            res = arg
    return res
print("min=", min1(3,4,1,2))

def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return res

s1='spam'
s2='cl'

R= intersect(s1, s2), union(s1,s2)
print(R)
R= intersect([1,2,3],(1,1,4,2))
U = union([1,2,3],(2,3,4))
print("data = [1,2,3],(1,1,4,2) => Intersect =",R,"Union =",U)

#Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# @my_decorator is just an easier way instead of-> say_whee = my_decorator(say_whee).
@my_decorator
def say_whee():
    print("here Whee!")

#the name say_whee now points to the wrapper() inner function.
say_whee()

#=> Something is happening before the function is called.
#here Whee!
#Something is happening after the function is called.

# reusing decorators
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_whee():
    print("here 2 Whee!")
say_whee()

#decorator arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"
print(return_greeting("me"))



