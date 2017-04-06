#! /usr/local/bin/python3

from pubsub import pub

# ------------ create a listener -----Need to call function written by catherine and michelle-------------
def translation(handle, language, tweet):
 #call translation function here
 print ('Handle,Language,Tweet =', handle,language,tweet)

# ------------ register listener ------------------
def setup_listener(topic):
 pub.subscribe(translation, topic)

#--------------function for language retrival from db --------------- 
def query_db_for_language_per_handle(handle):
  dict = {}
  dict['@GHC'] = ['spanish', 'german']
  dict['@eastpaloalto'] = ['spanish', 'french']
  languages_per_handle = []
  languages_per_handle = dict[handle]
  return languages_per_handle

#---------send message-------function called by anu/emily------
def create_message(handle, tweet):
  languages_per_handle = query_db_for_language_per_handle(handle)
  for language in languages_per_handle:
   topic = handle + "_" + language
   #@ is treated as an invalid char in topic and needs to be removed from the handle before creating a topic
   topic = topic.replace("@","")
   setup_listener(topic)
   pub.sendMessage(topic, handle=handle, language=language, tweet=tweet)
  
#Testing function
def handle_tweet_mock_db():
  dict = {}
  dict = {'@GHC':'This is the 140 char tweet at the @GHC handle', '@eastpaloalto':'This is the 140 char tweet written at @eastpaloalto handle'}
  return dict

def main():
  #testing
  handle_tweet = handle_tweet_mock_db()
  for handle, tweet in handle_tweet.items():
    #will be called by anu/emily
    create_message(handle,tweet)

if __name__ == "__main__":
  main()
