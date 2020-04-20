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
def show_recommendations(recommendations, user):
    """
    This method shows the recomendations generated for a given user.

    Parameters
    ----------
    recommendations : a list of recommend episodes
        The list of recommendations.
    user : string
        The user id.

    Returns
    -------
    None.

    """
    taste= input("Introduce what would you like to listen: ")
    f=open('data.csv')
    csv_f=csv.reader(f)
    mylist=[]
    for row in csv_f:
        if mylist.count(row[9])==0:
            mylist.append(row[9])
    for row in csv_f:
        if row[9]==taste:
            print("What you are looking for is {} episode {}. ".format(row[7],row[8]))
        else:
            print("Not found")
            print("The word introduced must coincide with one of the following one.")
            print(mylist)
