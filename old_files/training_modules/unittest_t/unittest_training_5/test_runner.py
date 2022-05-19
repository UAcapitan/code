import unittest
import test_1

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(test_1.CalcTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)