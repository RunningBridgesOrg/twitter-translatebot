import requests,json

#Function for getting API key from a stored file "apiKey.txt"
def get_authenticated():
    with open("apiKey.txt","r") as f:
        for line in f:
            key = line.strip()
        return key

def get_input_tweets():
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
    translatedTweets = {}
    for tweet in tweetsToTranslate:
        payload = {'q':tweet['text'],'target':tweet['lang'],'key':api_key}
        resp=requests.get('https://www.googleapis.com/language/translate/v2',params=payload)
        print resp.text
        response_dict = resp.json()
        print "%s ---> %s\n"%(tweet['text'],response_dict["data"]["translations"][0]["translatedText"])
	translatedTweets[tweet['text']] = response_dict["data"]["translations"][0]["translatedText"]
    print translatedTweets


def main():
    api_key = get_authenticated()
    #Error condition checking for existing key.
    if not api_key:
        print "No api key is found"

    #Get input tweets
    tweetsToTranslate = get_input_tweets()

    #Translate!
    translateTweets(tweetsToTranslate,api_key)
    

if __name__ == "__main__":
    main()
