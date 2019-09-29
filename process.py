
try:
    import json
except ImportError:
    import simplejson as json

tweets_filename = 'search_json.txt'
tweets_file = open(tweets_filename, "r")


for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            print(tweet['id']) # This is the tweet's id
            print(tweet['text']) # content of the tweet
            print(tweet['favorite_count'])
            print(tweet['retweet_count'])           
            print(tweet['user']['id']) # id of the user who posted the tweet
            print(tweet['user']['screen_name']) # name of the user account, e.g. "cocoweixu"




