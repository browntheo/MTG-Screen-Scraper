# Author Theo Brown
import requests
from bs4 import BeautifulSoup

for i in range(99999):
    if (i != 0):
        URL = 'https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=' + str(i)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')  # for readability during writing

        row = soup.find('tr')  # Extract and return first occurrence of tr
        print(row)  # Print row with HTML formatting
        print("=========Text Result==========")
        print(row.get_text())  # Print row as text