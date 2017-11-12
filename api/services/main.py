# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib
import time
import os
import sys
import re
from .services import _wikia, _musixmatch, _songmeanings, _songlyrics, _genius, _versuri, _minilyrics

# With Sync. Of course, there is one for now, but for the sake of
# make the code a little bit more cleaner, is declared.
services_list1 = [_minilyrics]

# Without Sync.
services_list2 = [_wikia, _musixmatch, _songmeanings, _songlyrics, _genius, _versuri]

artist = ""
song = ""
url = ""

'''
current_service is used to store the current index of the list.
Useful to change the lyrics with the button "Next Lyric" if
the service returned a wrong song
'''
current_service = -1


def load_lyrics(artist, song, sync=False):
    error = "Error: Could not find lyrics."
    global current_service

    if current_service == len(services_list2)-1: current_service = -1

    if sync == True:
        lyrics, url, timed = _minilyrics(artist, song)
        current_service = -1

    if sync == True and lyrics == error or sync == False:
        timed = False
        for i in range (current_service+1, len(services_list2)):
            lyrics, url = services_list2[i](artist, song)
            current_service = i
            if lyrics != error:
                lyrics = lyrics.replace("&amp;", "&").replace("`", "'").strip()
                break

    #return "Error: Could not find lyrics."  if the for loop doens't find any lyrics
    return(lyrics, url, timed)

# def main():
#     song = 'I think she like me'
#     s = load_lyrics('Rick ross', song, False)
#     print(s[0])

# if __name__ == '__main__':
#     main()