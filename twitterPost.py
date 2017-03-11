"""
Authors - Akila Sriram , Manika Murali
Post tweet to twitter handle - slackbot.spanish .
Add the string to post in teh variable tweet and open slackbot.spanish to view the tweet.
"""
import random

import itertools
import tweepy
import sqlite3


# convert sqlite resultset row into dict
def dict_factory(cursor, row):
    try:
        d = {}
        if row != None :
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
    except sqlite3.DataError as msg:
        print ('Error retrieving result set '+msg.__str__())



class TwitterPost :
    def __init__(self):
        '''
        constructor initializes an in memory db connection.Store config data and retrieve config data
        '''
        self.conn = sqlite3.connect(":memory:")
        self.sqlite_store()

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

    def sqlite_store(self):
        '''
        Create table and insert reference data in in-memory DB
        :param conn: connection
        :return:
        '''
        cur = self.conn.cursor()
        try:
            cur.execute("create table twitter_creds (consumer_key, consumer_secret,access_token,access_token_secret,twitter_handle)")
            cur.execute("insert into twitter_creds values (?,?,?,?,?)",('rcIlpeAhFKSXlzhjnWqfkS9x7','J96cwUhHWX93TvSxO7nBpmnqz8LCGuJLNQVFWKehg1bFQRysQe',
                                                                      '838080768408612868-sLc6Uo8iAbdHrJTeEd5C2pjskaitgq6','r1lj2ZT20H0aACoxqZdIHNq6nfBoWtCNwZNFrvAB6JOMn','spanish'))
            self.conn.commit()
            print('1 record for spanish handle committed to DB')
        except sqlite3.Error as msg:
            print (msg)

    #retrieve in memory db meta data for a given twitter handle
    def sqlite_retrieve(self,handle):
        try:
            cfg ={}
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM twitter_creds WHERE twitter_handle= '%s'" % handle)
            row = cursor.fetchone()
            cfg = dict_factory(cursor, row)
            return cfg

        except sqlite3.Error as msg:
            print ("Exception Message while Retrieving Data: "+msg.__str__())

    def twitter_post(self,tweet_msg,tweet_handle):
        '''
        :param tweet_msg: message to be tweeted
        :param tweet_handle: which twitter handle to post the message to
        :return: none
        '''
        try:
            cfg = self.sqlite_retrieve(tweet_handle)
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
