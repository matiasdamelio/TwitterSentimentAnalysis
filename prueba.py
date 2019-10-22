# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:00:41 2019

@author: mdamelio
"""

import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import sys
import time

from config import *

TRACKING_KEYWORDS = ['#Bolivia']
OUTPUT_FILE = 'file.json'

class StdOutListener(StreamListener):
    
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0
        self.file = open(OUTPUT_FILE, "w")
        
    def on_status(self, status):
        
        try:
            tweet = status._json
            self.file.write( json.dumps(tweet) + '\n' )
            self.num_tweets += 1
            print("tweet " + str(status.created_at) + "\n")
            print(status.text + "\n")
        except:
            print("Unexpected error:", sys.exec_info()[0])
        return True
       
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':
    
    listener = StdOutListener()
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    stream = Stream(auth, listener)
    
    stream.filter(track=TRACKING_KEYWORDS)