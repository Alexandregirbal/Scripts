import requests
import json
from datetime import datetime
import time
from bs4 import BeautifulSoup
print('Lauching python script...')

def fetchData():
  # print('Fetching new data ('+str(datetime.now().time()) + ')')
  url = 'https://selt.languagecert.org/api/selt/schedule'
  body = {"tcId":370531,"scheduler":[{"allocationId":0,"basketItemId":0,"assemblyId":2722,"voucherCode":"","ReserveTimeBefore":0,"ReserveTimeAfter":0,"JSON":""},{"allocationId":0,"basketItemId":0,"assemblyId":2714,"voucherCode":"","ReserveTimeBefore":0,"ReserveTimeAfter":0,"JSON":""}]}
  headers = {
    'accept': 'application/json, text/plain, /',
    'content-type': 'application/json;charset=UTF-8',
  }

  x = requests.post(url,json=body, headers=headers)
  if x.status_code == 200:
    # print('Request status: 200')
    parsed = json.loads(x.content)
    data = parsed['scheduler'][0]['JSON']['Days']
    # print(json.dumps(data, indent=4, sort_keys=True))
    return data
  else: 
    print('An error occured (code ' + str(x.status_code) + ')')

def keepAvailableDays(data):
  availableData = list(filter(lambda day: day['Enabled'], data))
  return availableData[0]['Day']

def generateDelay(interval, unit):
  if unit == 'sec':
    return interval
  if unit == 'min':
    return interval * 60
  if unit == 'hour':
    return interval * 3600

# PARAMS
_interval = 10
_unit = 'sec'
# INIT
count = 0
firstAvailableDay = 'None'
delay = generateDelay(_interval,_unit)
# INFINITE LOOP
while(True):
    tmp = keepAvailableDays(fetchData())
    if tmp != firstAvailableDay:
      print('The first available day changed from ' + firstAvailableDay + ' to ' + tmp)
      firstAvailableDay = tmp
      #sendEmail(emailAdresses,subject, message)
    print(str(count) + ' ('+ str(datetime.now().time()) +'):  ' + firstAvailableDay + '\n')
    count += 1
    time.sleep(delay)