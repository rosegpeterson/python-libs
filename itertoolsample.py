import sys
from itertools import izip
from itertools import izip_longest

#https://docs.python.org/2/library/itertools.html

fileName1="test1"
fileName2="test2"

# itertools 
# izip() -> p, q, =>(p[0], q[0]), (p[1], q[1]),
# izip('ABCD', 'xy') --> Ax By
# izip_longest() -> p, q, ->(p[0], q[0]), (p[1], q[1]),…
# izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
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

#Main
try:
    file1 = open(fileName1, 'r')
    file2 = open(fileName2, 'r')
    print('Printing content of files')
    read_file(file1,file2,1,1)
    file1.close()
    file2.close()
except IOError:
    print ("Error opening file(s)", fileName1, fileName2)
    sys.exit(1)

print('Printing content of files - zip option')
read_zip(fileName1,fileName2)
sys.exit(0)


