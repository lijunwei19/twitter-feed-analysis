import sys
try:
    import json
except ImportError:
    import simplejson as json

import tweepy


consumer_key = 'GAjg6NAk34JjP0m1GoNkD1SxM'
consumer_secret = 'Try9ShGIJl30TjYgiLcys6YFspv0boRKBLbGILzdhnn4TfkdUa'
access_token = '754494342287417344-TTs4GRqqTuO8RWF35YgJA1XDbuwOjmK'
access_token_secret = 'dctQBOIcT2kV9SH5Kuz9JcrmlWOj5NYghN38iXosGWaJw'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets=api.search(q=sys.argv[1:],count=20,lang='en')
for tweet in tweets:
  print(tweet._json)
 