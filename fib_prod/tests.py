from solution import fib_prod
import codewars_test as test


@test.describe("Fibonacci's Product")
def tests():
    @test.it("Corner cases. Examples for small n.")
    def samples():
        test.assert_equals(fib_prod(2), 1)
        test.assert_equals(fib_prod(3), 1)
        test.assert_equals(fib_prod(4), 1)
        test.assert_equals(fib_prod(5), 1)
        test.assert_equals(fib_prod(6), 1)
        test.assert_equals(fib_prod(7), 0)
        test.assert_equals(fib_prod(8), 2)
        test.assert_equals(fib_prod(9), 1)
        test.assert_equals(fib_prod(10), 1)
        