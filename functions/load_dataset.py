# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:59:24 2020

@author: Lucía
"""
import os
import csv

def load_dataset(filename="data.csv"):
    data = []
    if filename and os.path.isfile(filename):
        csv_file = open(filename, encoding="utf-8") 
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
        csv_file.close()
    return data
