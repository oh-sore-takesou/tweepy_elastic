from twitter_handler.handler import TwitterHandler
from elastic_handler.handler import ElasticSearchHandler

'''
data type ->
[
  {
    'time': datetime,
    'tweet_text': string
  }
]
'''

'''
flow
get required datas from twitter
save in to elasticsearch
'''

if __name__ == '__main__':
    tw = TwitterHandler()
    eh = ElasticSearchHandler()
    eh.es.indices.delete(index='test_tweets')
    eh.create_index('test_tweets')
    for trend_tweet in tw.get_trended_tweets():
        eh.add_doc('test_tweets', trend_tweet)
