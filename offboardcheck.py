import csv
#import json
import os
#from requests.auth import HTTPBasicAuth
#import requests
from datetime import datetime, timedelta, date
from time import time, sleep
#from fileinput import filename

""" api_url = requests.get("API URL") = {
    "Accept": "application/json",
    "Content-Type": "application/json"
} """


#os.system("#script to get CSV UTF-8")

def lastDateCheck():
    with open('users.csv', newline='') as csvfile:
        #nowTime = datetime.now()
        lastSixHours = datetime.now() - timedelta(hours = 48)
        yesterdayDate = date.today() - timedelta(days = 2)
        data = csv.DictReader(csvfile)
        #terminated_emails = []
        for row in data:
              if row['Employee_Status'] == 'Suspended' and row['Date_of_Last_Change'] >= str(yesterdayDate):
              #if row['CF_EE_Worker_Suspended_Date'] > str(lastSixHours) and row['Employee_Status'] == 'Suspended':
              #if row['Employee_Status'] == 'Suspended':
                print(row['Date_of_Last_Change'] + " " + row['Employee_Status'] + " " + row['Email_Address'])
                #print(row['Legal_Name'] + " " + row['Employee_Status'] + " " + row['Email_Address'])
                #terminated_emails.append(row['Email_Address'])
                #print(row['CF_EE_Worker_Suspended_Date'])
        #print(terminated_emails)

def main():
    lastDateCheck()

if __name__ == '__main__':
    main()
