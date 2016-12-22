import tweepy
import datetime
import time
import os

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

class TwitterHandler:
    def __init__(self):
        self.api = tweepy.API(auth)

    # get all current topicks in tokyo as a list of strings
    def get_topicks(self):
        topicks = []
        for trend in self.api.trends_place(90036018)[0]['trends']:
            topicks.append(trend['name'])

        return topicks


    # search today's tweet
    def search_with_list(self, words, count=200):
        searched_tweets = []
        max_id = None
        for i in range(int(count/100)):
            print('time {}'.format(i))
            for word in words:
                try:
                    tweets = self.api.search(q=word, max_id=max_id, count=count)
                except:
                    print('sleeping')
                    time.sleep(60*15 + 10)
                    tweets = self.api.search(q=word, max_id=max_id, count=count)
                print('will get')
                for tweet in tweets:
                    searched_tweet = {}
                    searched_tweet[str(tweet.created_at)] = tweet.text
                    searched_tweets.append(searched_tweet)
                    max_id = tweet.id
            print(len(searched_tweets))

        return searched_tweets

    # take trended tweets by date for days: int
    def get_trended_tweets(self):
        # key_words = self.get_topicks()
        key_words = ['今日']

        return self.search_with_list(key_words, count=100000)
