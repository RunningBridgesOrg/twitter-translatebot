import unittest
import translate

class TranslateTestCase(unittest.TestCase):
    """Tests for translate.py"""

    def test_get_authenticated(self):
        self.assertTrue("AIzaSyDeUDquCmTS1zxmQGj8dChbLAUyyYXkIXE" == translate.get_authenticated("apiKey.txt"))
    
    def test_no_file(self):
        self.assertTrue(translate.get_authenticated("api.txt") == None)
    
    def test_no_apiKey_in_file(self):
        self.assertTrue(translate.get_authenticated("apiKey_emptyKey.txt") == "")

    def test_invalid_apiKey(self):
        self.assertFalse(translate.get_authenticated("apiKey_wrongKey.txt") == None)

if __name__ == '__main__':
    #unittest.main() 
    suite = unittest.TestLoader().loadTestsFromTestCase(TranslateTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
