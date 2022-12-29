import unittest
from translator import frenchtoEnglish, englishtoFrench

class TestTranslations(unittest.TestCase):

    def test_translateNull1(self):
        self.assertEqual(frenchtoEnglish(''), None)

    def test_translateNull2(self):
        self.assertEqual(englishtoFrench(''), None)

    def test_translateEF(self):
        self.assertEqual(englishtoFrench('Hello'), 'Bonjour')

    def test_translateFE(self):
        self.assertEqual(frenchtoEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()