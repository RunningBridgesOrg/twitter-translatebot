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
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class TwitterPost :
    #Build the HTTP request
    def get_authenticated(self,cfg):
        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
        return tweepy.API(auth)


    #Create table and insert reference data in in-memory DB
    def sqlite_store(self,conn):
        cur = conn.cursor()
        try:
            cur.execute("create table twitter_creds (consumer_key, consumer_secret,access_token,access_token_secret,twitter_handle)")
            cur.execute("insert into twitter_creds values (?,?,?,?,?)",('rcIlpeAhFKSXlzhjnWqfkS9x7','J96cwUhHWX93TvSxO7nBpmnqz8LCGuJLNQVFWKehg1bFQRysQe',
                                                                      '838080768408612868-sLc6Uo8iAbdHrJTeEd5C2pjskaitgq6','r1lj2ZT20H0aACoxqZdIHNq6nfBoWtCNwZNFrvAB6JOMn','spanish'))
            conn.commit()
            print('Records committed to DB')
        except sqlite3.Error as msg:
            print (msg)

    #retrieve in memory db meta data for a given twitter handle
    def sqlite_retrieve(self,conn,handle):
        try:
            cfg ={}
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM twitter_creds WHERE twitter_handle= '%s'" % handle)
            row = cursor.fetchone()
            cfg = dict_factory(cursor, row)
            return cfg
        except sqlite3.Error as msg:
            print ("Exception Message while Retrieving Data: "+msg.__str__())


    def tweet_to_twitter(self,tweetMsg,api):
        status = api.update_status(status=tweetMsg)
        print("Hey I Tweeted!!!!!")


    def main(self):
      '''
      cfg = {
        "consumer_key"        : "rcIlpeAhFKSXlzhjnWqfkS9x7",
        "consumer_secret"     : "J96cwUhHWX93TvSxO7nBpmnqz8LCGuJLNQVFWKehg1bFQRysQe",
        "access_token"        : "838080768408612868-sLc6Uo8iAbdHrJTeEd5C2pjskaitgq6",
        "access_token_secret" : "r1lj2ZT20H0aACoxqZdIHNq6nfBoWtCNwZNFrvAB6JOMn"
        }
    '''
     #initializes an in memory db connection.Store config data and retrieve config data
      conn = sqlite3.connect(":memory:")

      self.sqlite_store(conn)
      cfg = self.sqlite_retrieve(self,conn,"spanish")
      twitter_api_handle = self.get_authenticated(self, cfg)
      tweet = "Hello! Hi There ! This is my test tweet blah blah la la la " + str(random.random())
      self.tweet_to_twitter(tweet,twitter_api_handle)



    if __name__ == "__main__":
      main()
