"""
Authors - Akila Sriram , Manika Murali
Post tweet to twitter handle - slackbot.spanish .
Add the string to post in teh variable tweet and open slackbot.spanish to view the tweet.
"""
import random

import tweepy,sqlite3
from dbConnect import connect_to_DB

class TwitterPost :
    def __init__(self):
        self.metaData= connect_to_DB()


    def get_authenticated(self,cfg):
        '''
        Get authetiated by twitter
        :param cfg: dictionary object having access token and secrets
        :return: Api object to post tweets
        '''
        if cfg != None:
            auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
            auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
            return tweepy.API(auth)
        else:
            print ('config data is null')



    def twitter_post(self,tweet_msg,tweet_handle):
        '''
        :param tweet_msg: message to be tweeted
        :param tweet_handle: which twitter handle to post the message to
        :return: none
        '''
        try:
            cfg = self.metaData.sqlite_retrieve(tweet_handle)
            twitter_api_handle = self.get_authenticated(cfg)
            if twitter_api_handle != None :
                status = twitter_api_handle.update_status(status=tweet_msg)
                print("Hey I Tweeted!!!!!")
        except :
            print ('Oops!!! Something went wrong.Posting to twitter failed.')
            raise




    def main(self):
      '''
      cfg = {
        "consumer_key"        : "rcIlpeAhFKSXlzhjnWqfkS9x7",
        "consumer_secret"     : "J96cwUhHWX93TvSxO7nBpmnqz8LCGuJLNQVFWKehg1bFQRysQe",
        "access_token"        : "838080768408612868-sLc6Uo8iAbdHrJTeEd5C2pjskaitgq6",
        "access_token_secret" : "r1lj2ZT20H0aACoxqZdIHNq6nfBoWtCNwZNFrvAB6JOMn"
        }
    '''

    if __name__ == "__main__":
      main()
