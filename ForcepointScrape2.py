from bs4 import BeautifulSoup
import csv


with open('/Users/yotamtwersky/Downloads/<div class="form--result_partner-distrib.html', 'r') as f:
    page = f.read()
soup = BeautifulSoup(page, 'html.parser')


listofpartners = []

for i in soup.findAll('div', attrs={"class": "form--result_partner-distributor"}):
    listofpartners.append((i))
for i in soup.findAll('div', attrs={"class": "appended-results-wrapper"}):
    for j in i.findAll('div', attrs={"class": "form--result_partner-distributor"}):
        listofpartners.append((j))


partnerscontent = []
for k in listofpartners:
    partnercontent = []
    first = k.find('div', attrs={"class": "form--results_partner-distributor--info"})
    second = first.find('div', attrs={"class": "form--result_partner-distributor--info--title"})
    third = second.find('h3')
    name = third.text
    tier = second.find('span').text
    aas = first.findAll('a')
    if len(aas) == 2:
        cell = aas[0].text
        site = aas[1].text
    else:
        try:
            site = aas[0].text
        except:
            pass
   
    next = k.find('div', attrs={"class": "form--results_partner-distributor--services"})
    secnext = next.find('ul')
    thirdnext = secnext.find('li').text
    partnercontent = [name,site,tier,cell,thirdnext]
    #Name site tier cell and services
    partnerscontent.append(partnercontent)
print(partnerscontent)
fields = ['Name', 'Site', 'Tier', 'Cell', 'Services']
with open('/Users/yotamtwersky/Documents/Forcepoint Partner Scrape Output.csv', 'w') as outfile:
    write = csv.writer(outfile)
    write.writerow(fields)
    write.writerows(partnerscontent)

