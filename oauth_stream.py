"""
Author - Anu Vaidya, Sujin Emily Cho
date: Mar 12, 2017
Get Streaming tweets for a specific user
"""

import tweepy

from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import json


class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        #print (data)
        all_data = json.loads(data)
        tweet_text = all_data['text']
        tweet_lang = all_data['lang']
        print(tweet_text + tweet_lang)
        return True

    def on_error(self,status):
        print(status)

def read_cfg_from_file():
    cfg = []
    with open("cfg.txt", "r") as f:
        for line in f:
            cfg.append(line.strip())
    return cfg

def main():
    cfg = read_cfg_from_file()
    consumer_key = cfg[0]
    consumer_secret = cfg[1]
    access_token = cfg[2]
    access_token_secret = cfg[3]

    my_stream_listener = MyStreamListener();
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    my_stream = tweepy.Stream(auth = api.auth,listener=my_stream_listener)

    #list of users to follow. Added value has to be "id" not username.
    follow_users = ['25073877','838107760721985536']

    my_stream.filter(follow= follow_users, async=True)

if __name__ == "__main__":
    main()
