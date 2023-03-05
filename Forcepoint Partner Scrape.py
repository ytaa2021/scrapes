from bs4 import BeautifulSoup


with open('/Users/yotamtwersky/Documents/Find a Partner | Forcepoint.html', 'r') as f:
    page = f.read()
soup = BeautifulSoup(page, 'html.parser')
body = soup.find('body')
div1 = body.find('div', attrs={"class": "panel-display panel-1col clearfix"} )
div2 = div1.find('div', attrs={"class": "panel-panel panel-col"} )
div3 = div2.find('div')
div4 = div3.find('div', attrs={"class": "panel-pane pane-page-content"} )
div5 = div4.find('div', attrs={"class": "ws-unwrapped__btm middle"} )
div6 = div5.find('div', attrs={"class": "panel-pane pane-find-partner"} )
div7 = div6.find('div', attrs={"class": "pane-content"} )
div8 = div7.find('div', attrs={"id": "form--partner_distributor"} )
div9 = div8.find('form')
div9 = div8.find('div')
div10 = div9.find('div', attrs={"id": "form--results"} )
allptnrs = div10.findAll('div', attrs={"class": "form--result_partner-distributor"})



#div5 = div4.find('div', attrs={"class": } )
#div6 = div5.find('div', attrs={"class": "panel-panel panel-col"} )
#panel-pane pane-panels-mini pane-header

print(div9)
