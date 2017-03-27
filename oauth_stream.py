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
#MyStreamListener inherits from tweeepyStreamListerner
class MyStreamListener(tweepy.StreamListener):
    #on_data method of stream listener receives all messages and calls
    def on_data(self, data):
       # print (data)
        all_data = json.loads(data)
        tweet_obj={}
        author = all_data['user']['id_str']
        #print (author)
        #print (this_id)

        if(author in this_id) :
            print("same?")
            tweet_obj['text'] = all_data['text']
            tweet_obj['lang'] = all_data['lang']
           # print (tweet_obj)
        # send it to queue
        return tweet_obj

    def on_error(self,status):
        print(status)

class TwitterListener:
    def read_cfg_from_file(self):
        cfg = {}
        cfg['consumer_key'] = ''
        cfg['consumer_secret'] = ''
        cfg['access_token'] = ''
        cfg['access_token_secret'] = ''

        '''
        with open("cfg.txt", "r") as f:
            for line in f:
                print (line)
                key, value = line.strip().split(':')
                print(value)
                print(key)
                cfg['consumer_key'] = key
                cfg['consumer_secret'] = value
        '''        

                
        return cfg

    #athenticated and get twitter handle
    def get_authenticated(self):
        #later reading from DB
        print(locals())
        cfg = self.read_cfg_from_file()
        if cfg is not None:
            auth = tweepy.OAuthHandler(cfg['consumer_key'],cfg['consumer_secret'])
            auth.set_access_token(cfg['access_token'],cfg['access_token_secret'])
            #print (tweepy.API(auth))
            return tweepy.API(auth)
        else:
            print ("%s: %s at %s" % ('Error','config data is null',__file__))

    def get_userlist(self):
        #list of users to follow. Added value has to be "id" not username.
        #reading from DB
        users = ['25073877','838107760721985536']
        return users;

    def main(self):
        api = self.get_authenticated()
        my_stream_listener = MyStreamListener();
        #Stream method will establish a session and route messages to 
        # stream listener interface.
        my_stream = tweepy.Stream(auth = api.auth,listener=my_stream_listener)
        users = self.get_userlist()
        return my_stream.filter(follow= users, async=True)

if __name__ == "__main__":
    TwitterListener().main()