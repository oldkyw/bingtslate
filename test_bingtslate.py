import unittest
import bingtslate

class TestBingtslate(unittest.TestCase):

    def test_translate_text(self):
        
        self.assertFalse('error' in bingtslate.translate_text('dobra pogoda'))
        
if __name__ == '__main__':
    unittest.main()
