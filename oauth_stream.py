"""
Author - Anu Vaidya, Sujin Emily Cho
date: Mar 12, 2017
Get Streaming tweets for a specific user
"""

import tweepy

from tweepy.streaming import StreamListener
from tweepy import Stream
import json

this_id = '838107760721985536'
class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        #print (data)
        all_data = json.loads(data)

        tweet_obj={}
        tweet_obj['text'] = all_data['text']
        tweet_obj['lang'] = all_data['lang']
        tweet_obj['created_at'] = all_data['created_at']
        print (tweet_obj)
        return tweet_obj

    def on_error(self,status):
        print(status)


def read_cfg_from_file():
    cfg = {}
    with open("cfg.txt", "r") as f:
        for line in f:
            key, value = line.strip().split(':')
            cfg[key] = value
    return cfg

#athenticated and get twitter handle
def get_authenticated():
    cfg = read_cfg_from_file()
    if cfg is not None:
        auth = tweepy.OAuthHandler(cfg['consumer_key'],cfg['consumer_secret'])
        auth.set_access_token(cfg['access_token'],cfg['access_token_secret'])
        return tweepy.API(auth)
    else:
        print ("%s: %s at %s" % ('Error','config data is null',__file__))


def main():

    api = get_authenticated()

    my_stream_listener = MyStreamListener();
    my_stream = tweepy.Stream(auth = api.auth,listener=my_stream_listener)

    #list of users to follow. Added value has to be "id" not username.
    follow_users = ['25073877','838107760721985536']
    my_stream.filter(follow= follow_users, async=True)

if __name__ == "__main__":
    main()
