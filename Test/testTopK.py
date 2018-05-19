# -*- coding: utf-8 -*-
# __Author__: Sdite, amyy4, JX-Soleil, hzgege
# __Email__ : a122691411@gmail.com

import unittest

import sys
sys.path.append('../')
import findTopK

class TestTopK(unittest.TestCase):
    testList1 = [1]
    testList2 = [1, 3, 5, 6, 8, 99, 434, 0, -5, -9, -10]
    testList3 = [1, 1, 1, 1, 1]

    def testQSelect(self):
        self.assertEqual(sorted(findTopK.qSelect(self.testList1, 1)), [1])
        self.assertEqual(sorted(findTopK.qSelect(self.testList2, 5)), [-10, -9, -5, 0, 1])
        self.assertEqual(sorted(findTopK.qSelect(self.testList3, 3)), [1, 1, 1])

    def testTopKHeapq(self):
        self.assertEqual(sorted(findTopK.topKHeap(self.testList1, 1)), [1])
        self.assertEqual(sorted(findTopK.topKHeap(self.testList2, 5)), [-10, -9, -5, 0, 1])
        self.assertEqual(sorted(findTopK.topKHeap(self.testList3, 3)), [1, 1, 1])

if __name__ == '__main__':
    unittest.main()



