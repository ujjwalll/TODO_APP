# In order to connect it to your emails so that a timely reminder comes to the user, we 
# need to use the API's as specified in the task, So one of the solution is to either host it
# or you can connect it to your google API account. 
# I have connected it to the google API account, For more info please see description of github 
# repository
# This file contains the code which is being used to write data to the google sheets

import forms
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('upgrad.json', scope)
client = gspread.authorize(creds)

sheet = client.open('upgrad').sheet1

a=form.text
a_split = a_split(';')

for i in range(100000):
	row = [a_split(0), a_split(1)]

