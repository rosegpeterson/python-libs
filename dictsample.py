
myText="""This is a test to initaliza a dictionary"""
words = myText.split()

# 1
d = {}.fromkeys(words,0)
for w in words:
    d[w] += 1
print '1. ',  d

# 2
d = {}
for w in words:
    d[w] = d.get(w,0) + 1
print '2. ',  d


# 3
from collections import defaultdict
d = defaultdict(int)
for w in words:
    d[w] += 1
print '3. ',  d

# construct dictionary whose values are lists.
cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}
# => {'US':['San Francisco', 'Los Angeles'], 'UK':[,], ...}

from collections import defaultdict

print "using collections.defaultdict()"
d1 = defaultdict(list) # initialize dict with list
for k,v in cities.items():
    d1[v].append(k)
print d1

print "using dict.setdefault(key, default=None)"
d2 = {}
for k,v in cities.items():
       d2.setdefault(v,[]).append(k)
print d2
