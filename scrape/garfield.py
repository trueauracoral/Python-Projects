#!/usr/bin/env python
import requests
import random
from calendar import monthrange

website = "https://www.gocomics.com/garfield/"

def random_date():
    year_list = list(range(1979, 2021))
    year = year_list[random.randint(0,len(year_list))]
    month = str(random.randint(1,12)).zfill(2)
    days = monthrange(int(year),int(month.replace("0","")))[1]
    day = str(random.randint(1,days)).zfill(2)
    return f"{year}/{month}/{day}"
    
def image_url(url):
    print(url)
    data = requests.get(url, allow_redirects=True).text
    loc = data.find('https://assets.amuniversal.com/')
    image = data[loc:loc+63]
    return image

print(image_url(website+random_date()))
