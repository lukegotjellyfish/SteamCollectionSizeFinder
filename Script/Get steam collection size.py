from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from decimal import Decimal
from lxml import html
from datetime import datetime
import os
import requests
import fnmatch


def add_another(input_url, addon_count, mode, spacer):
    req = Request(input_url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a', class_=False, href=True, target=False):  #get links and filter out unwanted class and target html
        links.append(str(link.get('href')))

    links = fnmatch.filter(links, 'https://steamcommunity.com/sharedfiles/filedetails/?id=*')
    links = list(dict.fromkeys(links))

    addon_count += len(links)

    len_links = len(links)
    if len_links >= 100:
        spacer = " "  #Make the output look more... a e s t h e t i c
    else:
        spacer = ""

    if mode == 1:
        print("==On New Collection===")
    elif mode == 2:
        spacer += "    "
        print(spacer + "    ===On sub-sub-collection===")
    else:
        print(spacer + "    ===On sub-collection===")

    if len_links >= 100:
        log = spacer + "   Collection Item Count: " + str(len_links)
    elif len_links >= 10:
        log = spacer + "    Collection Item Count: " + str(len_links)
    else:
        log = spacer + "     Collection Item Count: " + str(len_links)

    print(log)
    i = datetime.now()
    with open("log.txt", "a", encoding='utf8') as log_write:
        log_write.write(i.strftime('%Y/%m/%d %H:%M:%S') + " || " + log + "\n")


    #go through each mod in collection to get filesize
    x = 1
    link_bank = []
    total_size = 0

    for i in links:
        url = i

        try:
            if link_bank.index(url):
                log = "     Duplicate link: " + str(url)
                print(log)
                i = datetime.now()
                with open("log.txt", "a", encoding='utf8') as log_write:
                    log_write.write(i.strftime('%Y/%m/%d %H:%M:%S') + " || " + log + "\n")
                continue  #ignore duplicate link (if this somehow happens, just in case)

        except:
            link_bank.append(str(i))  #add to list of unique links
            #at least it works

        while True:
            try:
                page = requests.get(url)
                tree = html.fromstring(page.content)
                file_size = tree.xpath('//div[@class="detailsStatRight"]/text()')
                file_size = (file_size[0])[:-3].replace(",", "")
                break
            except: continue



        try:
            total_size += Decimal(file_size)
        except:
            if file_size == "Unique Visit":  # Is a collection
                details = add_another(url, addon_count, 2, spacer + "  ")
                total_size += details[0]
                addon_count = details[1]
                continue

        if x < 10:
            log = "     " + spacer + str(x) + "| Running total = " + str(total_size)
        elif x < 100:
            log = "     " + spacer + str(x) + "| Running total = " + str(total_size)
        else:
            log = "     " + spacer + str(x) + "| Running total = " + str(total_size)

        print(log)
        i = datetime.now()
        with open("log.txt", "a", encoding='utf8') as log_write:
            log_write.write(i.strftime('%Y/%m/%d %H:%M:%S') + " || " + log + "\n")
        x += 1
    return [total_size, addon_count - 1]  # - 1 to remove collections counted


if os.path.exists("log.txt"):
	os.remove("log.txt")

sizes = []
input_url = []
addon_count = 0
with open("Collections.txt", "r", encoding='utf8') as url_file:
    for line in url_file:
        collection_det = add_another(line, 0, 1, "")
        sizes.append(collection_det[0])
        addon_count += collection_det[1]
        print()

print("Collection sizes in written order:\n")
num = 1
for x in sizes:
    print(str(num) + ": " + '{:,}'.format(x) + " MB")
    num += 1
i = datetime.now()

print("\nTotal size of all collections: " + '{:,}'.format((sum(sizes))) + " MB")
print("Total number of addons: " + str(addon_count))
print("Taken at " + i.strftime('%Y/%m/%d %H:%M:%S'))
x = input("\n\nPress ENTER to EXIT")
