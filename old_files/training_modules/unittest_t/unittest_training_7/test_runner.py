import unittest
import test_1

testCases = []
testCases.append(test_1.CalcBasicTests)
testCases.append(test_1.CalcExTests)
testLoad = unittest.TestLoader()

suites = []
for tc in testCases:
    suites.append(testLoad.loadTestsFromTestCase(tc))

res_suite = unittest.TestSuite(suites)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)