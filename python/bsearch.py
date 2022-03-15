import unittest
import random
from BitVector import BitVector
from bisect import insort

def bsearch(a, n):
  lo=0
  hi=len(a)-1

  while lo <= hi:
    mid = int((lo+hi)/2)
    if a[mid] == n:
      return mid
    if a[mid] < n:
      lo=mid+1
    else:
      hi=mid-1
  
  return -1

class BSearchTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.huge = []
    cls.hugelength = 1000000

    for _ in range(0, cls.hugelength):
      n = random.randint(0, 0x7F_FF_FF_FF)
      insort(cls.huge,n)

  def test_bsearch(self):
    a = [0,1,2,3,4,5,6,7]
    self.assertEqual(0, bsearch(a,0))
    self.assertEqual(1, bsearch(a,1))
    self.assertEqual(2, bsearch(a,2))
    self.assertEqual(3, bsearch(a,3))
    self.assertEqual(4, bsearch(a,4))
    self.assertEqual(5, bsearch(a,5))
    self.assertEqual(6, bsearch(a,6))
  
  def test_bsearch_2(self):
    a = [3,5,12,56,80,91,123]
    self.assertEqual(0, bsearch(a,3))
    self.assertEqual(1, bsearch(a,5))
    self.assertEqual(2, bsearch(a,12))
    self.assertEqual(3, bsearch(a,56))
    self.assertEqual(4, bsearch(a,80))
    self.assertEqual(5, bsearch(a,91))
    self.assertEqual(6, bsearch(a,123))

  def test_bsearch_huge_random_list(self):
    for _ in range(0, self.hugelength):
      idx = random.randint(0, self.hugelength-1)
      elem = self.huge[idx]
      found = bsearch(self.huge,elem)
      self.assertEqual(elem, self.huge[found])

  def test_negative_one_if_fails(self):
    a = [3,5,12,56,80,91,123]
    self.assertEqual(-1, bsearch(a,69))

if __name__ == "__main__":
  unittest.main()
