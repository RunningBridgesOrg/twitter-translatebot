"""
Author - Anu Vaidya, Sujin Emily Cho
date: Mar 12, 2017
Get Streaming tweets for a specific user
"""

import tweepy

from tweepy.streaming import StreamListener
from tweepy import Stream
import json

this_id = ['838107760721985536','25073877']
class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        print("init")

        real_tweet = {"text": "Four more years. http:\/\/t.co\/bAJE6Vom",
        "user": {"id": 266031293949698048,"id_str": "266031293949698048"}
        }

        self.on_data(json.dumps(real_tweet))

    def __call__(self):
        print ("calling")
        real_tweet = {"text": "Four more years. http:\/\/t.co\/bAJE6Vom",
        "user": {"id": 266031293949698048,"id_str": "266031293949698048"}
        }
        self.on_data(json.dumps(real_tweet))

    def on_data(self, data):
        #print (data)
        all_data = json.loads(data)
        tweet_obj={}
        author = all_data['user']['id_str']
        print (author)
        #print (this_id)

        if(author in this_id) :
            print("same?")
            tweet_obj['text'] = all_data['text']
            tweet_obj['lang'] = all_data['lang']
            print (tweet_obj)
        # send it to queue
        return tweet_obj

    def on_error(self,status):
        print(status)

class TwitterListener:

#    def __init__(self):
        #private attribute
#        self.__user_list = []
#        self.__cfg = {}
        #self.__MyStreamListener =  MyStreamListener();

    def read_cfg_from_DB(self):
        cfg = {}
        with open("cfg.txt", "r") as f:
            for line in f:
                # we have to retrieve the correct key for listener.
                key, value = line.strip().split(':')
                cfg[key] = value
        return cfg


    #athenticated and get twitter handle
    def get_authenticated(self):
        #later reading from DB
        cfg = self.read_cfg_from_DB()
        if cfg is not None:
            auth = tweepy.OAuthHandler(cfg['consumer_key'],cfg['consumer_secret'])
            auth.set_access_token(cfg['access_token'],cfg['access_token_secret'])
            return tweepy.API(auth)
        else:
            print ("%s: %s at %s" % ('Error','config data is null',__file__))

    def get_userlist(self):
        #list of users to follow. Added value has to be "id" not username.
        #reading from DB
        users_list = ['25073877','838107760721985536']
        return self.__user_list;

    def main(self):

        api = self.get_authenticated()
        users = self.get_userlist()

    #    my_stream_listener = MyStreamListener();
        my_stream = tweepy.Stream(auth = api.auth,listener=my_stream_listener)
        my_stream.filter(follow= users, async=True)


if __name__ == "__main__":
    TwitterListener().main()
