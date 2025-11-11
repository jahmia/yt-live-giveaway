import os
import pickle

from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
credentials = None


def get_credentials():
    # token.pickle stores the user's credentials from previously successful logins
    if os.path.exists('token.pickle'):
        print('Loading Credentials From File...')
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)


    '''
    If there are no valid credentials available,
    then either refresh the token or log in.
    '''
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            credentials.refresh(Request())
        else:
            print('Fetching New Tokens...')
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json',
                scopes=[
                    'https://www.googleapis.com/auth/youtube.readonly',
                    'https://www.googleapis.com/auth/youtube',
                    'https://www.googleapis.com/auth/youtube.force-ssl',
                ]
            )

            flow.run_local_server(port=8080, prompt='consent',
                                authorization_prompt_message='')
            credentials = flow.credentials

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as f:
                print('Saving Credentials for Future Use...')
                pickle.dump(credentials, f)

def connect():
    crendentials = get_credentials()
    youtube = build('youtube', 'v3', credentials=credentials)
    return youtube

def connect_by_api_key():
    load_dotenv()

    api_key = os.getenv('GOOGLE_API_KEY')

    if not api_key:
        print("API Key not found in .env file or environment variables.")
        exit(1)
    youtube = build('youtube', 'v3', developerKey=api_key)
    return youtube