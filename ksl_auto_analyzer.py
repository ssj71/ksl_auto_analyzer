#!/usr/bin/env python3
#spencer jackson 
#this script is to grab data to make a scatter plot of car listings for price vs mileage to help me understand the current market
import urllib.request
import re
import copy
import numpy
import matplotlib
import sys

#url = sys.argv[1]+"&page="
url = "https://cars.ksl.com/search/index?make[]=Nissan&model[]=Leaf"
#page = urllib.request.urlopen(url+"0")
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib.request.Request(url,None,hdr)
page = urllib.request.urlopen(req)

#print(page.read())
data = page.read().decode('utf-8')
prices = [int(m.group()) for m in re.finditer('(?<=class="listing-detail-line price" data-price=")(\d+)(?=")',data)]
miles = [int(m.group().replace(",","")) for m in re.finditer('(?<=Mileage: )\d{1,3}(,\d{3})*',data)]

print(miles,prices)
exit()

top1000 = top100

for p in range(2,11):
    url = "https://boardgamegeek.com/browse/boardgame/page/"+str(p)
    page = urllib.request.urlopen(url)
    data = page.read().decode('utf-8')
    top = [int(m.group()) for m in re.finditer('(?<=href="/boardgame/)(\d+)(?=/)',data)]
    top1000.extend(top[0::3])
