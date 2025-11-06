import os
import youtube_oauth

from googleapiclient.discovery import build

youtube = build('youtube', 'v3', credentials=youtube_oauth.credentials)

# request = youtube.videos().list(
#     part='snippet,contentDetails,statistics',
#     id='VIDEO_ID'
# )

request = youtube.playlistItems().list(
    part='status',
    playlistId='PLQYbfmTsxXjCGZVtWlzOW3JKuVkqy_UMU'>
)

response = request.execute()

print(response)

def connect():
    pass

