import requests
from bs4 import BeautifulSoup
import time

# time.sleep(5)
url = "https://pagar22.github.io"
cl = "https://www.uefa.com/uefachampionsleague/history/seasons/2021/"
cl2 = "https://www.uefa.com/uefachampionsleague/news/026c-131a0f45d056-813415b1929d-1000--all-the-2021-22-champions-league-fixtures-and-results/"
pl = "https://www.premierleague.com/results"

page = requests.get(pl)
htmlContent = page.content

soup = BeautifulSoup(htmlContent, "html.parser")
title = soup.title
divs = soup.find_all("div")

# print(soup.find('div')['id'])


# CL elements
# print(soup.find_all("span", class_="pk-font-size--s"))
# print(soup.find_all("div", class_="pk-match-unit"))

# results = soup.find_all("a", {"target": "_self"})
# results = soup.find_all("span", {"class": "score"})
results = soup.find_all("pk-button")
# results = soup.find_all("pk-match-unit")

# PL elements
# pl_matches = soup.find_all("ul", {"class": "matchList"})
pl_matches = soup.find_all("div", {"class": "tabbedContent"})

print(pl_matches)

# for result in results:
#     print(result)
