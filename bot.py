# coding utf-8
import requests

from urllib.parse import urlparse
from . import login

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


def get_video_comments(video_id)
    request = youtube.videos().list(
        part='contentDetails,statistics',
        id=video_id
    )

    # request = youtube.playlistItems().list(
    #     part='status',
    #     playlistId='PLQYbfmTsxXjCGZVtWlzOW3JKuVkqy_UMU'
    # )

    response = request.execute()

    content = response.get('items', [])
    comment_count = content[0]['statistics']['commentCount'] if content and content[0] else 0
    print(f'Comment count: {comment_count}')



link = set_unlisted_stream("vQQEaSnQ_bs")
key = set_keyword()
