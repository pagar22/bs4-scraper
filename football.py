from main import makeMeSomeSoup
import json
import re


def football_scraper():
    cl = "https://www.uefa.com/uefachampionsleague/history/seasons/2021/"
    cl2 = "https://www.uefa.com/uefachampionsleague/news/026c-131a0f45d056-813415b1929d-1000--all-the-2021-22-champions-league-fixtures-and-results/"
    pl = "https://www.premierleague.com/results"

    soup = makeMeSomeSoup(cl)

    # CL elements
    # print(soup.find_all("span", class_="pk-font-size--s"))
    # print(soup.find_all("div", class_="pk-match-unit"))
    # results = soup.find_all("a", {"target": "_self"})
    # results = soup.find_all("span", {"class": "score"})
    results = soup.find_all("pk-button")
    # results = soup.find_all("pk-match-unit")

    # PL elements
    # pl_matches = soup.find_all("ul", {"class": "matchList"})
    # pl_matches = soup.find_all("div", {"class": "tabbedContent"})

    # print(pl_matches)
    # print(results)
    matchBaseURL = "https://www.uefa.com/uefachampionsleague/match/"
    for result in results:
        data = result.get("data-tracking")
        if data != None:
            url = (
                matchBaseURL
                + json.loads(data)["id"]
                + "--"
                + re.sub("\s", "-", json.loads(data)["name"].lower())
                + "/"
            )
            print(url)


football_scraper()
