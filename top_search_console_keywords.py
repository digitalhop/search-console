#This file is used to extract your top keywords from search console
from date_functions import date_plus_day, get_todays_date, date_plus_month
from googleapiclient.errors import HttpError
from time import sleep
import pandas as pd

#import the google connection
from google_auth import google_connector

#You'll need to enter in your own Search Console verified website here
SITE_URL = 'https://digitalhop.co.uk'

#enter the start date and end date that you want to get the keywords from
#By default we will search about 16 months of data on search console
#you can search for a shorter time by replacing the start_date with your own start date e.g. '2019-10-01'
start_date = date_plus_month(get_todays_date(), -16)
end_date = date_plus_day(get_todays_date(), -1)
print(f'The start date: {start_date}')
print(f'The end date: {end_date}')

#how many keywords to do you want. Can be up to 25000
row_limit = 25000

#how many clicks above over the time period
#A click represents someone who searched with a keyword nd clicked on your link in the SERPS
#By default this is set to 10, the more clicks required, the less keywords will qualify
#If you set this too low, you might get too many keywords
#the goal should be to get your best performing keywords

click_limit = 10

#this sets the filters in the body for search console
#we are basically getting the top 999 search queries
def get_search_console_data(the_start_date,the_end_date, the_row_limit=row_limit):
	body = {"startDate":the_start_date,
			"endDate": the_end_date,
			"dimensions":["query"],
			"searchType":"web",
			"rowLimit": the_row_limit}
	return body

#add dimensions to the_body
the_body = get_search_console_data(start_date,end_date)

#build the webmaster service
webmasters_service = google_connector()

#query the data from search console and use a exception tester
#data gets added to the gsc_data variable, which we can then extract
#the data from it
while True:
	try:
		print("fetching data from search console")
		gsc_data = webmasters_service.searchanalytics().query(siteUrl=SITE_URL, body=the_body).execute()
	except HttpError as err:
	# If the error is a rate limit or connection error,
	# wait and try again.
		if err.resp.status in [403, 500, 503, 429]:
			print(f"recieved error: {err.resp.status} from google, waiting to try again")
			sleep(5)
			continue
		else: 
			print("came across an error that is not known yet")
			exit()
	break

#create a list for the search console keywords we queried
search_console_list_of_keywords = []
number_count = 1

#create the pandas dataframe
column_names = ["Keyword", "CTR", "Clicks"]
df = pd.DataFrame(columns = column_names)
#get the keywords and check if they are above 1 impressions
if 'rows' in gsc_data:
	for metric in gsc_data["rows"]:
		if metric['clicks'] >click_limit:
			#print(f"number {str(number_count)} for {metric['keys'][0]} with {str(metric['ctr'])} CTR")
			keyword = metric['keys'][0]
			CTR = metric['ctr']
			clicks = metric['clicks']
			if keyword not in search_console_list_of_keywords:
				search_console_list_of_keywords.append(keyword)
				#add to pandas dataframe
				df2 = pd.DataFrame([[keyword,CTR,clicks]],columns = column_names)
				df = df.append(df2)
			number_count += 1
else:
	print('No data found')

print(f'The amount of keywords is: {len(search_console_list_of_keywords)}')

#create the csv file with the keywords, CTR's and Clicks
df.to_csv(r'Data\\keywords\\top-keywords.csv', index = False)