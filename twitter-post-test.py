#python3
from mock import MagicMock, Mock, patch
import unittest
import json
import twitterPost

class TwitterPostTestMock (unittest.TestCase) :

    @patch('dbConnect.connect_to_DB.sqlite_retrieve')
    @patch('tweepy.API.update_status')
    def test_twitter_post_success(self,m_update_status, m_sql_retrieve):
          #print out arguments passed for clarity sake
          print(locals())
          m_sql_retrieve.return_value = MagicMock()
          #set data type and content of Magic Mock reponse
          m_sql_retrieve.__dir__ = ({
                "consumer_key"        : "rcIlpeAhFKSXlzhjnWqfkS9x7",
                "consumer_secret"     : "J96cwUhHWX93TvSxO7nBpmnqz8LCGuJLNQVFWKehg1bFQRysQe",
                "access_token"        : "838080768408612868-sLc6Uo8iAbdHrJTeEd5C2pjskaitgq6",
                "access_token_secret" : "r1lj2ZT20H0aACoxqZdIHNq6nfBoWtCNwZNFrvAB6JOMn"
                })
          m_update_status.return_value = MagicMock()
          #calling the function to be tested
          twitterPost.TwitterPost().twitter_post('I am a tweet message','spanish')
          m_update_status.assert_called_with(status='I am a tweet message')
          #checks if api.call_api is called with the right token, 'spnaish' this case
          m_sql_retrieve.assert_called_with('spanish')



    @patch('dbConnect.connect_to_DB.sqlite_retrieve')
    @patch('tweepy.API.update_status')
    def test_twitter_post_failed(self, m_update_status, m_sql_retrieve):
        print(locals())
        m_sql_retrieve.return_value = MagicMock()
        m_update_status.side_effect =Exception('Twitter post failed')
        with self.assertRaises(Exception):
            twitterPost.TwitterPost().twitter_post('I am a tweet message', 'spanish')


if __name__ == ' __main__ ':
    unittest.main()
