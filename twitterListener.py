"""
Author - Sujin Emily Cho, Anu
Get application-only authentication and pull tweets from a specific user
"""
import tweepy

#Read cfg from a seperated file for security
def read_cfg_from_file():
    cfg = {}
    with open("cfg.txt", "r") as f:
        for line in f:
            key, value = line.strip().split(':')
            cfg[key] = value
    return cfg

#Application-only-auth
def get_authenticated():
    cfg = read_cfg_from_file()
    if cfg is not None:
        auth = tweepy.AppAuthHandler(cfg['consumer_key'],cfg['consumer_secret'])
        #auth.set_access_token(cfg['access_token'],cfg['access_token_secret'])
        return tweepy.API(auth)
    else:
        print ("%s: %s at %s" % ('Error','config data is null',__file__))

def get_tweets_from_timeline(user):

    user = "@"+user
    list_of_tweet = []
    user_tweets = api.user_timeline(id=user)
    for tweet in user_tweets:
        req{}
        req['text'] = tweet.text
        req['user'] = tweet.user.screen_name
        req['lang'] = tweet.lang
        list_of_tweet.add(req)

    return list_of_tweet




#execute only from the comman line
def main():

    #Get api hangle
    api = get_authenticated()
    #pull tweets from user timeline
    user_tweets = api.user_timeline(id="@PaloAltoPolice")
    list_users = ["PaloAltoPolice","realDonaldTrump","tw_listener"]

    tweets_from_user =[]
    for user in list_users:
        tweets_from_user.append(get_tweets_from_timeline(user))


if __name__ == "__main__":
    main()
