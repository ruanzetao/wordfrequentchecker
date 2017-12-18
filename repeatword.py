#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Title         :  Keywords Generator
About         :  Simple program to find how much times a word repeat a webpage.
Author        :  Satheesh Kumar D
Date          :  07-05-2017
Organisation  :  LICO TECH
"""



import requests
from bs4 import BeautifulSoup
import operator
import sys
#import string
#import codecs




def start(url):
    #sys.stdin = codecs.getreader('utf_8')(sys.stdin)
    word_list = []
    error = 0
    src = requests.get(url).text
    soup = BeautifulSoup(src,"html.parser")
    #unicode(soup,"utf_8")
    for para in soup.findAll('p'):
        content = para.string
        try:
            words = content.lower().split()
        except AttributeError:
            error += 1
        for word in words:
            word_list.append(word)
    clean_list(word_list)


def clean_list(word_list):
    cleaned = []
    for word in word_list:
        symbols = "!@#$%^&*()_-+=~`{[}]|\\:;'\"\<\,\.\>\/\?"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            cleaned.append(word)
    frequency(cleaned)


def frequency(uncleanlist):
    #sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
    words_list = {}
    for word in uncleanlist:
        if word in words_list:
            words_list[word] += 1
        else:
            words_list[word] = 1
    for key, value in sorted(words_list.items(), key=operator.itemgetter(1)):
        #key.decode('utf8')
        print(key, value)

start("http://localhost/wordfrequentchecker/index.html")