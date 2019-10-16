###############################################################
# unittes assert 
# nose doctest py mock
# test support package
# flask testing
###############################################################

from timeit import timeit

t1= timeit('7. ** i', setup='i = 5')
t2= timeit('pow(7., i)', setup='i = 5')
t3= timeit('math.pow(7, i)', setup='import math; i = 5')

print( t1, t2, t3)

# try
try:
   f = open("demofile.txt")
   f.write("Lorum Ipsum")
   print(f)
except NameError:
   print("nameerror")
except:
   print("Something else went wrong")
else:
   print("Nothing went wrong")
finally:
   f.close()
	

#unittest assert
import unittest
def fun(x):
   return x + 1
class MyTest(unittest.TestCase):
   def test(self):
      self.assertEqual(fun(3), 4)

#unittest assertEqual
class TestSum(unittest.TestCase):
   def test_sum(self):
      self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
   def test_sum_tuple(self):
      self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
if __name__ == '__main__':
unittest.main()

#Sample sort list sortTest.py
import unittest
import sys
	
sys.path.append('/home/salsa/scripts/sortSample.sikuli')
from sortlist import SortList
	
def is_sorted(expRes):
	    """Return True if l is sorted"""
	    a = [13, 4, 8, 1, 1, 18]
	    b = [10, 5, 7, 1, 4, 19, 1]
	    sortRes = SortList(a, b)
	    resSort = sortRes.sort_list()
	    print "Comparing result: ", resSort, " = ", expRes
	    if expRes == resSort:
	        return True
	    else:
	        return False
	
	class SortedCases(unittest.TestCase):
	
	    def test_is_sorted(self):
	        #expected result
	        expRes = [1, 4, 5, 7, 8, 10, 13, 18, 19]
	        # expRes = [5, 4, 5, 7, 8, 10, 13, 18, 19]
	        self.assertTrue(is_sorted(expRes))
	
	    def is_merged(self):
	        """Return True if ml includes l1 and l2"""
	        mRes = [1, 4, 5, 7, 8, 10, 13, 18, 19]
	        self.assertEqual(mRes, mRes)
	
if __name__ == '__main__':
   # to run a simple run: unittest.main()
   # to run suite
   suite = unittest.TestLoader().loadTestsFromTestCase(SortedCases)
   unittest.TextTestRunner(verbosity=2).run(suite)

# sort list 2
import sys
	
class SortList():
     # merge, sort, remove dups from 2 lists
     def __init__(self, a, b):
	        self.list1 = a
	        self.list2 = b
	
     def sort_list(self):
	        listM = self.list1 + self.list2
	        return list(set(listM))
	
     def sort_slist(self, list1, list2):
	        self.list1.extend(list2)
	        self.list1.sort()
	        return self.list1
	
def main():
     a = [13, 4, 8, 1, 1, 18]
     b = [10, 5, 7, 1, 4, 19, 1]
     sortRes = SortList(a, b)
     listSorted = sortRes.sort_list()
     # print "list: ", sortRes.list1, sortRes.list2, "Sorted =", listSorted
     return listSorted
	
if __name__ == "__main__":
   sys.exit(main())
	
#unittest samples
	#!/usr/bin/python3
	#unit test
	
	import unittest
	
	def is_fiveMulp(number):
	    """Return True if *number* is fiveMulp."""
	    for element in range(number):
	       if number % 5 == 0:
	          return True
	       return False
	
	def is_fiveCount(number):
	    """Return True if *number* is 5"""
	    if number == 5:
	       return True
	    return False
	
	class FiveTestCase(unittest.TestCase):
	    def test_is_fiveMulp(self):
	        """Is 10 successfully determined to be 5number?"""
	        self.assertTrue(is_fiveMulp(10))
	
	class CountFiveTestCase(unittest.TestCase):
	    def test_is_countFives(self):
	        """Is 5 successfully determined to be number of multiple of fives ?"""
	        self.assertTrue(is_fiveCount(5))
	
	if __name__ == '__main__':
	    unittest.main()



	Sample 2: suites
	
	mport unittest
	import sys
	
	n1=1
	n2=5
	narg=len(sys.argv)
	if narg < 2:
	    print("Error Invalid number of parameters %d " % narg)
	    sys.exit(1)
	s1=sys.argv[1] or 'foo'
	
	class TestStringMethods(unittest.TestCase):
	
	    def test_suma(self):
	        self.assertEqual(n1 + n2, 6)
	
	
	    def test_upper(self):
	        self.assertEqual(s1.upper(), 'FOO')
	
	    def test_isupper(self):
	        self.assertTrue('FOO'.isupper())
	        self.assertFalse('Foo'.isupper())
	
	    def test_split(self):
	        s1='hola salsa'
	        self.assertEqual(s1.split(), ['hola', 'salsa'])
	        with self.assertRaises(TypeError):
	            s1.split(2)
	
	
	if __name__ == '__main__':
	    # simple run => unittest.main()
	    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
	    unittest.TextTestRunner(verbosity=2).run(suite)



	Sample 4: unittest sample fib
	
	import unittest
	import sys
	
	""" Fibonnaci number """
	
	def fib(n):
	    a,b = 0,1
	    for i in range(n):
	        a,b = b, a+b
	    return a
	
	def fiblist(n):
	    fib = [0,1]
	    for i in range(1,n):
	        fib += [fib[-1]+fib[-2]]
	    return fib
	
	
	"""
	if __name__ == '__main__':
	    fibn=fib(numero)
	    fibl=fiblist(numero)
	    print("fibn =  %d  " % fibn)
	    print("fibl =  %s  " % fibl)
	"""
	

	Sample 4a: unittest
	
	# test unittest
	import unittest
	from fibonacci import fib
	import sys
	
	class FibonacciTest(unittest.TestCase):
	
	    def testCalculation(self):
	        self.assertEqual(fib(0), 0)
	        self.assertEqual(fib(1), 1)
	        self.assertEqual(fib(5), 5)
	        self.assertEqual(fib(10), 5)
	
	if __name__ == '__main__':
	    unittest.main()
	

	Sample 4b: unittest
	
	# unit test and tearDown
	  
	import unittest
	from fibonacci import fib
	import sys
	
	class FibonacciTest(unittest.TestCase):
	
	    # hook method for setting up the test fixture
	    def setUp(self):
	        self.fib_elems = ( (0,0), (1,1), (5,5), (10,55) )
	        print ("setup executed")
	
	    def testCalculation(self):
	        for (i,val) in self.fib_elems:
	            self.assertEqual(fib(i), val)
	
	    def testCalculation2(self):
	        for (i,val) in self.fib_elems:
	            self.assertEqual(fib(i), val)
	
	    # hook method for descontructing the class fixture after run test
	    def tearDown(self):
	        self.fib_elems = None
	        print ("tearDown executed")
	
	if __name__ == '__main__':
	    unittest.main()


	Sample UnitTest for Arrays
	#!/usr/bin/python3
	#unit test
	
	import unittest
	
	def is_fiveMulp(number):
	    """Return True if *number* is fiveMulp."""
	    for element in range(number):
	       if number % 5 == 0:
	          return True
	       return False
	
	def is_fiveCount(number):
	    """Return True if *number* is 5"""
	    if number == 5:
	       return True
	    return False
	
	class FiveTestCase(unittest.TestCase):
	    def test_is_fiveMulp(self):
	        """Is 10 successfully determined to be 5number?"""
	        self.assertTrue(is_fiveMulp(10))
	
	class CountFiveTestCase(unittest.TestCase):
	    def test_is_countFives(self):
	        """Is 5 successfully determined to be number of multiple of fives ?"""
	        self.assertTrue(is_fiveCount(5))
	
	if __name__ == '__main__':
	    unittest.main()

	Sample Test Power of 2 results:
	Module script
	$ cat power2.py
	#!/usr/bin/python
	
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
	
	#print "2 =>"
	#powerResult=power2()
	#print(powerResult)
	
	Unit test script:
	└─ $ ▶ cat power2test.py
	#!/usr/bin/python
	import unittest
	import sys
	sys.path.append('/home/salsa/myrepo/Scripts')
	from power2 import power2
	
	def is_power2():
	    #expected result
	    expRes = ['1 sum = 1', '2 sum = 3', '4 sum = 7', '8 sum = 15', '16 sum = 31', '32 sum = 63', '64 sum = 127', '128 sum = 255', '256 sum = 511']
	    powerRes = power2()
	    print "Comparing result: ", powerRes, " = ", expRes
	    if expRes == powerRes:
	        return True
	    else:
	        return False
	
	class PowerCases(unittest.TestCase):
	
	    def test_power(self):
	        self.assertTrue(is_power2())
	
	if __name__ == '__main__':
	    # to run a simple run: unittest.main()
	    # to run suite
	    suite = unittest.TestLoader().loadTestsFromTestCase(PowerCases)
	    unittest.TextTestRunner(verbosity=2).run(suite)



# Nose
	def my_setup_function():
	    global a
	    print("teardown")
	    a=3
	    pass
	
	def my_teardown_function():
	    print("teardown")
	    pass
	
	def test_numbers_3_4():
	    print("test_numbers")
	    assert a*4 == 12
	
	a=1
	# same as @with_setup(my_setup_function, my_teardown_function)
	test_numbers_3_4.setup = my_setup_function
	test_numbers_3_4.teardown = my_teardown_function
	

#nose.tools.assert_equals:
	from nose.tools import assert_equals

	def run_foo(x):
	    print(x)
	    pass
	
	def test_numbers_3_4():
	    print("test_numbers")
	    assert_equals(run_foo('testfoo'),'testfoo')
	
#doctest
	Sample 1: doctest
	
	import doctest
	import sys
	
	
	def fib(n):
	    """
	    test fibonacci number iterativale
	
	    >>> fib(0)
	    0
	    >>> fib(1)
	    1
	    >>> fib(10)
	    55
	    >>> fib(15)
	    610
	    >>>
	
	    """
	    #success a,b = 0,1
	    a,b = 1,1
	    for i in range(n):
	        a,b = b, a+b
	    return a
	
	if __name__ == '__main__':
	    doctest.testmod()
	
	
	Sample 2: doctest
	
	import doctest
	import sys
	
	# TDD test Driven Development - testing code hasnot been writen
	
	
	def fib(n):
	    """
	    test fibonacci number iterativale
	
	    >>> fib(0)
	    0
	    >>> fib(1)
	    1
	    >>> fib(10)
	    55
	    >>> fib(15)
	    610
	    >>>
	
	    """
	
	    return 0
	
	if __name__ == '__main__':
	    doctest.testmod()

#py.test
# content of test_sample.py
def func(x):
    return x + 1
	def test_answer():
    assert func(3) == 5
	and then running the py.test command
$ py.test

#mock
def mock_search(self):
    class MockSearchQuerySet(SearchQuerySet):
        def __iter__(self):
            return iter(["foo", "bar", "baz"])
    return MockSearchQuerySet()
# SearchForm here refers to the imported class reference in myapp,
# not where the SearchForm class itself is imported from
@mock.patch('myapp.SearchForm.search', mock_search)
def test_new_watchlist_activities(self):
   # get_search_results runs a search and iterates over the result
   self.assertEqual(len(myapp.get_search_results(q="fish")), 3)


#test support package
import unittest
from test import support
	class MyTestCase1(unittest.TestCase):
	# Only use setUp() and tearDown() if necessary
	def setUp(self):
        ... code to execute in preparation for tests ...
	def tearDown(self):
        ... code to execute to clean up after tests ...
	def test_feature_one(self):
        # Test feature one.
        ... testing code ...
	def test_feature_two(self):
        # Test feature two.
        ... testing code ...
	... more test methods ...
	class MyTestCase2(unittest.TestCase):
    ... same structure as MyTestCase1 ...
	... more test classes ...
	def test_main():
    support.run_unittest(MyTestCase1,
                         MyTestCase2,
                         ... list other tests ...
                         )
	if __name__ == '__main__':
    test_main()


# test flask
import my_app
import unittest
class MyTestCase(unittest.TestCase):
   def setUp(self):
      my_app.app.testing = True
      self.app = my_app.app.test_client()
   def test_home(self):
      result = self.app.get('/')
      # Make your assertions


