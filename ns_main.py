#!/usr/bin/env python
#-*- coding: utf-8 -*-
import datetime
import ns_tweet as tw
import ns_mecab as mcb
from ns_yahoonews import ns_yahoonews
def main():
    exclist=["日本"]
    
    # get user's timeline
    # ------------------------------
    #tweets=tw.tweets # sample
    tweets=tw.usrtl()
    
    
    # get keywords in tweets
    # ------------------------------
    tw_kws=[]
    for tweet in tweets:
        tweet=tw.cut(tweet.encode("utf-8"))
        tw_kws+=mcb.propers(tweet)
    tw_kws=list(set(tw_kws))


    # cut 1 length word
    # ------------------------------
    tw_kws=[tw_kw for tw_kw in tw_kws if (len(tw_kw.decode("utf-8"))>1)\
            and (tw_kw not in exclist) ]


    # today
    # ------------------------------
    today_m=str(datetime.datetime.today().month)
    today_d=str(datetime.datetime.today().day)
    today=today_m+"月"+today_d+"日"
    print "today:\t",today


    # the day before yesterday
    # ------------------------------
    dayby=datetime.datetime.today()+datetime.timedelta(days=-2)
    dayby_m=str(dayby.month)
    dayby_d=str(dayby.day)
    dayby=dayby_m+"月"+dayby_d+"日"
    print "dayby:\t",dayby


    # Yahoo News scraping
    # ------------------------------
    yah=ns_yahoonews(today,dayby.decode("utf-8"))
    yah.scrape()
    yah.news_propers()


    # matching keywords and topic of articles.
    # Then, tweet urls of the articles
    # ------------------------------
    for tw_kw in tw_kws:
        articles=yah.match_keyword(tw_kw)
        for i in range(0,len(articles),tw.MAX_ARTICLES):
            cnt=tw.gnews(tw_kw,yah.source,articles[i:i+tw.MAX_ARTICLES])
            try:
                print tw_kw
                tw.twt_mention(cnt)
                print "corret"
            except:
                print "tweet error"



if __name__=='__main__':
    main()
