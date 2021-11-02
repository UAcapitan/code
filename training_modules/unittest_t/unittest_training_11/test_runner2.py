import unittest
import test2

t = unittest.TestSuite()
t.addTest(unittest.makeSuite(test2.CalcTests))
t.addTest(unittest.makeSuite(test2.OtherCalcTests))
runner = unittest.TextTestRunner(verbosity=2)
test_result = runner.run(t)

print('Errors:')
print(len(test_result.errors))
print('Failures:')
print(len(test_result.failures))
print('Skipped:')
print(len(test_result.skipped))
print('Tests run:')
print(test_result.testsRun)

