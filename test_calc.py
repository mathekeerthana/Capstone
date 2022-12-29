import calc     # Here we import only functions

import unittest

class testcalc(unittest.TestCase):

    def testadd(self):
        #self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(12,5),7)
        #self.assert

    def test_sub(self):
        #self.assertEqual(calc.sub(4,1),3)
        self.assertNotEqual(calc.sub(1,2),3)




if __name__=="__main__":
    unittest.main(verbosity=2)
