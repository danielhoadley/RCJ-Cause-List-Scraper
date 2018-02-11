from bs4 import BeautifulSoup
from urllib import urlopen
from pprint import pprint
import datetime

now = datetime.datetime.now()
date_label = now.strftime("%Y-%m-%d")


# Set the target url
url = 'https://www.justice.gov.uk/courts/court-lists/list-cause-rcj'

# Open the url
site = urlopen(url)

# Grab the page contents and store it in an object called soup
soup = BeautifulSoup(site, "lxml", from_encoding='utf-8')

# Find the <div class='article'></div> element in the page
table = soup.find_all("div", class_="article")

for i in table:
    html = str(i)

# print the table elements

pprint (html)

file = open(date_label + '.html', 'w')
file.write(html)

