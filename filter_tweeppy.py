
from tweepy import OAuthHandler
import tweepy
## the key of twitter API
import private
from tweepy.streaming import StreamListener
from tweepy import Stream
import json

class TwitterStreamer():
    def __init__(self):
        pass
    def stream_tweets(self, filter_feed_stream, track_content):
        listener = StdOutListener(filter_feed_stream)

        ## using the twitter api key here, my key file is named "private.yp"
        auth = tweepy.OAuthHandler(private.consumer_key, private.consumer_secret)
        auth.set_access_token(private.access_token, private.access_token_secret)
        stream = Stream(auth, listener)
        stream.filter(track=track_content)

class StdOutListener(StreamListener):
    def __init__(self, filter_feed_stream):
        self.filter_feed_stream = filter_feed_stream

    def on_data(self, data):

        try:
            print(data)
            with open(self.filter_feed_stream, 'a') as outfile:
                outfile.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True         
    def on_error(self, status):
        print(status)

 


def track_feed(track_content):
   filter_feed_stream = "result.txt"
   twitter_streamer = TwitterStreamer()
   twitter_streamer.stream_tweets(filter_feed_stream, track_content)

## function to tracking the feeds with "key words"

## for example: 
track_content = ["BU", "boston university"]
track_feed(track_content)
