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
     topics=[]
    f=open('data.csv')
    csv_f=csv.reader(f)
    for row in csv_f:
        if row[10]==200 or row[10]==206:
            topics.append(row[9])
    v=open('observations.csv')
    csv_v=csv.reader(v)
    episodes=[]
    for row_2 in csv_v:
        if topics.count(row_2[10])!=0:
            episodes.append(row_2[9])
    new_episode=[]
    for i in episodes:
        if new_episode.count(i)==0:
            new_episode.append(i)
    dictionary_episodes={}
    for j in new_episode:
        dictionary_episodes["j"]=[episodes.count(j)]
    organised_dictionary = sorted(dictionary_episodes.items(), key=lambda x: x[1], reverse=True)
    recommendations_organised=[]
    for k in organised_dictionary.key():
        recommendations_organised.append(k)
    
    final_recommendations=[]
    n=0
    while n<5:
        final_recommendations.append(recommendations_organised[n])
        n+=1
    print("These are the recommendations for you: ")
    for a in final_recommendations:
        print("- {}".format(a)
