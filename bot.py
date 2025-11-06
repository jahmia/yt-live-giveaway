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

def is_reachable_url(url_string):
    try:
        response = requests.head(url_string, timeout=5)
        return 200 <= response.status_code < 400
    except requests.exceptions.RequestException:
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

def get_video_details(video_id):
    request = youtube.videos().list(
        part='snippet,statistics,liveStreamingDetails',
        id=video_id
    )
    response = request.execute()
    content = response.get('items', [])
    content = content[0] if content else []

    res = {
        'id': content.get('id'),
        'title': content['snippet']['title'],
        'channelTitle': content['snippet']['channelTitle'],
        'liveBroadcastContent': content['snippet']['liveBroadcastContent'],
        'commentCount': int(content.get('statistics')['commentCount'])
    }
    print("\nHere is some details about the youtube video.")
    print(json.dumps(res, indent=4))
    return res

def get_video_comments(video_id, keyword):
    # TODO: Also check comments for live video
    next_page = 'first'
    while next_page:
        if next_page == 'first':
            next_page = None

        # https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails
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

youtube = build(
    'youtube', 'v3',
    developerKey="AIzaSyBB9KR0avf3MJ3njd56raMUpjTOor9dqvo",
)

# link = set_unlisted_stream()
# mekOjGBYeoQ    UCI
# vQQEaSnQ_bs    Python Youtube API
# TEuRjhhYkvA     Outlier Odoo - Gestion d'un parc

get_video_details("vQQEaSnQ_bs")
key = set_keyword()
get_video_comments("vQQEaSnQ_bs", keyword=key)


