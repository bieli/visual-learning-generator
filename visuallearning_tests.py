import unittest

from visuallearning import *


class TestVisualLearning(unittest.TestCase):
    def test_should_gen_ascii_char(self):
        test_chars = ["a", "b", "c"]
        result = gen_ascii_char(chars=test_chars)
        self.assertTrue(result in test_chars)

    def test_should_gen_world_proper_length_of_word(self):
        min_chars = 1
        max_chars = 5
        result = gen_world(min_chars=min_chars, max_chars=max_chars)
        self.assertTrue(max_chars >= len(result) >= min_chars)

    def test_should_remove_duplicates_from_word(self):
        test_word_with_duplicats = "aaabbcw"
        expected_result = "abcw"
        result = remove_duplicates_from_word(test_word_with_duplicats)
        self.assertTrue("a" in result)
        self.assertTrue("b" in result)
        self.assertTrue("c" in result)
        self.assertTrue("w" in result)
        self.assertEqual(len(result), 4)

    def test_should_list_all_chars(self):
        expected_chars = "x y z"
        test_chars = ["x", "y", "z"]
        result = list_all_chars(chars=test_chars)
        self.assertEqual(result, expected_chars)

    def test_should_generate_words_with_alphabet_including_additional_random_words(self):
        template = "{}"
        min_words = 1
        max_words = 3
        min_chars = 1
        max_chars = 3
        test_alphabet = ["d", "e", "f"]
        result = generate_words_with_alphabet(template, min_words=min_words, max_words=max_words, min_chars=min_chars, max_chars=max_chars, alphabet=test_alphabet, verbose=False)
        self.assertTrue(len(result.split(' ')) >= 3)
        self.assertTrue(len(result.split(' ')) < 16)

    def test_should_generate_words_with_alphabet_including_proper_sequence(self):
        template = "{}"
        min_words = 1
        max_words = 2
        min_chars = 1
        max_chars = 2
        test_alphabet = ["a", "b", "c"]
        result = generate_words_with_alphabet(template, min_words=min_words, max_words=max_words, min_chars=min_chars, max_chars=max_chars, alphabet=test_alphabet, verbose=False)
        print(result)
        self._verify_alphabet_squence_in_genrated_words(test_alphabet, result)

    def _verify_alphabet_squence_in_genrated_words(self, alphabet, result):        
        alphabet_idx = 0
        alphabet_len = len(alphabet)

        print(alphabet, result)
        
        for word in result.split(" "):
          if -1 != word.find(alphabet[alphabet_idx]):
            del alphabet[alphabet_idx]

        self.assertTrue(alphabet == [], f"Not found letter(s) '{alphabet}' in words" )


if __name__ == "__main__":
    unittest.main()

