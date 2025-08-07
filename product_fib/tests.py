import codewars_test as test
try:
    from solution import productFib as product_fib
except:
    from solution import product_fib

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(product_fib(4895), [55, 89, True])
        test.assert_equals(product_fib(5895), [89, 144, False])