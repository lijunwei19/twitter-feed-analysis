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


consumer_key = 'XXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXX'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets=api.search(q=sys.argv[1:],count=5,lang='en')
for tweet in tweets:
  print(tweet.text, file=open("result.txt","a"))
