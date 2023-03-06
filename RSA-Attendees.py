import requests
import lxml
import sys
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'referer': 'https://www.rsaconference.com/'}
#page = requests.get(r"https://www.rsaconference.com/usa/expo-and-sponsors", headers=headers)

from bs4 import BeautifulSoup
  
# Opening the html file. If the file
# is present in different location, 
# exact location need to be mentioned
page = open(r"C:\Users\yotam.twersky\OneDrive - Kiteworks\Desktop\Expo & Sponsors _ RSA Conference.html", "r")
contents = page.read()
bsText = BeautifulSoup(contents, 'lxml')

#print(bsText.body.prettify())


title = bsText.findAll('a', {"class":'CoveoResultLink'})

finallist = []
for el in title:
    finallist.append([el.get_text()])
print(finallist)

f = open(r'C:\Users\yotam.twersky\OneDrive - Kiteworks\Desktop\Book1.csv', 'w')
csv_writer = csv.writer(f)
csv_writer.writerows(finallist)

'''
for tag in bsText.findAll(True):
    print(tag.name, " : ", len(bsText.find(tag.name).text))
'''
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')'''