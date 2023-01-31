pip install gspread oauth2client df2gspread

#Importing the module
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

#The scope is always look like this so we did not need to change anything
scope = [
   'https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
#Name of our Service Account Key
google_key_file = 'service_key.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(google_key_file, scope)
gc = gspread.authorize(credentials)

pip install pmaw pandas

import pandas as pd
from pmaw import PushshiftAPI
api = PushshiftAPI()

import datetime as dt
before = int(dt.datetime(2022,6,1,0,0).timestamp())
after = int(dt.datetime(2022,4,30,0,0).timestamp())

#Here is where you would enter the subreddit name and maximum number of comments you wish to pull. I would avoid going over 1000 (if possible)as there are limits to PushShift API.
subreddit="Test"
limit=1000
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before, after=after)
print(f'Retrieved {len(comments)} comments from Pushshift')

comments_df = pd.DataFrame(comments)
# preview the comments data
comments_df.head(1000)

#This is the Worksheet ID
spreadsheet_key = '1test'
#This is the sheet name
wks_name = 'test'
#We upload the tips data to our Google Sheet. Setting the row_names to False if you did not want the index to be included
d2g.upload(comments_df, spreadsheet_key, wks_name, credentials=credentials, row_names=True)
