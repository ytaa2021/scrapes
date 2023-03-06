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
page = open(r"C:\Users\yotam.twersky\Downloads\The Cyber Security Providers at Infosecurity Europe.mhtml", "r", encoding="UTF-8")
contents = page.read()
bsText = BeautifulSoup(contents, 'lxml')

#print(bsText.body.prettify())


title = bsText.findAll('h3')


finallist = []
for el in title:
    finallist.append([el.get_text()])

finallist = [[i[0].replace("=\n", '')] for i in finallist]
finallist = [[i[0].replace("</h3>", '')] for i in finallist]
finallist = [[i[0].replace("h3>", '')] for i in finallist]

print(finallist)

f = open(r"C:\Users\yotam.twersky\OneDrive - Kiteworks\Desktop\infosecurity-exhibitors.csv", 'w')
csv_writer = csv.writer(f)
csv_writer.writerows(finallist)