import requests
from bs4 import BeautifulSoup


url = "https://pagar22.github.io"
cl = "https://www.uefa.com/uefachampionsleague/history/seasons/2021/"
cl2 = "https://www.uefa.com/uefachampionsleague/news/026c-131a0f45d056-813415b1929d-1000--all-the-2021-22-champions-league-fixtures-and-results/"

page = requests.get(cl2)
htmlContent = page.content

soup = BeautifulSoup(htmlContent, "html.parser")
title = soup.title
divs = soup.find_all("div")

# print(soup.find('div')['id'])


# print(soup.find_all("span", class_="pk-font-size--s"))
# print(soup.find_all("div", class_="pk-match-unit"))

results = soup.find_all("a", {"target": "_self"})


for result in results:
    print(result.contents[0])
