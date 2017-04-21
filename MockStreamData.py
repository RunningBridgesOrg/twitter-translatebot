
import tweepy

from tweepy.streaming import StreamListener

class MockStreamData(tweepy.StreamListener):

    def on_data(self, data):
        #print (data)
        #all_data = json.loads(data)
        #tweet_obj={}
        #author = all_data['user']['id_str']
        #print (author)
        #print (this_id)

        #if(author in this_id) :
        #    print("same?")
        #    tweet_obj['text'] = all_data['text']
        #    tweet_obj['lang'] = all_data['lang']
        #    print (tweet_obj)
        # send it to queue

        response = {'text':'abcd', 'lang':'en'}
        print (response)
        return response
