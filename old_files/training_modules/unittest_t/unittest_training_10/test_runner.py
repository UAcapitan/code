import unittest
import test_1

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(test_1.CalcBasicTests))
calcTestSuite.addTest(unittest.makeSuite(test_1.CalcExTests))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)