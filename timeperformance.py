from timeit import timeit

t1= timeit('7. ** i', setup='i = 5')
t2= timeit('pow(7., i)', setup='i = 5')
t3= timeit('math.pow(7, i)', setup='import math; i = 5')

print( t1, t2, t3)
