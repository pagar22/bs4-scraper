import requests
from bs4 import BeautifulSoup


def makeMeSomeSoup(url):
    page = requests.get(url)
    htmlContent = page.content
    return BeautifulSoup(htmlContent, "html.parser")


url = "https://pagar22.github.io"
soup = makeMeSomeSoup(url)

# print(soup.find_all("div"))
