import unittest,sqlite3,random


from twitterPost import TwitterPost


class TwitterPostTest (unittest.TestCase) :

    def setUp(self):
        self.tweet = TwitterPost()

    def test_twitterpost(self):
        print("\nRunning twitter_post test")
        self.tweet_msg = "Posting twitter test message from unit tests  "+ str(random.random())
        self.tweet.twitter_post(self.tweet_msg,"spanish")

    def test_twitterpost_failure(self):
        print("\nRunning twitter_post test failure")
        self.tweet_msg = "Posting twitter test message from unit tests  "+ str(random.random())
        self.assertRaisesRegexp(self.tweet.twitter_post(self.tweet_msg,"gibberish"),
                                "error")

if __name__ == ' __main__ ':
    unittest.main()