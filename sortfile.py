import sys

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


#sort <file name> | uniq

#from list
GoT = ['Tony', 'Rocket', 'Scott', 'Steve', 'Rocket', 'Natasha', 'Tony']
mylist = sorted(list(dict.fromkeys(GoT)), reverse=True)
print(mylist)
