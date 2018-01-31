#!/usr/bin/env python
#-*- coding:utf-8 -*-
import MeCab

def propers(text):
    m=MeCab.Tagger("-Ochasen")
    node=m.parseToNode(text)
    keywords=[]

    while node:
        if "固有名詞" in node.feature.split(","):
            keywords.append(node.surface)
        node=node.next

    return keywords



