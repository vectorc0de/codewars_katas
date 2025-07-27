import codewars_test as test
from solution import longest_consec

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        test.assert_equals(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        test.assert_equals(longest_consec([], 3), "")
        test.assert_equals(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        test.assert_equals(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        test.assert_equals(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        test.assert_equals(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        test.assert_equals(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        test.assert_equals(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")