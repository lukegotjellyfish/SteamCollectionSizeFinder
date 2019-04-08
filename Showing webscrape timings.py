from lxml import html
from bs4 import BeautifulSoup
from urllib.request import urlopen
from decimal import Decimal
import requests
import time
import numpy as np


def timestart():
    global start
    start = time.time()
	

def timeend():
    global end
    end = time.time()
    TimeTaken = (end-start)  # This gets the seconds passed
    TimeTaken = round(TimeTaken, 3)
    return TimeTaken


time_array_1 = []
time_array_2 = []

for i in range(0, 100):
    timestart()
    
    page = requests.get('https://steamcommunity.com/sharedfiles/filedetails/?id=1593674891.html')
    tree = html.fromstring(page.content)
    file_size = tree.xpath('//div[@class="detailsStatRight"]/text()')
    file_size = (file_size[0])[:-3].replace(",", "")
    
    time_array_1.append(timeend())
    print("Request done")

print("\n")

for i in range(0, 100):
    timestart()

    html = urlopen('https://steamcommunity.com/sharedfiles/filedetails/?id=1593674891.html').read()
    soup = BeautifulSoup(html, features="html.parser")
    text = (soup.select('.detailsStatRight')[0].text.strip()).replace(" MB", "").replace(",","")
    
    time_array_2.append(timeend())
    print("BS4 done")
    
print("Average for request: " + str(np.mean(time_array_1)))
print("Total time for request: " + str(sum(time_array_1)))
print("Average for BS4: " + str(np.mean(time_array_2)))
print("Total time for BS4: " + str(sum(time_array_2)))
