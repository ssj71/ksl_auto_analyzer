#!/usr/bin/env python3
#spencer jackson 
#this script is to grab data to make a scatter plot of car listings for price vs mileage to help me understand the current market
import urllib.request
import re
import copy
import numpy
import matplotlib.pyplot
import sys
import time

make = "Toyota"
model = "Corolla"
url = "https://cars.ksl.com/search/index?make[]="+make+"&model[]="+model+"&page="
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

prevp = []
prevm = []
prices = []
miles = []
duplicate = False
pagen = 0
start = time.time()
while not duplicate:
    req = urllib.request.Request(url+str(pagen),None,hdr)
    page = urllib.request.urlopen(req)
    pagen += 1

    data = page.read().decode('utf-8')

    p = [float(m.group()) for m in re.finditer('(?<=class="listing-detail-line price" data-price=")(\d+)(\.\d{2})?(?=")',data)]
    m = [int(m.group().replace(",","")) for m in re.finditer('(?<=Mileage: )\d{1,3}(,\d{3})*   ',data)]
    if(len(p) != len(m)):
        print("error,",len(m),"vs",len(p),"listings found on page",pagen+1)
        #print(data)
        print(m)
        print(p)
        exit()
    if(p != prevp and m != prevm):
        prevp = p
        prevm = m
        prices += p
        miles += m
        print(len(miles),"listings found in",time.time()-start,"seconds")
    else:
        duplicate = True
        
#print(miles)
#print(prices)
matplotlib.pyplot.scatter(miles,prices)
matplotlib.pyplot.ylabel('price')
matplotlib.pyplot.xlabel('mileage')
matplotlib.pyplot.show()
exit()
