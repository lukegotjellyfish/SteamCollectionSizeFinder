from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from decimal import Decimal
from lxml import html
import requests
import fnmatch

def add_another(input_url):
    req = Request(input_url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a', class_=False, href=True, target=False):  #get links and filter out unwanted class and target html
        links.append(str(link.get('href')))
        
    links = fnmatch.filter(links, 'https://steamcommunity.com/sharedfiles/filedetails/?id=*')
    links = list(dict.fromkeys(links))

    len_links = len(links)
    if len_links >= 100:
        spacer = "    "  #Make the output look more... a e s t h e t i c
    else:
        spacer = "   "

    if len_links >= 100:
        print("\n   Collection Addon Count: " + str(len_links))
    elif len_links >= 10:
        print("\n  Collection Addon Count: " + str(len_links))
    else:
        print("\n Collection Addon Count: " + str(len_links))


        
    #go through each mod in collection to get filesize
    x = 1
    link_bank = []
    total_size = 0

    for i in links:
        url = i

        try:
            if link_bank.index(url):
                print("Duplicate link: " + str(url))
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
            if file_size == "Unique Visit":
                total_size += add_another(url)  # this is a collection on the collection
                continue

        if x < 10:
            print(" " + spacer + str(x) + "| Running total = " + str(total_size))
        elif x < 100:
            print(spacer + str(x) + "| Running total = " + str(total_size))
        else:
            print(str(x) + "| Running total = " + str(total_size))
        x += 1
    print()
    return total_size




    





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
    for link in soup.findAll('a', class_=False, href=True, target=False):  #get links and filter out unwanted class and target html
        links.append(str(link.get('href')))
        
    links = fnmatch.filter(links, 'https://steamcommunity.com/sharedfiles/filedetails/?id=*')
    links = list(dict.fromkeys(links))


    if (len(links) >= 100):
        spacer = " "  #Make the output look more... a e s t h e t i c
    else:
        spacer = ""

    print("\n" + spacer + "Collection Addon Count: " + str(len(links)))



    #go through each mod in collection to get filesize
    x = 1
    link_bank = []
    total_size = 0

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
            if file_size == "Unique Visit":
                total_size += add_another(url)

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

print("Collection sizes in written order:\n")
for x in sizes:
    print(x)

print("\nTotal size of all collections: " + '{:,}'.format((sum(sizes))) + " MB")

while True:
    x = input("Paused")
