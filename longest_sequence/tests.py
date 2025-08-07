import codewars_test as test
from solution import longest_consec

@test.describe("Fixed Tests")
test.it('should pass all basic test')

l = [(41, {4,5}), (50, {3,4,5}), (595, {6, 7, 8, 9, 10, 11, 12})]

for n, soln in l:
  test.assert_equals(set(longest_sequence(n)), soln, 'Wrong! ')