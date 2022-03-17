import csv
from fileinput import filename
from datetime import datetime, timedelta
from time import time, sleep

#block for checking out dated users from CSV
def lastTimeCheck():
  with open('users.csv', newline='') as csvfile:
    nowTime = datetime.now()
    lastSixHours = datetime.now() - timedelta(hours = 6)
    data = csv.DictReader(csvfile)
    for row in data:
      if row['Last_Functionally_Updated'] <= str(lastSixHours) and row['Employee_Status'] == 'Suspended':
        print(row['Last_Functionally_Updated'] + " "+ row['Employee_Status'] + " " + row['Email_Address'])



lastTimeCheck()
print("************************")
