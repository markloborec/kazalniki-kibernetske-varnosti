import datetime
import unittest

from calsec import func
import calsec

class Test_SPS(unittest.TestCase):
    def test_1(self):
        returned = func.SPS(
            Tmeasure=[10,10,10],
            Wmesaure =[10,10,10],
            ResultMTBI=1,
        )
        self.assertEqual(returned,1)

    def test_2(self):
        returned = func.SPS(
            Tmeasure=[1,1,1],
            Wmesaure =[10,10,10],
            ResultMTBI=1,
        )
        self.assertEqual(round(returned,9),0.129032258)
    def test_3(self):
        returned = func.SPS(
            Tmeasure=[10,10,10],
            Wmesaure =[40,40,40],
            ResultMTBI=1,
        )
        self.assertEqual(returned,1)

class Test_TNPPS(unittest.TestCase):
    def test_1(self):
        returned = func.TNPPS(
            Resultmeasure = [
            func.TNPPS_OLMCME([1 for i in range(12)]),
            func.TNPPS_OLMCMU([1 for i in range(12)]),
            func.TNPPS_OLMCNP([1 for i in range(12)]),
            func.TNPPS_ONMAPS ([1 for i in range(12)])

        ],

            Wmeasure =[10,10,10,10],
            C=10,
        )
        self.assertEqual(returned,9.75)

class Test_TNPPS_OLMCME(unittest.TestCase):
    def test_1(self):
        returned = func.TNPPS_OLMCME(
            MEcounterm=[0]

        )
        self.assertEqual(returned,0)
    def test_2(self):
        returned = func.TNPPS_OLMCME(
            MEcounterm=[1,2,3,4,5,6,7,8,9,10,11,12]

        )
        self.assertEqual(returned,6.5)
    def test_3(self):
        returned = func.TNPPS_OLMCME(
            MEcounterm=[0]

        )
        self.assertEqual(returned,0)

class Test_TNPPS_OLMCMU(unittest.TestCase):
    def test_1(self):
        returned = func.TNPPS_OLMCMU(
            MUcounterm=[0]

        )
        self.assertEqual(returned,0)

    def test_2(self):
        returned = func.TNPPS_OLMCMU(
            MUcounterm=[1,2,3,4,5,6,7,8,9,10,11,12]

        )
        self.assertEqual(returned, 6.5)

    def test_3(self):
        returned = func.TNPPS_OLMCMU(
            MUcounterm=[3,4,5,6,7,8,9,10,4,5,2,6]


        )
        self.assertEqual(returned, 5.75)

class Test_TNPPS_OLMCNP(unittest.TestCase):
    def test_1(self):
        returned = func.TNPPS_OLMCNP(
            NPcounterm=[3,4,5,6,7,8,9,10,4,5,2,6]

        )
        self.assertEqual(returned, 5.75)
    def test_2(self):
        returned = func.TNPPS_OLMCNP(
            NPcounterm=[0]

        )
        self.assertEqual(returned, 0)
    def test_3(self):
        returned = func.TNPPS_OLMCNP(
            NPcounterm=[0]

        )
        self.assertEqual(returned, 0)

class Test_TNPPS_ONMAPS(unittest.TestCase):
    def test_1(self):
        returned = func.TNPPS_ONMAPS(
            MAPScounterm=[0]

        )
        self.assertEqual(returned, 1)
    def test_2(self):
        returned = func.TNPPS_ONMAPS(
            MAPScounterm=[10]

        )
        self.assertEqual(returned, 0)
    def test_3(self):
        returned = func.TNPPS_ONMAPS(
            MAPScounterm=[6,2]

        )
        self.assertEqual(round(returned,7), 0.600000)

class Test_TEPS(unittest.TestCase):
    def test_1(self):
        returned = func.TEPS(
            Resultmeasure = [
            func.TEPS_OLMCMW([1 for i in range(12)]),
            func.TEPS_OLMCMD_SD([1 for i in range(12)]),

        ],

            Wmeasure =[10,10],
            C=10,
        )
        self.assertEqual(returned,10)

    def test_2(self):
        returned = func.TNPPS(
            Resultmeasure = [
            func.TEPS_OLMCMW([1 for i in range(12)]),
            func.TEPS_OLMCMD_SD([1 for i in range(12)]),

        ],

            Wmeasure =[10,10],
            C=10,
        )
        self.assertEqual(returned,10)
class Test_TEPS_OLMCMW(unittest.TestCase):
    def test_1(self):
        returned = func.TEPS_OLMCMW(
            MWcounterm=[3,4,5,6,7,8,9,10,4,5,2,6]

        )
        self.assertEqual(returned, 5.75)

    def test_2(self):
        returned = func.TEPS_OLMCMW(
            MWcounterm=[3, 4, 5, 6, 7, 8, 9, 10, 4, 5, 2, 6]

        )
        self.assertEqual(returned, 5.75)

    def test_3(self):
        returned = func.TEPS_OLMCMW(
            MWcounterm=[3, 4, 5, 6, 7, 8, 9, 10, 4, 5, 2, 6]

        )
        self.assertEqual(returned, 5.75)

class Test_TEPS_OLMCMD_SD(unittest.TestCase):
    def test_1(self):
        returned = func.TEPS_OLMCMD_SD(
            MDSDcounterm=[3,4,5,6,7,8,9,10,4,5,2,6]

        )
        self.assertEqual(returned, 5.75)
    def test_2(self):
        returned = func.TEPS_OLMCMD_SD(
            MDSDcounterm=[3,4,5,6,7,8,9,10,4,5,2,6]

        )
        self.assertEqual(returned, 5.75)
    def test_3(self):
        returned = func.TEPS_OLMCMD_SD(
            MDSDcounterm=[3,4,5,6,7,8,9,10,4,5,2,6]

        )
        self.assertEqual(returned, 5.75)

class Test_THSS(unittest.TestCase):
    def test_1(self):
        returned = func.THSS(
            Resultmeasure = [
            func.THSS_OLMCSE([1 for i in range(12)]),
            func.THSS_OLMCHR([1 for i in range(12)]),

        ],

            Wmeasure =[10,10],
            C=10,
        )
class Test_THSS_OLMCSE(unittest.TestCase):
    def test_1(self):
        returned = func.THSS_OLMCSE(
            SEcounterm = [2,5,1,2,4,5,6],


        )
        self.assertEqual(returned,3.5714285714285716)
class Test_THSS_OLMCHR(unittest.TestCase):
    def test_1(self):
        returned = func.THSS_OLMCHR(
            HRcounterm = [2,4,5,6,2,1,2,3],

        )
        self.assertEqual(returned,3.125)
class Test_OIMBTI(unittest.TestCase):
    def test_1(self):
        returned = func.OIMTBI(
            I = [datetime.date(2023,12,2),datetime.date(2023,12,17), datetime.date(2024,1,2), datetime.date(2024,1,17), datetime.date(2024,2,2)],


        )
        self.assertEqual(returned,15.5)

if __name__ == '__main__':
    unittest.main()
