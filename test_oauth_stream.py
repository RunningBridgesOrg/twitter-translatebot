from unittest.mock import MagicMock, patch
import json
import oauth_stream
import unittest

@patch('tweepy.Stream')
@patch('tweepy.OAuthHandler')
def test_json_func(m_tweepy_OAuthHandler,m_tweepy_stream):
	# print(locals())
	# m_tweepy_stream.return_value = MagicMock()
	# m_tweepy_stream.__dir__ = ({"text": "cab"})
	# oauth_stream.TwitterListener().main()
	#assert oauth_stream.TwitterListener().main() == 2345 # use a valid id

	m_tweepy_OAuthHandler.return_value = MagicMock()
	m_tweepy_OAuthHandler.assert_called_once_with('***REMOVED***','***REMOVED***')


test_json_func()
