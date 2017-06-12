import unittest
from unittest.mock import MagicMock, Mock, patch
from translate2 import Translate,DBReader,TranslationObj
import json

class TranslateMockTest(unittest.TestCase):

  def test_get_authenticated(self):
    transAuth = DBReader()
    transAuth.setTranslateKey()
    testKey = transAuth.getTranslateKey()  
    self.assertEqual(testKey,"AIzaSy")

  @patch('translate2.Translate.getTranslation')
  def test_translate_pass(self,m_getTranslation):
    db1 = DBReader()
    db1.setTranslateKey()
    tweet1 = TranslationObj("I hope this works","zh-TW")
    translate1 = Translate(db1,tweet1)
    m_getTranslation.return_value = MagicMock(status_code=200,response_dict=json.dumps({'key':'value'}))
    a = translate1.getTranslation()
    print(a)
    

if __name__=="__main__":
    unittest.main()

