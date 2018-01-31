#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tweepy, time, sys

TARGET_TwitterID=""
MAX_ARTICLES=3
TS_TWEET=5

KEYS=list(open("news_scraper_keys"))
CONSUMER_KEY=KEYS[0].strip()
CONSUMER_SECRET=KEYS[1].strip()
ACCESS_KEY=KEYS[2].strip()
ACCESS_SECRET=KEYS[3].strip()

auth=tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api=tweepy.API(auth)


def usrtl():
    tweets=[]
    targettweets=api.user_timeline(screen_name=TARGET_TwitterID)
    for tweet in targettweets:
        tweets.append(tweet.text)
    return tweets

def twt_mention(tweet):
    target_id="@"+TARGET_TwitterID
    tweet=" ".join([target_id,tweet])
    api.update_status(tweet)
    time.sleep(TS_TWEET)

def twt(tweet):
    api.update_status(tweet)
    time.sleep(TS_TWEET)
    
def gnews(keyword,source,urls):
    keyword="["+keyword+"]"
    source=" ".join(["from",source])
    content="\n".join([keyword]+urls+[source])
    return content

def cut(tweet):
    return tweet

