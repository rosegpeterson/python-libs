# classes
import sys

class MyClass:
    def setdata(self, namevalue, cityvalue):
        self.name = namevalue
        self.city = cityvalue
        self.status = "Active"

    def display(self):
        print("Myclass data= ", self.name, self.city, self.status)

# create two instances
x=MyClass()
x.setdata('rose','bogota')
x.display()

y=MyClass()
y.setdata('salsa','seattle')
y.display()

#create subclass
class SecondClass(MyClass):
    def display(self):
        print('SecondClass Current value = \n', self.name,  self.city, self.status)

#create instance of subclass
z =SecondClass()
z.setdata('tango','canada')
z.display()


# create subclass of subclass
class ThirdClass(SecondClass):
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status


a = ThirdClass('scott','boise','no')
a.display()  #call the display from SecondCalss


#usign classes
class Employees:
   def __init__(self,name,pay):  # init class with name and pay attributes
      self.name = name          # new object self 
      self.pay = pay
   
   def lastName(self):
      return self.name.split()[-1]  #return LN 
   
   def gieveRaise(self, percent):    # update pay
      self.pay *= (1.0 + percent)

sal=Employees('rose pet', 2000)
tan=Employees('tango gom', 3000)
salln=sal.lastName()
sal.gieveRaise(2.1)
print("sal lastName and pay = ", salln, sal.pay)
print("tan lastName and pay = ", tan.lastName(), tan.pay)


sys.exit(0)

