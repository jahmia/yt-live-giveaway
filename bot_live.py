# coding utf-8
import json
import requests
import youtube_oauth

from urllib.parse import urlparse
from googleapiclient.discovery import build

youtube = None
comments = []

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
    request = youtube.liveBroadcasts().list(
        part='snippet,contentDetails,status',
        id=video_id
    )
    response = request.execute()
    # content = response.get('items', [])
    # content = content[0] if content else []

    # res = {
    #     'id': content.get('id'),
    #     'title': content['snippet']['title'],
    #     'channelTitle': content['snippet']['channelTitle'],
    #     'liveBroadcastContent': content['snippet']['liveBroadcastContent'],
    #     'commentCount': int(content.get('statistics')['commentCount'])
    # }
    print("\nHere is some details about the youtube video.")
    print(json.dumps(content, indent=4))
    return content

def get_live_chats(video_id, keyword):
    # TODO: Also check comments for live video
    next_page = 'first'
    while next_page:
        if next_page == 'first':
            next_page = None

        request = youtube.commentThreads().list(
            part="id,snippet",
            videoId=video_id,
            textFormat='plainText',
            searchTerms=keyword,
            order='time',
            maxResults=100,
            pageToken=next_page
        )
        response = request.execute()
        content = response.get('items')
        for ct in content:
            c = ct.get('snippet').get('topLevelComment')
            s = c.get('snippet')
            comments.append({
                "kind": c['kind'],
                "id": c['id'],
                "authorDisplayName": s.get('authorDisplayName'),
                "textDisplay": s.get('textDisplay'),
                "publishedAt": s.get('publishedAt'),
                "updatedAt": s.get('updatedAt'),
            })
        
        next_page = response.get('nextPageToken')
    
    print(f"Found {len(comments)} comments with keyword '{keyword}':")
    return comments


youtube = youtube_oauth.connect()
# link = set_unlisted_stream()
# mekOjGBYeoQ    UCI
# vQQEaSnQ_bs    Python Youtube API
# TEuRjhhYkvA     Outlier Odoo - Gestion d'un parc

get_live_details("onogE5uepoQ")
# key = set_keyword()
# get_video_comments("onogE5uepoQ", keyword=key)


