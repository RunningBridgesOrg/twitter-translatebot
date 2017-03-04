"""
Authors - Akila Sriram , Manika Murali
Post tweet to twitter handle - slackbot.spanish .
Add the string to post in teh variable tweet and open slackbot.spanish to view the tweet.
"""

import tweepy
#Build the HTTP request 
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  
  cfg = { 
    "consumer_key"        : "rcIlpeAhFKSXlzhjnWqfkS9x7",
    "consumer_secret"     : "J96cwUhHWX93TvSxO7nBpmnqz8LCGuJLNQVFWKehg1bFQRysQe",
    "access_token"        : "838080768408612868-sLc6Uo8iAbdHrJTeEd5C2pjskaitgq6",
    "access_token_secret" : "r1lj2ZT20H0aACoxqZdIHNq6nfBoWtCNwZNFrvAB6JOMn" 
    }

  api = get_api(cfg)
  tweet = "Hello!This is my second tweet"
  status = api.update_status(status=tweet) 
  

if __name__ == "__main__":
  main()
