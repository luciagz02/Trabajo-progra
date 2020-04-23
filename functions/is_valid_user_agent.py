# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:12:22 2020

@author: Lucía
"""


def is_valid_user_agent(user_agent):
    keywords=["bot","spider","crawler", "heritrix","Bot", "Spider","Crawler","Heritrix","BOT","SPIDER", "CRAWLER", "HERITRIX"]
    if user_agent=="" or user_agent==None:
            return False
    else:
        if any(keyword in user_agent for keyword in keywords):
            return False
        else:
            return True


