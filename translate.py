"""
   This code does the part of google translate.   
   Takes string of text to be translated, the languge it needs to be translated to, and the API key of the user accessing the google translate, makes a request to google translate. 

"""
import requests,json

def get_authenticated():
    """
     Inputs: 
       - None
     Outputs:
       - key : a string representing the API key that will be used in other functions to access google translate.
     Process:
       - Read in a pre-existing text file that should only have 1 line that contains the API key  associated with a user.  
    """
    fName = "apiKey.txt"
    try:
        with open(fName,"r") as f:
            key = ""
            for line in f:
                key = line.strip()
            
            #Error condition checking for existing key.
            if not key:
                print "No api key is found"
            return key
    except IOError:
        print "Could not read file: '%s'"%(fName)

def get_input_tweets():
    """
     Inputs: 
       - None
     Outputs:
       - listOfTweets : a list of dictionary of tweets to translate.  Dictionary contains information of string to translate and language to translate to.
     Process:
       - Create some text to translate and put into dictionary, and then list.  
    """
    listOfTweets = []
    tweet1 = {}
    tweet1['text'] = "Let them eat cake"
    tweet1['lang'] = "fr"

    tweet2 = {}
    tweet2['text'] = "Doing demonstration is hard"
    tweet2['lang'] = "ko"

    tweet3 = {}
    tweet3['text'] = "I hope this works!"
    tweet3['lang'] = "zh-TW"

    tweet4 = {}
    tweet4['text'] = "We are moving on Friday!"
    tweet4['lang'] = "es"

    listOfTweets.append(tweet1)
    listOfTweets.append(tweet2)
    listOfTweets.append(tweet3)
    listOfTweets.append(tweet4)

    return listOfTweets

def translateTweets(tweetsToTranslate,api_key):
    """
     Inputs: 
       - tweetsToTranslate : list of tweets, which is stored in a dictionary data structure providing info on text, target language.
       - api_key :  Google Translate API credentials. 
     Outputs:
       - translatedTweets : dictionary of translated tweets, where key is the string to translate, and value is the translation string (in unicode)
     Process:
       - Loop through each tweet that is in the list of tweets.  For each tweet, obtain the string to be translated, and the target language. 
       - Make a request to google api with provided parameters of text, target language and api-key.  Returns an object 'resp'. 
       - Put translated text into a dictionary structure, where key is the string to translate, and value is the translation. Return result. 
    """

    translatedTweets = {}
    for tweet in tweetsToTranslate:
        payload = {'q':tweet['text'],'target':tweet['lang'],'key':api_key}
        resp=requests.get('https://www.googleapis.com/language/translate/v2',params=payload)
        #print resp.text
        response_dict = resp.json()
        #print "%s ---> %s\n"%(tweet['text'],response_dict["data"]["translations"][0]["translatedText"])
        translatedTweets[tweet['text']] = response_dict["data"]["translations"][0]["translatedText"]
    return translatedTweets


def main():

    tweetsToTranslate = get_input_tweets()

    api_key = get_authenticated()

    if api_key:
        translated = translateTweets(tweetsToTranslate,api_key)
    
        #debug prints.
        for key,value in translated.iteritems():
            print "%s (%s) ---> %s (%s)\n"%(key,type(key),value,type(value))
    

if __name__ == "__main__":
    main()
