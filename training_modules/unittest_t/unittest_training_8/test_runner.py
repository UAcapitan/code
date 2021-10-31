import unittest
import test_1

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(test_1)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suites)