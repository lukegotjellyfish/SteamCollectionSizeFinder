from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from decimal import Decimal
from lxml import html
from datetime import datetime
import os
import requests
import fnmatch


def write_log(log):  #Show information, log information with timestamp
    print(log)  #Output information
    i = datetime.now()  #Fetch datetime
    with open("log.txt", "a", encoding='utf8') as log_write:
        log_write.write("[" + i.strftime('%Y/%m/%d %H:%M:%S') + "]" + " || " + log + "\n")  #Write date then UI output to log


def add_another(input_url, addon_count, mode, spacer):  #On new collection, "add another" instance
    try:
        req = Request(input_url)
    except:
        return [0, addon_count - 1]
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")  #Parse html with lxml

    links = []
    for link in soup.findAll('a', class_=False, href=True, target=False):  #get links and filter out unwanted class and target html
        links.append(str(link.get('href')))  #Includes other collection links (and those in the description)

    links = fnmatch.filter(links, 'https://steamcommunity.com/sharedfiles/filedetails/?id=*')
    links = list(dict.fromkeys(links))  #Order links

    addon_count += len(links)  #Addon count

    len_links = len(links)  #Number of actuyal addons
    spacer = " "  #Make the output easier to read

    if mode == 1:
        print("==On New Collection===")
    elif mode == 2:
        spacer += " "
        print(spacer + "===On sub-collection===")
    else:
        print(spacer + "===On sub-sub-collection===")

    write_log(spacer + "╔Collection Item Count: " + str(len_links))
    #Go through each addon in collection to get filesize
    x = 1
    link_bank = []
    total_size = 0
    leading_zero = "{:02d}".format(len(str(len_links))+1)
    leading_zero = "{:" + leading_zero + "d}"  #To use to format current addon number in output

    for url in links: #ends with err on collec
        try:
            if link_bank.index(url):
                write_log("     Duplicate link: " + str(url))
                continue  #ignore duplicate link (if this somehow happens, just in case)
        except:
            link_bank.append(str(url))  #add to list of unique links

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
            if (file_size == "Unique Visit"):  # Is a collection
                details = add_another(url, addon_count, 2, spacer + "  ")
                total_size += details[0]
                addon_count = details[1]
                continue
        write_log(spacer + "║" + leading_zero.format(x) + "║ Running total = " + "{:,}".format(total_size) + " MB" + "|" + url)
        x += 1
    print(" ╚═══════════════════════════════════════")

    return [total_size, addon_count - 1]  # - 1 to remove collections counted


##START##
if (os.path.exists("log.txt")):
	os.remove("log.txt")  #Delete existing log

sizes = []
input_url = []
addon_count = 0
with open("Collections.txt", "r", encoding='utf8') as url_file:
    for line in url_file:
        collection_det = add_another(line, 0, 1, "")
        sizes.append(collection_det[0])
        addon_count += collection_det[1]
        print()

write_log("Collection sizes in stored order (collections.txt):")
print()
num = 1
for x in sizes:
    write_log(str(num) + ": " + '{:,}'.format(x) + " MB")
    num += 1

print()
write_log("Total size of all collections: " + '{:,}'.format((sum(sizes))) + " MB")
write_log("Total number of addons: " + str(addon_count))
i = datetime.now()
write_log("Taken at " + i.strftime('%Y/%m/%d %H:%M:%S'))
print("\n\n")
write_log("Press ENTER to EXIT")
input()