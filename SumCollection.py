from urllib.request import urlopen
from bs4 import BeautifulSoup
from decimal import Decimal
import fnmatch
import time

while True:
    url = input("Enter steam collection URL:\n- ")
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
    print("\nMod links:\n" + '\n'.join(new_text))



    #go through each mod in collection to get filesize
    x = 1
    link_bank = []
    total_size = 0
    if (len(new_text) > 100):
        spacer = " "  #Make the output look more... a e s t h e t i c
    else:
        spacer = "" 
    print("")

    for i in new_text:
        url = str(i)
        try:
            if link_bank.index(url):
                continue  #ignore duplicate link
        except:
            link_bank.append(str(i))  #add to list of unique links
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
                break #this is trying to add a colection... no thx skip
            if x < 10:
                print(" " + spacer + str(x) + "| Running total = " + str(total_size))
            elif x < 100:
                print(spacer + str(x) + "| Running total = " + str(total_size))
            else:
                print(str(x) + "| Running total = " + str(total_size))

            x += 1
        
    print("\nTotal = " + str(total_size))
    halt = input('"Paused" press ENTER to continue...')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
