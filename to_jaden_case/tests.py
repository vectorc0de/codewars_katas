from solution import to_jaden_case
import codewars_test as test

@test.describe('Sample test')
def basic_tests():
    @test.it('Simple text')
    def _():
        quote = "How can mirrors be real if our eyes aren't real"
        result = to_jaden_case(quote)
        expect = "How Can Mirrors Be Real If Our Eyes Aren't Real"
        test.assert_equals(result, expect)