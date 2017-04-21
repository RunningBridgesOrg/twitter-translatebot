from unittest import mock
from unittest.mock import MagicMock, patch
from twitterListener import TwitterListener

from twitterListener import MyStreamListener
from MockStreamData import MockStreamData

import tweepy

def test_read_cfg_from_file():
    """Testing for read_cfg_from_file
    when supposed it is readfrom DB. Test for correct value"""

    ans_cfg = {'consumer_key' :'***REMOVED***'}
    testListener = TwitterListener()
    my_cfg = testListener.read_cfg_from_DB

    assert ans_cfg == my_cfg


def test_get_authenticated():

    tweepy.OAuthHandler = mock.MagicMock()
    myListener = TwitterListener()
    myListener.get_authenticated()

    tweepy.OAuthHandler.assert_called_once_with("***REMOVED***","***REMOVED***");

    auth = tweepy.OAuthHandler()
    auth.set_access_token.assert_called_once_with('***REMOVED***', '***REMOVED***')


@patch('tweepy.Stream')
@patch('tweepy.OAuthHandler')
def test_main(m_tweepy_OAuthHandler,m_tweepy_stream):
    myListener = TwitterListener()
    api_handle = myListener.get_authenticated()

    m_tweepy_stream.listener = MyStreamListener()

#    tweepy.Stream.return_value = mock.MagicMock()
#    my_stream = tweepy.Stream(auth = api_handle.auth,listener=)

#    users_list = ['25073877','838107760721985536']
#    my_stream.filter(follow= '838107760721985536', async=True)

def main():
    #test_read_cfg_from_file()
    #test_get_authenticated()
    test_main()
if __name__ == "__main__":
    main()
