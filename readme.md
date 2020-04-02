# Search Console API Analytics with Python

This project allows you to connect with Google Search Console API using Python. You will then be able to extract various types of data from Search Console that is just not really possible to get using the normal browser interface. For example using the API we would be able to extract all the keywords for any landing page that have seen any clicks or impressions over the last 18 months in an instant. We can also extract a CSV file with data for all our keywords to see which landing pages are recieving clicks for a particular keyword.

## Index
* Getting Started
* Extract your top performing keywords from Search Console
* Authors
* Acknowledgments

## Getting Started
To get up and running there are 3 Main steps. The instructions below will take you through the process. Much more detailed instructions with screengrabs can be found here:
https://digitalhop.co.uk/blog/how-to-connect-to-the-google-search-console-api-with-python/

1. Install the necesary Python modules
2. Set-up a Google Search Console API
3. Authenticate your Python app

### Prerequisites
Before you begin, you will need the domain you are interested in to be verified for your personal Google account in search console. You can find more information here: https://support.google.com/webmasters/topic/4564314. If you have used the domain property verification where you update your DNS records, then you might also need to do a URL prefix verification in Google search console. For example, I had to add my full URL **https://digitalhop.co.uk** as a domain property. So now I have both the **digitalhop.co.uk** and the **https://digitalhop.co.uk** properties verified.

1. Install the necesary Python modules
 - Clone this repository and add it to your local hard drive
 - Install the Python modules that you will need, which can be found in the 
   **requirements.txt** file in this repository. If you are in your command prompt terminal, navigate to the place where you saved this repository and run the following command to install all the required modules:
   '''$ pip install -r requirements.txt'''

   tip - You might want to use a virtual environment to keep these modules isolated from your main Python environment. Details of this can be found in the Achnowledgements section below.

2. Set-up a Google Search Console API
 - Follow this link to set-up your API https://console.developers.google.com/start/api?id=webmasters&credential=client_key
 - The Main Steps here are:
    - Create a Google API project
    - Configure an External OAUTH consent screen
    - Create your OAuth 2.0 client credentials
    - Download your json client secret file to the config folder in the repository you just cloned and rename it to **client_secret.json**

3. Authenticate your Python app
 - Run the **check_verified_sites.py** file
 - The terminal will print out a URL for you to visit to verify that you are accepting your new Python app to connect to your Google personal account
 - Copy the authentication code Google then gives you and paste it into the terminal
 - If Everything has worked, then the terminal will print out a list of the sites that are verified for you to access the search console data

## Extract your top performing keywords from Search Console
probably one of the best things about using the Search Console API will be that you can extract a lot of keywords used to find your website on Google. Currently this is up to about **25 000**. If you just used the browser to access Search Console, you would be able to get about 1000 keywords.

### Steps to extract top keywords as a CSV file
1. Open the **top_search_console_keywords.py** file in your Python interpreter e.g. VS Code/Genie etc
2. Change the **'SITE_URL'** variable (currently set to 'https://digitalhop.co.uk) to your verified URL (It must be a full URL with the http part)
3. Optional - Set the **start_date** and **end_date** to your own dates if you don't want to use the default 16 months. The longer the period, the more keywords.
4. Optional - Set the **row_limit** to an amount under 25000. You might not want to work with as many keywords as 25000, but you can always edit the csv file later.
5. Optional - Set the **click_limit** to an amount that works for you. If the click limit is higher, then you will only see keywords that had that many clicks or higher during that time period. If it is lower, then you might get a lot of keywords that are not relevant. 
6. Run the script. The CSV file with all your keywords will now be found in the keywords folder found in the data folder of your cloned directory. It is called **top-keywords.csv**


## Authors
**Jordan Dwyer - Digital Hop**

## Acknowledgments
A useful video if you are going to be setting up your own GitHub Repository is:
https://www.youtube.com/watch?v=9cMWR-EGFuY
By **Madness Labs**

If you are going to be setting up a virtual environment, I found this video rather helpful:
https://www.youtube.com/watch?v=APOPm01BVrk
By **Corey Schafer**

Thanks to https://github.com/trevorfox for the code of using pickle to assist with the Google authentication 