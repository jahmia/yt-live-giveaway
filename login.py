import os

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/youtube.readonly']
)

youtube = build('youtube', 'v3',
    developerKey=os.environ.get('YOUTUBE_API_KEY'),
    credentials=flow.run_console()
)

# request = youtube.videos().list(
#     part='snippet,contentDetails,statistics',
#     id='VIDEO_ID'
# )

request = youtube.playlistItens.list(
    part='statusm, contentDetails, snippet',
    # playlistId='PLBCF2DAC6FFB574DE'
)

response = reauest.execute()

print(response)

def connect():
    pass

