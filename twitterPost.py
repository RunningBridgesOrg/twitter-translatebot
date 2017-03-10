"""
Authors - Akila Sriram , Manika Murali
Post tweet to twitter handle - slackbot.spanish .
Add the string to post in teh variable tweet and open slackbot.spanish to view the tweet.
"""
import random

import itertools
import tweepy
import sqlite3


#Build the HTTP request
def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


#Create table and insert reference data in in-memory DB
def sqlite_store(conn):
    cur = conn.cursor()
    cur.execute("create table twitter_creds (consumer_key, consumer_secret,access_token,access_token_secret,twitter_handle)")
    cur.execute("insert into twitter_creds values (?,?,?,?,?)",('rcIlpeAhFKSXlzhjnWqfkS9x7','J96cwUhHWX93TvSxO7nBpmnqz8LCGuJLNQVFWKehg1bFQRysQe',
                                                                  '838080768408612868-sLc6Uo8iAbdHrJTeEd5C2pjskaitgq6','r1lj2ZT20H0aACoxqZdIHNq6nfBoWtCNwZNFrvAB6JOMn','spanish'))
    #commit the row insert to disk
    conn.commit()
    print ('Records committed to DB')

#retrieve in memory db meta data for a given twitter handle
def sqlite_retrieve(conn,handle):
    cfg ={}
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM twitter_creds WHERE twitter_handle= '%s'" % handle)
    row = cursor.fetchone()
    cfg = dict_factory(cursor, row)
    return cfg

#convert sqlite resultset row into dict
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def main():
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

  sqlite_store(conn)
  cfg = sqlite_retrieve(conn,"spanish")

  api = get_api(cfg)
  tweet = "Hello! Hi There ! This is my test tweet blah blah la la la "+ str(random.random())
  status = api.update_status(status=tweet) 
  print ("Hey I Tweeted!!!!!")

if __name__ == "__main__":
  main()
