#!/usr/bin/python
import math

def power1():
    print "1 =>"
    for i in range(0, 8):
        sum = 0
        power = 0
        print 2 ** power
        sum = 2 ** power
        print sum

def power2():
    sum = 0
    resultado=[]
    for power in range(0, 9):
      sum += 2 ** power
      #print('Power ',   2 ** power, 'Sum', sum)
      #result=result + str(2 ** power) + " sum = " + str(sum) + "\n"
      resultado.append(str(2 ** power) + " sum = " + str(sum))
    return resultado
    
def power3():
    print "3 =>"
    print([1<<exponent for exponent in range(9)])

def power4():
    print "4 =>"
    sumtot=0
    for power in range(0, 9):
        x = int(math.pow(2,power)) # x = 2 to the power of 'power' var
        sumtot+=sum([x])
        print x , sumtot

def powerS():
    print math.pow(10, 2)
    print 10 ** 2


print "2 =>"
powerResult=power2()
print(powerResult)
power4()
powerResult=power2()
