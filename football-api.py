import requests

url = "https://match.uefa.com/v5/matches"

params = dict(
    competitionId=0,
    seasonYear="2021",
    phase="TOURNAMENT",
    order="DESC",
    offset=0,
    limit=125,
)

resp = requests.get(url=url, params=params)
data = resp.json()

for match in data:
    print(
        match["awayTeam"]["internationalName"]
        + " "
        + str(match["score"]["regular"]["away"])
        + " - "
        + str(match["score"]["regular"]["home"])
        + " "
        + match["homeTeam"]["internationalName"]
    )
