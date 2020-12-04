import urllib.request

from bs4 import BeautifulSoup as bs

i = 2
URL = 'https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=' + str(i)
# redditPage1 = "http://redditlist.com/sfw"
r = urllib.request.urlopen(URL,  cafile=None, capath=None, cadefault=False, context=None).read()
soup = bs(r, 'html.parser')
for sub_div in soup.find("td", id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rightCol").parent.find_all('div', {"class": "row"}):
    print(str(sub_div.find('value')))