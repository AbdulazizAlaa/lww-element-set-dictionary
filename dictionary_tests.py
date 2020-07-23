import unittest
from lww_element_dictionary import Dictionary
from datetime import date


class Test_Dictionary_LWW_Element_Set(unittest.TestCase):

    def test_simple_add_remove(self):
        word_dict: Dictionary = Dictionary()
        a: str = "play"
        b: str = "ball"
        word_dict.add(a, date(2020, 1, 5))
        self.assertTrue(word_dict.checkExists(a))
        self.assertFalse(word_dict.checkExists(b))
        word_dict.add(b, date(2020, 1, 5))
        word_dict.remove(a, date(2020, 1, 6))
        self.assertTrue(word_dict.checkExists(b))
        self.assertFalse(word_dict.checkExists(a))
        expected_arr: list = [b, ]
        self.assertEqual(word_dict.get(), expected_arr)

    def test_add_remove_multiple_words_in_reverse_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "play"
        b: str = "football"
        c: str = "tennis"
        word_dict.remove(a, date(2020, 1, 6))
        word_dict.remove(c, date(2020, 1, 6))
        self.assertFalse(word_dict.checkExists(a))
        self.assertFalse(word_dict.checkExists(c))
        word_dict.add(a, date(2020, 1, 5))
        word_dict.add(c, date(2020, 1, 5))
        self.assertFalse(word_dict.checkExists(a))
        self.assertFalse(word_dict.checkExists(c))
        word_dict.add(b, date(2020, 1, 5))
        word_dict.add(b, date(2020, 1, 7))
        self.assertTrue(word_dict.checkExists(b))
        word_dict.add(a, date(2020, 1, 7))
        self.assertTrue(word_dict.checkExists(a))
        expected_arr: list = [a, b, ]
        self.assertEqual(word_dict.get(), expected_arr)

    def test_add_same_word_with_newer_date_in_reverse_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "boy"
        word_dict.add(a, date(2020, 1, 5))
        self.assertTrue(word_dict.checkExists(a))
        word_dict.add(a, date(2020, 1, 4))
        self.assertTrue(word_dict.checkExists(a))
        expected_arr: list = [a, ]
        self.assertEqual(word_dict.get(), expected_arr)

    def test_add_same_word_with_same_date(self):
        word_dict: Dictionary = Dictionary()
        a: str = "Girls"
        word_dict.add(a, date(2020, 10, 14))
        self.assertTrue(word_dict.checkExists(a))
        word_dict.add(a, date(2020, 10, 14))
        self.assertTrue(word_dict.checkExists(a))
        expected_arr: list = [a, ]
        self.assertEqual(word_dict.get(), expected_arr)

    def test_add_same_word_with_newer_date_in_correct_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "Girls"
        word_dict.add(a, date(2020, 7, 14))
        self.assertTrue(word_dict.checkExists(a))
        word_dict.add(a, date(2020, 10, 14))
        self.assertTrue(word_dict.checkExists(a))
        expected_arr: list = [a, ]
        self.assertEqual(word_dict.get(), expected_arr)

    def test_remove_word_after_add_in_reverse_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "earth"
        word_dict.remove(a, date(2020, 10, 14))
        self.assertFalse(word_dict.checkExists(a))
        word_dict.add(a, date(2020, 10, 12))
        self.assertFalse(word_dict.checkExists(a))
        expected_arr: list = []
        self.assertEqual(word_dict.get(), expected_arr)

    def test_remove_add_word_at_same_date_in_reverse_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "sea"
        word_dict.remove(a, date(2020, 10, 12))
        self.assertFalse(word_dict.checkExists(a))
        word_dict.add(a, date(2020, 10, 12))
        self.assertTrue(word_dict.checkExists(a))
        expected_arr: list = [a, ]
        self.assertEqual(word_dict.get(), expected_arr)

    def test_remove_word_before_add_in_correct_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "waves"
        word_dict.remove(a, date(2020, 10, 12))
        self.assertFalse(word_dict.checkExists(a))
        word_dict.add(a, date(2020, 10, 15))
        self.assertTrue(word_dict.checkExists(a))
        expected_arr: list = [a, ]
        self.assertEqual(word_dict.get(), expected_arr)

    def test_remove_word_twice_in_reverse_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "waves"
        word_dict.remove(a, date(2020, 10, 12))
        self.assertFalse(word_dict.checkExists(a))
        word_dict.remove(a, date(2020, 10, 1))
        self.assertFalse(word_dict.checkExists(a))
        expected_arr: list = []
        self.assertEqual(word_dict.get(), expected_arr)

    def test_remove_word_twice_at_same_date(self):
        word_dict: Dictionary = Dictionary()
        a: str = "tea"
        word_dict.remove(a, date(2020, 10, 12))
        self.assertFalse(word_dict.checkExists(a))
        word_dict.remove(a, date(2020, 10, 12))
        self.assertFalse(word_dict.checkExists(a))
        expected_arr: list = []
        self.assertEqual(word_dict.get(), expected_arr)

    def test_remove_word_twice_in_correct_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "cup"
        word_dict.remove(a, date(2020, 10, 12))
        self.assertFalse(word_dict.checkExists(a))
        word_dict.remove(a, date(2020, 10, 16))
        self.assertFalse(word_dict.checkExists(a))
        expected_arr: list = []
        self.assertEqual(word_dict.get(), expected_arr)

    def test_remove_word_before_add_in_reverse_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "blue"
        word_dict.add(a, date(2020, 10, 12))
        self.assertTrue(word_dict.checkExists(a))
        word_dict.remove(a, date(2020, 10, 1))
        self.assertTrue(word_dict.checkExists(a))
        expected_arr: list = [a, ]
        self.assertEqual(word_dict.get(), expected_arr)

    def test_remove_add_word_at_same_date_in_correct_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "green"
        word_dict.add(a, date(2020, 10, 12))
        self.assertTrue(word_dict.checkExists(a))
        word_dict.remove(a, date(2020, 10, 12))
        self.assertTrue(word_dict.checkExists(a))
        expected_arr: list = [a, ]
        self.assertEqual(word_dict.get(), expected_arr)

    def test_add_word_before_remove_in_correct_order(self):
        word_dict: Dictionary = Dictionary()
        a: str = "hookah"
        word_dict.add(a, date(2020, 10, 12))
        self.assertTrue(word_dict.checkExists(a))
        word_dict.remove(a, date(2020, 10, 17))
        self.assertFalse(word_dict.checkExists(a))
        expected_arr: list = []
        self.assertEqual(word_dict.get(), expected_arr)


if __name__ == '__main__':
    unittest.main()
