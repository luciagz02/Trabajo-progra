# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:06:11 2020

@author: Lucía
"""
import unittest 

def is_valid_status(status):
    if status=="200" or status=="206":
        return True
    else:
        return False