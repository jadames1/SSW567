#Test Math Fuction Triangle Classifications
#By Jenelee Adames 

import unittest
import Triangles


class BuggyTriangleTest(unittest.TestCase):
    def test_init(self):
        """ Sides stored properly in _init_()"""
        t = BuggyTriangle(3,4,5)
        self.assertEqual (t.a,3)
        self.assertEqual (t.b,4)
        self.assertEqual (t,c,5)

    def test_right_triangle(self):
        """test right triangle detection"""
        t = BuggyTriangle(3,4,5)
        self.assertTrue (t.right_triangle())
        self.assertTrue (BuggyTriangle (5,4,3).right_triangle())
        self.assertFalse (BuggyTriangle (3,3,3). right_triangle())
        
if __name__=='__main__':
    unittest.main(exit=False, verbosity=2)
    