from solution import is_pangram
import codewars_test as test


@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Test pangrams")
    def test_pangrams():
        pangrams = ["The quick brown fox jumps over the lazy dog.",
                    "Cwm fjord bank glyphs vext quiz",
                    "Pack my box with five dozen liquor jugs.",
                    "How quickly daft jumping zebras vex.",
                    "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"]
        for pangram in pangrams:
            test.assert_equals(is_pangram(pangram), True, f"Incorrect answer for '{pangram}'")

    @test.it("Test non-pangrams")
    def test_non_pangrams():
        non_pangrams = ["This isn't a pangram!",
                        "abcdefghijklm opqrstuvwxyz",
                        "Aacdefghijklmnopqrstuvwxyz"]
        for non_pangram in non_pangrams:
            test.assert_equals(is_pangram(non_pangram), False, f"Incorrect answer for '{non_pangram}'")