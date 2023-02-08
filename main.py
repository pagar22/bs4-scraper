import requests
from bs4 import BeautifulSoup


def makeMeSomeSoup(url):
    page = requests.get(url)
    htmlContent = page.content
    return BeautifulSoup(htmlContent, "html.parser")


url = "https://pagar22.github.io"
soup = makeMeSomeSoup(url)

all_links = set()
anchors = soup.find_all("a")

for anchor in anchors:
    all_links.add(anchor.get("href"))

print(all_links)
