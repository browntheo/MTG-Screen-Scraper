# Author Theo Brown
import requests
from bs4 import BeautifulSoup

# for i in range(99999):
#     if (i != 0):
i = 2
URL = 'https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=' + str(i)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')  # for readability during writing
#  print(soup)  # to confirm the format of the html for scraping
card_name = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_nameRow")
card_mana = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_manaRow")
card_cmc = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cmcRow")
card_type = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_typeRow")
card_text = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_textRow")
card_flavour_text = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_flavorRow")
card_set = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_setRow")
card_rarity = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rarityRow", )
card_artist = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_artistRow")
card_image = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cardImage")
# print(i)
# print(card_name)
