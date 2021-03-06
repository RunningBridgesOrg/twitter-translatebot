"""
Author - Anu Vaidya, Sujin Emily Cho
date: Mar 12, 2017
Get Streaming tweets for a specific user
"""

import tweepy

from tweepy.streaming import StreamListener
from tweepy import Stream
import json

#this_id = ['838107760721985536','25073877']
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, user_list):
        print("init")
        self.__this_id = user_list

        #    print("this.id"  + self.__this_id[0])

        #This code is for testing
        # real_tweet = {"text": "Four more years. http:\/\/t.co\/bAJE6Vom",
        # "user": {"id": 266031293949698048,"id_str": "266031293949698048"}
        # }
        #
        # self.on_data(json.dumps(real_tweet))

        #This code is for testing
    #def __call__(self):
        # print ("calling")
        # real_tweet = {"text": "Four more years. http:\/\/t.co\/bAJE6Vom",
        # "user": {"id": 266031293949698048,"id_str": "266031293949698048"}
        # }
        # self.on_data(json.dumps(real_tweet))

    def on_data(self, data):
        #print (data)
        all_data = json.loads(data)
        tweet_obj={}
        author = all_data['user']['id_str']
        #print (author)

        if(author in self.__this_id) :
            print("same?")
            tweet_obj['text'] = all_data['text']
            tweet_obj['lang'] = all_data['lang']
            print (tweet_obj['text'])
        # send it to queue
        return tweet_obj

    def on_error(self,status):
        print(status)

class TwitterListener:
    def __get_userlist(self):
        #list of users to follow. Added value has to be "id" not username.
        #reading from DB
        user_list = ['25073877','838107760721985536']
        return user_list;

    def __init__(self):
    #def __init__(self, service):
        #private attribute
        #self.__user_list = []
        self.__cfg = self.__read_cfg_from_DB()
        self.__user_list = self.__get_userlist()
        #MyStreamListener instance is created inside TwitterListener
        self.myStreamListener =  MyStreamListener(self.__user_list);
        #? If we create the service outside, how can we see the user list?, user list is a private variable.
        #self.myStreamListener = service

    def __read_cfg_from_DB(self):
        cfg = {}
        with open("cfg.txt", "r") as f:
            for line in f:
                # we have to retrieve the correct key for listener.
                key, value = line.strip().split(':')
                cfg[key] = value
                print("cfg " + cfg[key])
        return cfg


    #athenticated and get twitter handle
    def get_authenticated(self):
        #later reading from DB
        #self.__cfg = self.__read_cfg_from_DB()
        if self.__cfg is not None:
            print("get_authenticated" + self.__cfg['consumer_key'])
            auth = tweepy.OAuthHandler(self.__cfg['consumer_key'],self.__cfg['consumer_secret'])
            auth.set_access_token(self.__cfg['access_token'],self.__cfg['access_token_secret'])
            return tweepy.API(auth)
        else:
            print ("%s: %s at %s" % ('Error','config data is null',__file__))


    def main(self):
        api = self.get_authenticated()
        #self.__users_list = self.__get_userlist()

    #    my_stream_listener = MyStreamListener();
    #Do we also need depenedcy injection for stream instance?
        my_stream = tweepy.Stream(auth = api.auth,listener=self.myStreamListener)
        my_stream.filter(follow= self.__user_list, async=True)


if __name__ == "__main__":

    #This code is for depenedcy injection
    #myStreamListenerService = MyStreamListener()
    #MyTwitterListener = TwitterListener(myStreamListenerService)

    MyTwitterListener = TwitterListener()
    MyTwitterListener.main()
    #TwitterListener().main()
