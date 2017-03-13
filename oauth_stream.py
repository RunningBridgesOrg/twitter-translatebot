"""
Author - Anu Vaidya
Get Streaming tweets for a particular keyword
"""
import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

class MyStreamListener(tweepy.StreamListener):
	"""A listener handles tweets that are received from the stream.
	This is a basic listener that just prints received tweets to stdout

	"""

	def on_data(self,data):
		print(data)
		return true

	def on_error(self,status):
		print(status)

def main():

	myStreamListener = MyStreamListener();

	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	api = tweepy.API(auth)
	myStream = tweepy.Stream(auth = api.auth,listener=myStreamListener)
		
	myStream.filter(track=['PaloAlto'],async=True)

if __name__ == "__main__":
    main()		
