# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:28:31 2024

@author: 2561986

SMART MUSIC APP

This is an artist search app implementing basic CSV functions in Python
"""

def read_csv(file_path):
    songs = []
    with open(file_path, 'r', encoding='utf8') as file:
        header = file.readline().strip().split(",")
        for line in file:
            song = line.strip().split(",")
            songs.append(song)
    return header, songs

def search_artist(songs, artist_name):
    artist_name = artist_name.lower().capitalize()
    found_songs = []
    for song in songs:
        if song[-1].lower() == artist_name:
            found_songs.append(song)
    return found_songs

def display_songs(songs, header):
    print("{:<17} {:<18} {:<12}".format(header[0], header[1], header[2]))
    print("----------------------------------------------------")
    for song in songs:
        print("{:<17} {:<18} {:<12}".format(song[0], song[1], song[2]))

if __name__ == "__main__":
    file_path = "songs.csv"
    header, all_songs = read_csv(file_path)
    input_name = input("Search for an artist name: ")
    found_songs = search_artist(all_songs, input_name)
    display_songs(found_songs, header)
