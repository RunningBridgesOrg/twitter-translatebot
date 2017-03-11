"""
Author - Sujin Emily Cho
Get application-only authentication and pull tweets from a specific user
"""
import tweepy

#Read cfg from a seperated file for security
def read_cfg_from_file():
    cfg = []
    with open("cfg.txt", "r") as f:
        for line in f:
            cfg.append(line.strip())
    return cfg

#Application-only-auth
def get_authenticated():
    #will improve later to a fancy way
    cfg = read_cfg_from_file()
    CONSUMER_KEY = cfg[0]
    CONSUMER_SECRET = cfg[1]
    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    return auth

#execute only from the comman line
def main():

    #get access_token
    auth = get_authenticated()
    #Get api hangle
    api = tweepy.API(auth)
    #pull tweets from user timeline
    user_tweets = api.user_timeline(id="@realDonaldTrump")
    for tweet in user_tweets[:3]:
        print (tweet.lang),
        print (tweet.text)
        print ()

if __name__ == "__main__":
    main()
