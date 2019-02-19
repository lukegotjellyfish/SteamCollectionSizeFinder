from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from decimal import Decimal
from lxml import html
import requests
import fnmatch

sizes = []
input_url = []
with open("Collections.txt") as url_file:
    for line in url_file:
        input_url.append(line)

for i in range(0, len(input_url)):
    req = Request(input_url[i])
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    links = []
    x = 2

    for link in soup.findAll('a', class_=False, href=True, target=False):  #get links and filter out unwanted class and target html
        if x%2 == 0:
            links.append(str(link.get('href')))
        x += 1
        
    links = fnmatch.filter(links, 'https://steamcommunity.com/sharedfiles/filedetails/?id=*')
    print("Addon Count: " + str(len(links)) + "\n")


    #go through each mod in collection to get filesize
    x = 1
    link_bank = []
    total_size = 0

    if (len(links) > 100):
        spacer = " "  #Make the output look more... a e s t h e t i c
    else:
        spacer = "" 

    for i in links:
        url = i

        try:
            if link_bank.index(url):
                continue  #ignore duplicate link (if this somehow happens, just in case)

        except:
            link_bank.append(str(i))  #add to list of unique links
            #at least it works
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            file_size = tree.xpath('//div[@class="detailsStatRight"]/text()')
            file_size = (file_size[0])[:-3].replace(",", "")
        except:
            try:
                page = requests.get(url)
                tree = html.fromstring(page.content)
                file_size = tree.xpath('//div[@class="detailsStatRight"]/text()')
            except:
                try:
                    page = requests.get(url)
                    tree = html.fromstring(page.content)
                    file_size = tree.xpath('//div[@class="detailsStatRight"]/text()')
                except:
                    continue  #oof
    

        try:
            total_size += Decimal(file_size)
        except:
            continue
        
        if x < 10:
            print(" " + spacer + str(x) + "| Running total = " + str(total_size))
        elif x < 100:
            print(spacer + str(x) + "| Running total = " + str(total_size))
        else:
            print(str(x) + "| Running total = " + str(total_size))
        x += 1
    
    sizes.append(total_size)
    print("\nTotal = " + '{:,}'.format(total_size) + " MB")
    print("\n\n\n\n\n\n\n\n\n")

print("Collection sizes in written order:\n" + str(sizes).strip())
print("\nTotal size of all collections: " + '{:,}'.format((sum(sizes))))

while True:
    x = input("Paused")
