import unittest
import test3

classes = []
classes.append(test3.CalcTests)
classes.append(test3.OtherCalcTests)

t = unittest.TestLoader()

suites = []
for i in classes:
    suites.append(t.loadTestsFromTestCase(i))

res_suite = unittest.TestSuite(suites)
runner = unittest.TextTestRunner(verbosity=2)
test_result = runner.run(res_suite)

print('Errors:')
print(len(test_result.errors))
print('Failures:')
print(len(test_result.failures))
print('Skipped:')
print(len(test_result.skipped))
print('Tests run:')
print(test_result.testsRun)

