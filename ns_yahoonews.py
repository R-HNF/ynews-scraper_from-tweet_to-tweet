#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import lxml.html
import time

#------------------------------
# res={"title":"",
#      "link":"",
#      "summary":"",
#      "date":"",
#      "category":""
#      "topics":[]
# }
#-----------------------------

class ns_yahoonews:
    def __init__(self,today,dayby):
        # some default settings
        # --------------------
        self.target_url=\
            "http://news.search.yahoo.co.jp/search?fr=news_sw&p="\
            +today+"&ei=UTF-8"
        print self.target_url
        
        self.source="Yahoo News"
        self.dayby=dayby
        self.flag=0
        self.parse_results=[]
        self.ts_scrape=1
        

    def parse_html(self,root):
        result=[]
        # The order of news is by date on Yahoo NEWS
        # ---div tag---
        for div in root.cssselect("div"):
            if ("class" in div.attrib) and (div.attrib["class"]=="l cf"):

                # ---data structure---
                res={"title":"",
                     "link":"",
                     "summary":"",
                     "d":"",
                     "date":"",
                     "sep":"",
                     "ct1":"",
                     "category":"",
                     "topic":[]
                }

                for child in div.getchildren():
                    if (child.tag=="div") and \
                       ("class" in child.attrib) and \
                       (child.attrib["class"]=="txt"):
                        
                        # ---p tags---
                        for gchild in child.getchildren():
                            if ("class" in gchild.attrib) and \
                               (gchild.attrib["class"]=="a"):
                                
                                # ---summary---
                                res["summary"]=gchild.text_content()

                            else:

                                # g2child
                                for g2child in gchild.getchildren():
                                    if ("class" in g2child.attrib):
                                        
                                        # ---date and category---
                                        res[g2child.attrib["class"]]= \
                                        g2child.text_content()

                    # check the finish
                    # --------------------
                    try:
                        if res["d"][5:5+len(self.dayby)]==self.dayby:
                            self.flag=1
                            print "-"*10,"flag = 1","-"*10
                            return result
                    except:
                        print res["d"]

                    # ---h2 tag---
                    if (child.tag=="h2") and \
                       ("class" in child.attrib) and \
                       (child.attrib["class"]=="t"):
                        gchild=(child.getchildren())[0]
                        
                        # ---a tag---
                        if ("href" in gchild.attrib):
                            
                            # ---title---
                            res["title"]=gchild.text_content()
                            
                            # ---link for article---
                            res["link"]=gchild.attrib["href"]

                # ---copy to date and category---
                res["date"]=res["d"]
                res["category"]=res["ct1"]
                result.append(res)
                
        return result


    def next_target(self,root):
        for span in root.cssselect("span"):
            if ("class" in span.attrib) and \
               (span.attrib["class"]=="m"):
                child=(span.getchildren())[0]
                if ("href" in child.attrib) and \
                   (u"次へ" in child.text_content()):
                    
                    # ---next target---
                    return child.attrib["href"]    

            
    def scrape(self):
        i=1
        while 1:
            
            target_html=requests.get(self.target_url).content
            root=lxml.html.fromstring(target_html)

            # list of dict
            # --------------------
            result=self.parse_html(root)
            self.parse_results+=result

            # check the flag
            # --------------------
            if self.flag==1: break
            else: self.target_url=self.next_target(root)

            print "time",i
            i+=1
            time.sleep(self.ts_scrape)


    def news_propers(self):
        import ns_mecab as mcb
        for result in self.parse_results:
            # proper noun in titile
            # --------------------
            result["topic"]+=\
                mcb.propers(result["title"].encode("utf-8"))
            # proper noun in summary
            # --------------------
            result["topic"]+=\
                mcb.propers(result["summary"].encode("utf-8"))
            
            result["topic"]=list(set(result["topic"]))


    def match_keyword(self,kw):
        # get the url of articles that have a keyword
        # --------------------
        articles=[]
        for res in self.parse_results:
            if kw in res["topic"]:
                articles.append(res["link"])
        return articles
            
