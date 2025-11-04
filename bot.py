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

def set_unlisted_stream():
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

link = set_unlisted_stream()
key = set_keyword()
