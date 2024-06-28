# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:28:31 2024

@author: 2561986

SMART MUSIC APP

This is a artist search app implementing the basic csv functions of Python

"""

file = open("songs.csv", encoding='utf8')
header = file.readline().strip().split(",")

input_name = input("Search for an artist name : ")
input_name = input_name.lower().capitalize()
songs = []

for data in file:
    song = data.strip().split(",")
    
    artist_name = song[-1]
    
    if artist_name == input_name:
        if song not in songs:
            songs.append(song)
        
print("{:<17} {:<18} {:<12}".format("Artist", "Song Name", "Year"))    
print("----------------------------------------------------")    
for song in songs:
    artist_name = song[0]
    song_name = song[1]
    year = song[2]
    
    
    print("{:<17} {:<18} {:<12} ".format(artist_name, song_name, year))
    print()
