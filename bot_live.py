# coding utf-8
import json
# import requests
import time

from urllib.parse import urlparse

import youtube_oauth

YOUTUBE = None
comments = []

def is_structurally_valid_url(url_string):
    try:
        result = urlparse(url_string)
        return all([result.netloc, result.path])
    except ValueError:
        return False

def set_unlisted_stream(stream=None):
    if not stream:
        stream = input("Enter the stream link (in form youtu.be/videoID): ")
        if not is_structurally_valid_url("http://youtu.be/" + stream):
            print("The link is not valid. Please enter a valid URL.")
            return set_unlisted_stream()
        if stream and not stream.startswith("http://youtu.be/"):
            return set_unlisted_stream()
        if not stream:
            print("The video will be a default to a live channel.")
            # Default test link
            stream = "l8PMl7tUDIE"
    return stream

def set_keyword():
    keyword = input("Enter keyword to monitor : ")
    return keyword

def get_participants():
    pass

def get_live_details(video_id):
    request = YOUTUBE.videos().list(
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
    print("\nHere is some details about the YOUTUBE video.")
    print(json.dumps(res, indent=4))
    if 'liveBroadcastContent' in res and res['liveBroadcastContent'] != 'live':
        print("The video is not live currently. Aborting")
        exit(0)
    return content


def get_live_chats(chat_id, keyword):
    page_token = ""
    content = []
    while page_token is not None:
        request = YOUTUBE.liveChatMessages().list(
            liveChatId=chat_id,
            part='snippet,authorDetails',
            maxResults=200,
            pageToken=page_token,
        )

        response = request.execute()
        if response.pop('items', []):
            content.append(response['items'])
        print(json.dumps(response, indent=4))

        wait_time = int(response.get('pollingIntervalMillis', 0)) / 1000
        wait_polling(wait_time)

        if page_token != response['nextPageToken']:
            page_token = response.get('nextPageToken', None)
        else:
            page_token = None

    print(json.dumps(content, indent=4))
    print(len(content))
    return 0

def wait_polling(seconds):
    if seconds == 0:
        return
    print(f"Waiting for {seconds} seconds before fetching new messages...")
    time.sleep(seconds)

if __name__ == "__main__":
    YOUTUBE = youtube_oauth.connect()
    YOUTUBE = youtube_oauth.connect_by_api_key()

    videoId = set_unlisted_stream()
    live = get_live_details(videoId)
    key = set_keyword()
    liveChatId = live.get('liveStreamingDetails', {}).get('activeLiveChatId')
    get_live_chats(liveChatId, keyword=key)
