import unittest
import test_1

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(test_1.CalcBasicTests))
calcTestSuite.addTest(unittest.makeSuite(test_1.CalcExTests))
print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)