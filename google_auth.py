from google_auth_oauthlib.flow import InstalledAppFlow
from apiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import pickle
from time import sleep

#this is used to do the Google Authentication for the search console app
#first time file runs it sets the Google verification code in a pickle file
#lists out the verified domains of a Google user

# Read more: https://developers.google.com/webmaster-tools/search-console-api-original/v3/
OAUTH_SCOPE = ('https://www.googleapis.com/auth/webmasters.readonly', 'https://www.googleapis.com/auth/webmasters')

def google_connector(the_scopes=OAUTH_SCOPE):
    """this is the authorisation that checks your client id and client secret
    in your config folder. It also does the login to Google to verify and then stores
    the verification in a pickle file in the config folder"""
    try:
        credentials = pickle.load(open("config/credentials.pickle", "rb"))
    except (OSError, IOError) as e:
        flow = InstalledAppFlow.from_client_secrets_file('config/client_secret.json', scopes=OAUTH_SCOPE)
        credentials = flow.run_console()
        pickle.dump(credentials, open("config/credentials.pickle", "wb"))
    webmasters_service = build('webmasters', 'v3', credentials=credentials)
    return webmasters_service