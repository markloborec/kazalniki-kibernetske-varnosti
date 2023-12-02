import unittest

from calsec import func, vec


class TestStringMethods(unittest.TestCase):
    def test_multi(self):
        returned = vec.multi(v1 = [1,2,3], v2 = [4,5,6])
        self.assertEqual(returned, [4,10,18])

    def test_skal_multi(self):
        returned = vec.skal_multi(v1=[3, -2, 6],s= 5)
        self.assertEqual(returned, [15, -10, 30])


if __name__ == '__main__':
    unittest.main()