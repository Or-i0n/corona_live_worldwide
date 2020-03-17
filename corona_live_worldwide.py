"""After pressing RUN, enter your country's
name or continent's name or leave it empty to see all the data."""

# COVID-19 worldwide status

import re
from urllib import request as req
import os

os.system("pip -q install bs4")
from bs4 import BeautifulSoup as Soup 


URL = ("https://www.ecdc.europa.eu/en/"
       "geographical-distribution"
       "-2019-ncov-cases")

DATAERR = "Data Error! Failed to fetch information."

raw = req.urlopen(URL).read()
page = raw.decode()

soup = Soup(page, features="html.parser")

# Info status.
h1 = soup.find("h1")
ps = soup.find_all("p")

if not h1 or not ps:
    quit(DATAERR)
print(f"🌟 {h1.text}")


def showinfo(data, query=None):
    """Shows data in a beautiful way."""
    
    print("➖" * 19)
    # If query is provided only print 
    # countries that match query.
    if query:
        
        for country in data.split(","):
            if query in country.lower():
                print("●", country)
    else:
        for country in data.split(","):
                print("●", country)
    
    print("➖" * 19)
        

query = input().lower()

for n, p in enumerate(ps[:9]):
    para = p.text

    if n == 0:
        summary = re.match(r"\b.+ deaths\.", para)
        if summary:
            print(f"🌐 Global Summary: ")
            print("➖" * 19)
            
            print(summary.group())
            if query in para.lower():
                print("\n💀 Reported deaths:")
                deaths = para.replace(summary.group(), "")
                showinfo(deaths, query)
        else:
            print(DATAERR)
    elif n in range(1, 8):
        if para.lower().startswith(query):
            print("\n😷 Reported cases:")
            showinfo(para)
        elif query in para.lower():
            print("\n😷 Reported cases:")
            showinfo(para, query)
    
