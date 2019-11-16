#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:38:56 2018

@author: mikeogawa

This Script was used to acquire the adress of the best pork cutlet around Kagoshima station.
(2019/11/16 still working)
"""

from bs4 import BeautifulSoup
import requests
import re


TARGET_URL="https://tabelog.com/kagoshima/A4601/A460101/R7366/rstLst/1/?Srt=D&SrtT=rt&sort_mode=1&LstRange=SG"

# =============================================================================
# target url:input url  delete string:
# function : get a-> find words that are surrounded by "" ->  take the 1st "" -
#      ->delete string
# return get list
# =============================================================================
def get_index_list(target_url):
    delete_string='data-detail-url="'
    delete_string_back='"'
    
    html = requests.get(target_url)
    soup = BeautifulSoup(html.text, "html.parser")
    res_1=soup.find_all("li", class_="list-rst js-bookmark js-rst-cassette-wrap list-rst--ranking")
    
    match=[]
    for res in res_1:
        match+=[re.findall(r'data-detail-url=".*?"',str(res))[0]]
  
    len_url=len(delete_string)
    len_url2=len(delete_string_back)

    return [i[len_url:-len_url2] for i in match]

def get_adress(target_url):

    html = requests.get(target_url)
    soup = BeautifulSoup(html.text, "html.parser")
    res_1=soup.find_all("p", class_="rstinfo-table__address")
    res_2=re.findall(r'<.*?>',str(res_1))
    res=str(res_1[0])
    for a in res_2:
        res=res.replace(a,"")
        
    return res

 
def get_title_list(target_url):

    html = requests.get(target_url)
    soup = BeautifulSoup(html.text, "html.parser")
    res_1=soup.find_all("a", class_="list-rst__rst-name-target cpy-rst-name js-ranking-num")
    res=[x.string for x in res_1]

    return res



def get_status(target_url):

    html = requests.get(target_url)
    soup = BeautifulSoup(html.text, "html.parser")
    res_1=soup.find_all("span", class_="c-rating__val c-rating__val--strong list-rst__rating-val")
    res=[x.string for x in res_1]

    return res
    
    
A=get_index_list(TARGET_URL)

[print(get_adress(i)) for i in A]
