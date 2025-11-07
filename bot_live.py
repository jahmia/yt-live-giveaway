# coding utf-8
import json
import requests

from urllib.parse import urlparse
from googleapiclient.discovery import build

youtube = None
comments = []

def is_structurally_valid_url(url_string):
    try:
        result = urlparse(url_string)
        print(result)
        return all([result.netloc])
    except ValueError:
        return False

def set_unlisted_stream(stream=None):
    if not stream:
        stream = input("Enter the stream link : ")
        if not is_structurally_valid_url(stream):
            print("The link is not valid. Please enter a valid URL.")
            return set_unlisted_stream()
    return stream

def set_keyword():
    keyword = input("Enter keyword to monitor : ")
    return keyword

def get_participants():
    pass

def get_live_details(video_id):
    request = youtube.videos().list(
        part='snippet,statistics,liveStreamingDetails',
        id=video_id
    )
    response = request.execute()
    content = response.get('items', [])[0]

    res = {
        'id': content.get('id'),
        'title': content['snippet']['title'],
        'channelTitle': content['snippet']['channelTitle'],
        'liveBroadcastContent': content['snippet']['liveBroadcastContent'],
        'liveStreamingDetails': content.get('liveStreamingDetails'),
        'commentCount': int(content.get('statistics')['commentCount'])
    }
    print("\nHere is some details about the youtube video.")
    print(json.dumps(res, indent=4))
    if 'liveBroadcastContent' in res and res['liveBroadcastContent'] != 'live':
        print("The video is not live currently. Aborting")
        exit(0)
    return content

def get_live_chats(liveChatId, keyword):
    # TODO: Also check comments for live video
    request = youtube.liveChatMessages().list(
        liveChatId=liveChatId,
        part='snippet,authorDetails',
        maxResults=200
    )
    response = request.execute()
    print(json.dumps(response, indent=4))
    return response


# youtube = youtube_oauth.connect()
youtube = build(
    'youtube', 'v3',
    developerKey="AIzaSyBB9KR0avf3MJ3njd56raMUpjTOor9dqvo",
)
# link = set_unlisted_stream()
# mekOjGBYeoQ    UCI
# vQQEaSnQ_bs    Python Youtube API
# TEuRjhhYkvA     Outlier Odoo - Gestion d'un parc
live = get_live_details("l8PMl7tUDIE")
key = set_keyword()
liveChatId = live.get('liveStreamingDetails', {}).get('activeLiveChatId')
get_live_chats(liveChatId, keyword=key)


