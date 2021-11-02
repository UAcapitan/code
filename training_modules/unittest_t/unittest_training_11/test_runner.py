import unittest
import test

t = unittest.TestLoader()
suites = t.loadTestsFromModule(test)
runner = unittest.TextTestRunner(verbosity=2)
test_result = runner.run(suites)

print('Errors:')
print(len(test_result.errors))
print('Failures:')
print(len(test_result.failures))
print('Skipped:')
print(len(test_result.skipped))
print('Tests run:')
print(test_result.testsRun)

