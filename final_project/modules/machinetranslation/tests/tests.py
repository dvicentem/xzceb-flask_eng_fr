import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    ENGLISH_TEXT = 'Hello.'
    FRENCH_TEXT = 'Bonjour.'
    def test_french_to_english(self):
        self.assertEqual(english_to_french(self.ENGLISH_TEXT), self.FRENCH_TEXT)
    def test_english_to_french(self):
        self.assertEqual(french_to_english(self.FRENCH_TEXT), self.ENGLISH_TEXT)

if __name__ == '__main__':
    unittest.main()