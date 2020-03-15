from google_auth_oauthlib.flow import InstalledAppFlow
from apiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import pickle


def google_connector(the_scopes='https://www.googleapis.com/auth/webmasters.readonly'):
    """this is the authorisation that checks your client id and client secret
    in your config folder. It also does the login to Google to verify and then stores
    the verification in a pickle file in the config folder"""
    try:
        credentials = pickle.load(open("config/credentials.pickle", "rb"))
    except (OSError, IOError) as e:
        flow = InstalledAppFlow.from_client_secrets_file('config/client_secret.json', scopes=the_scopes)
        credentials = flow.run_console()
        pickle.dump(credentials, open("config/credentials.pickle", "wb"))
    webmasters_service = build('webmasters', 'v3', credentials=credentials)
    return webmasters_service

#build the webmaster service
webmasters_service = google_connector()

# Retrieve list of properties in account
site_list = webmasters_service.sites().list().execute()

# Filter for verified websites
verified_sites_urls = [s['siteUrl'] for s in site_list['siteEntry']
                       if s['permissionLevel'] != 'siteUnverifiedUser']

# Print the URLs of all websites you are verified for.
for site_url in verified_sites_urls:
    print (site_url)