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


consumer_key = 'OARHsYwZ9PqQ1db87f4S27b9E'
consumer_secret = 'iQx8pHV9k2ZtaEbkokK2dWpMPnNDRANUm2agAbbS07ZjzswtNr'
access_token = '754494342287417344-a7RVsdsLxuQPPkg7vnfydJQHv6agely'
access_token_secret = 'hf0LgJAn0uBl7bcmZMHTfhc2u2gbdqFMjoYOvRJiHePy1'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets=api.search(q=sys.argv[1:],count=5,lang='en')
for tweet in tweets:
  print(tweet.text)
