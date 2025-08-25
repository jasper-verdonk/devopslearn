import my_script
import unittest

# inhereting the TestCase class from the unittest library. 
class TestUpperAdd(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = my_script.cap_upper(text)
        self.assertEqual(result, 'PYTHON')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = my_script.cap_upper(text)
        self.assertEqual(result, 'MONTY PYTHON')
        
    def test_adder(self):
        x = 5
        y = 10
        result = my_script.adder(x, y)
        self.assertEqual(result, 15)
if __name__ == '__main__':
    unittest.main()