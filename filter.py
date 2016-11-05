# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 16:30:34 2016

@author: Rob Braggaar
"""
import logging
try:
    from tweepy import OAuthHandler
    from tweepy import Stream
    from tweepy.streaming import StreamListener
    import time
    import json
    from HTMLParser import HTMLParser
except:
    logging.critical("---- Error importing modules -----")

# API authorization config variables
consumer_key = "8BJ7fv4ogKZZMbTGki4O1IOXy"
consumer_secret = "WYPMRW7PpqPjON0JSNTyVrkWzpvaAfHKLcDnxK1KpCXrLY2bbN"

access_token = "793757327497240580-yqKhGsQoQg3nC8RJli4lQ5mUIdRYMDW"
access_token_secret = "GIQETfqjbVRg9Az8wsuerF86Ef4UJReK5wp6UgoQsGvZH"



# Status listener
class status_listener(StreamListener):
    # counter for number of tweets sent from Schiphol
    from_schiphol = 0
    count = 0
    def __init__(self, time_limit=60*1):
        self.start_time = time.time()
        self.limit = time_limit

    def on_data(self, data):
        if (time.time() - self.start_time) > self.limit:
            print "end time", time.time()
            print "tweets from Schiphol: ", l.from_schiphol
            print "runtime", time.time() - l.start_time
            return False
        decoded = json.loads(HTMLParser().unescape(data))
        if decoded.get('coordinates',None) is not None:
            coordinates = decoded.get('coordinates','').get('coordinates','')
            if (4.73 < coordinates[0] < 4.77) and (52.29 < coordinates[1] < 52.32):
                status_listener.from_schiphol += 1
            print coordinates,
        status_listener.count += 1
        print "tweet number: ", status_listener.count
        return True

    def on_error(self, status_code):
        print status_code
        return True

if __name__ == '__main__':
    t_end = time.time() + 60 * 1 #1 min
    print "start time", time.time()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    l = status_listener()
    stream = Stream(auth, l)
    # Filters the Twitter stream to capture data by location Amsterdam
    stream.filter(locations=[4.73,52.29,4.98,52.42])


