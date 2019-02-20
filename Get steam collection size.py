from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from decimal import Decimal
from lxml import html
import requests
import fnmatch

def add_another(input_url, addon_count, mode, spacer):
    with open("log.txt", "a", encoding='utf8') as log_append:
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
            spacer = "       "  #Make the output look more... a e s t h e t i c
        elif len_links >= 10:
            spacer = "      "
        else:
            spacer = "     "

        if mode == 2:
            spacer += "    "
            print(spacer + "===On sub-sub-collection===")
        else:
            print(spacer + "===On sub-collection===")

        if len_links >= 100:
            log = spacer + "Collection Item Count: " + str(len_links)
            print(log)
            log_append.write(log + "\n")
        elif len_links >= 10:
            log = spacer + "Collection Item Count: " + str(len_links)
            print(log)
            log_append.write(log + "\n")
        else:
            log = spacer + "Collection Item Count: " + str(len_links)
            print(log)
            log_append.write(log + "\n")



        #go through each mod in collection to get filesize
        x = 1
        link_bank = []
        total_size = 0

        for i in links:
            url = i

            try:
                if link_bank.index(url):
                    log = "Duplicate link: " + str(url)
                    print(log)
                    log_append.write(log + "\n")
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
                    details = add_another(url, addon_count, 2, spacer)
                    total_size += details[0]
                    addon_count = details[1]
                    continue

            if x < 10:
                log = " " + spacer + str(x) + "| Running total = " + str(total_size)
                print(log)
                log_append.write(log + "\n")
            elif x < 100:
                log = spacer + str(x) + "| Running total = " + str(total_size)
                print(log)
                log_append.write(log + "\n")
            else:
                log = spacer + str(x) + "| Running total = " + str(total_size)
                print(log)
                log_append.write(log + "\n")

            x += 1
        return [total_size, addon_count - 1]  #-1 to de-count each collection








sizes = []
input_url = []
addon_count = 0
with open("Collections.txt", "r", encoding='utf8') as url_file:
    for line in url_file:
        input_url.append(line)
with open("log.txt", "w", encoding='utf8') as log_write:
    for i in range(0, len(input_url)):
        req = Request(input_url[i])
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")

        links = []
        for link in soup.findAll('a', class_=False, href=True, target=False):  #get links and filter out unwanted class and target html
            links.append(str(link.get('href')))

        links = fnmatch.filter(links, 'https://steamcommunity.com/sharedfiles/filedetails/?id=*')
        links = list(dict.fromkeys(links))
        len_links = len(links)
        addon_count += len_links

        if len_links >= 100:
            spacer = " "  #Make the output look more... a e s t h e t i c
        else:
            spacer = ""


        log = "Collection Item Count: " + str(len_links)
        print(log)
        log_write.write(log + "\n")


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
                    details = add_another(url, addon_count, 1, spacer)
                    total_size += details[0]
                    addon_count = details[1]
                    continue

            if x < 10:
                log = " " + spacer + str(x) + "| Running total = " + str(total_size)
                print(log)
                log_write.write(log + "\n")
            elif x < 100:
                log = spacer + str(x) + "| Running total = " + str(total_size)
                print(log)
                log_write.write(log + "\n")
            else:
                log = str(x) + "| Running total = " + str(total_size)
                print(log)
                log_write.write(log + "\n")

            x += 1

        sizes.append(total_size)                                                                            
        log = "\nTotal for this collection = " + '{:,}'.format(total_size) + " MB\n\n╔══════════════╗\n║   Finished   ║\n╚══════════════╝\n"
        print(log)
        log_write.write(log + "\n")
        total_size = 0

print("Collection sizes in written order:\n")
for x in sizes:
    print('{:,}'.format(x))

print("\nTotal size of all collections: " + '{:,}'.format((sum(sizes))) + " MB")
print("\nTotal number of addons: " + str(addon_count))
x = input("Press ENTER to EXIT")
