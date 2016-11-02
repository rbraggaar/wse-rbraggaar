# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 16:30:34 2016

@author: Rob Braggaar
"""

try:
    from tweepy import OAuthHandler
    from tweepy import Stream
    from tweepy.streaming import StreamListener
except:
    print "Error importing modules"

# API authorization config variables
consumer_key = "8BJ7fv4ogKZZMbTGki4O1IOXy"
consumer_secret = "WYPMRW7PpqPjON0JSNTyVrkWzpvaAfHKLcDnxK1KpCXrLY2bbN"

access_token = "793757327497240580-yqKhGsQoQg3nC8RJli4lQ5mUIdRYMDW"
access_token_secret = "GIQETfqjbVRg9Az8wsuerF86Ef4UJReK5wp6UgoQsGvZH"

# Status listener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status__code):
        if status__code == 420:
            return False


if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    l = StdOutListener()
    stream = Stream(auth, l)

    # Filters the Twitter stream to capture data by location Amsterdam
    stream.filter(locations=[4.73,52.29,4.98,52.42])