# Author Theo Brown
import requests
import re
from bs4 import BeautifulSoup

# for i in range(99999):
#     if i != 0:
i=2
listOfCard =  list()
URL = 'https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=' + str(i)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')  # for readability during writing
# print(soup)
row = soup.find('tr')  # Extract and return first occurrence of tr
# print(row)  # Print row with HTML formatting
print("=========Text Result==========")
print(row.get_text())  # Print row as text

for text in row.get_text():
    for st in text:
        temp = list()
        if not re.search(r'^\s|\s$', st):
            temp.append(st)
        listOfCard.append(temp)
        print(temp)

        # a = '''<input type="hidden" value="985207" name="order[ship_address_attributes]
        # [id]" id="order_ship_address_attributes_id">'''
        #
        # # Or:
        # # soup = bs(a, 'lxml')
        # soup = BeautifulSoup(a, 'html.parser')
        # option = soup.find("selected", {"name": "try"}).findAll("option")
        # option_ = soup.find("table", {"style": "font-size:14px"}).findAll("option")
        # print(option)
        # print(option_)
        # card_name = soup.find('div', {'id': 'ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_nameRow'})['value']
        # print(card_name)
       # name = name_div.find('value').text