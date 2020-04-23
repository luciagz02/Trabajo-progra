# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:11:19 2020

@author: Lucía
"""


def is_valid_resource(resource):
    s=""
    if resource=="" or resource==None:
       return False
    else:
        for i in range(-1,-5,-1):
            s=s+resource[i]
        if s=="3pm." or s=="3PM.":
            return True
        else:
            return False        
