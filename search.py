import sys
try:
    import json
except ImportError:
    import simplejson as json


try:
    import json
except ImportError:
    import simplejson as json

import tweepy


consumer_key = 'XXXXXXX'
consumer_secret = 'XXXXXXXX'
access_token = 'XXXXXXXX'
access_token_secret = 'XXXXXXXX'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets=api.search(q=sys.argv[1:],count=5,lang='en')
for tweet in tweets:
  print(tweet.text)
