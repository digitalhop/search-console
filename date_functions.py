#This file deals hosts the various date functions used to sort and select dates
import pandas as pd
from datetime import date, datetime, timedelta

#get todays date
def get_todays_date():
	today = date.today()
	return today

#takes in a date and adds an amount of days to it
def date_plus_day(the_date, days_to_add):
	new_date = pd.to_datetime(the_date) + pd.DateOffset(days=days_to_add)
	return str(new_date)[0:10]
	
#add x amount of months to a date
def date_plus_month(the_date, months_to_add):
	new_date = pd.to_datetime(the_date) + pd.DateOffset(months=months_to_add)
	return str(new_date)[0:10]

#find the first and last date in a list of dates
#returns a list with the first[0] and last date[1]
def find_the_last_date(date_list):
	#create a panda data frame with a list of dates
	df = pd.DataFrame({'Date':date_list})
	first_and_last_date = []
	first_and_last_date.append(df['Date'].min())
	first_and_last_date.append(df['Date'].max())
	return first_and_last_date