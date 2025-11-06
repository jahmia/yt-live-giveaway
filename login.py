import os
import youtube_oauth

from googleapiclient.discovery import build

youtube = None

def connect():
    youtube = build('youtube', 'v3', credentials=youtube_oauth.credentials)
    return youtube


