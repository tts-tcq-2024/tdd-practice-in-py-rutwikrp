import unittest
from StringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(StringCalculator.add(""), 0)
    
    def test_single_number(self):
        self.assertEqual(StringCalculator.add("1"), 1)
    
    def test_two_numbers(self):
        self.assertEqual(StringCalculator.add("1,2"), 3)
    
    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator.add("1,2,3,4,5"), 15)
    
    def test_newline_delimiter(self):
        self.assertEqual(StringCalculator.add("1\n2,3"), 6)
    
    def test_custom_delimiter(self):
        self.assertEqual(StringCalculator.add("//;\n1;2"), 3)
    
    def test_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            StringCalculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "Negatives not allowed: -2")
    
    def test_ignore_large_numbers(self):
        self.assertEqual(StringCalculator.add("2,1001"), 2)
    
    def test_any_length_delimiter(self):
        self.assertEqual(StringCalculator.add("//[***]\n1***2***3"), 6)

if __name__ == '__main__':
    unittest.main()
