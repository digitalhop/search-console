#This file is used to check which sites are registered to the Google account

#import the google connection
from google_auth import google_connector

#build the webmaster service
webmasters_service = google_connector()

# Retrieve list of properties in account
site_list = webmasters_service.sites().list().execute()

# Filter for verified websites
verified_sites_urls = [s['siteUrl'] for s in site_list['siteEntry']
                       if s['permissionLevel'] != 'siteUnverifiedUser']

# Print the URLs of all websites you are verified for.
if len(verified_sites_urls) >0:
    print('The sites you are verified for are:')
    for site_url in verified_sites_urls:
        print (site_url)
else:
    print('There are no sites verified for your Google account')