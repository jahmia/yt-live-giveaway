# coding utf-8
import requests
import login

from urllib.parse import urlparse

youtube = None

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

def get_video_comments(video_id):
    request = youtube.videos().list(
        part='contentDetails,statistics',
        id=video_id
    )
    response = request.execute()
    content = response.get('items', [])
    comment_count = content[0]['statistics']['commentCount'] if content and content[0] else 0
    print(f'Comment count: {comment_count}')
    return comment_count

def get_video_comments(video_id):
    # TODO: Also check comments for live video
    # Thes comments should be ordered by time
    comments = None

    request = youtube.videos().list(
        part='contentDetails,statistics',
        id=video_id
    )
    response = request.execute()
    content = response.get('items', [])
    comments = content[0][''][''] if content and content[0] else 0

    return comments

youtube = youtube_oauth.connect()
# link = set_unlisted_stream()
total_comment = get_video_comments("vQQEaSnQ_bs")
key = set_keyword()
