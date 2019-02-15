from urllib.request import urlopen
from bs4 import BeautifulSoup
from decimal import Decimal
import fnmatch
import time

url = "https://steamcommunity.com/sharedfiles/filedetails/?id=1645890656"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

#get all links in collection
for script in soup(["script", "style"]):
    script.extract()

text =[]
x=2

for link in soup.find_all('a'):
    if x%2 == 0:  #links we want are inbetween mod author's link...or something i can't remember
        text.append(str(link.get('href'))) #append to text to filter out bad links
    x+=1

new_text = fnmatch.filter(text, 'https://steamcommunity.com/sharedfiles/filedetails/?id=*')  #if link matches workshop item url
del(new_text[0])  #first link is the page itself
print("Mod links:\n" + '\n'.join(new_text))



#go through each mod in collection to get filesize
x = 1
total_size = 0
if (len(new_text) > 100):
    spacer = " "  #Make the output look more... a e s t h e t i c
else:
    spacer = ""
    
print("")
for i in new_text:
    url = str(i)

    #at least it works
    try:
        html = urlopen(url).read()
    except:
        try:
            html = urlopen(url).read()
        except:
            try:
                html = urlopen(url).read()
            except:
                try:
                    html = urlopen(url).read()
                except:
                    try:
                        html = urlopen(url).read()
                    except:
                        try:
                            html = urlopen(url).read()
                        except:
                            html = urlopen(url).read()

    soup = BeautifulSoup(html, features="html.parser")
    text = (soup.select('.detailsStatRight')[0].text.strip()).replace(" MB", "").replace(",","")

    try:
        total_size += Decimal(text)
    except:
        print("Tried to add a value that wasn't the filesize, oops")

    if x < 10:
        print(" " + spacer + str(x) + "| Running total = " + str(total_size))
    else:
        print("" + spacer + str(x) + "| Running total = " + str(total_size))
    x += 1
    
print("Total = " + str(total_size))
halt = input('"Paused"')
