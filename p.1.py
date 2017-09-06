import requests
from bs4 import BeautifulSoup
import csv


currentPage = 1
pages = 6



def getText(root, findTag, findClass):
    return root.find(findTag, findClass).text.strip().encode("utf-8")


with open("./team.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Year", "Wins", "Losses", "OT losses", "Win ratio", "Goals for", "Goals against", "Goal difference"])


    while (currentPage <= pages):
        print currentPage
        url = "https://scrapethissite.com/pages/forms/?%{}&per_page=100".format(currentPage)

        r = requests.get(url)

        soup = BeautifulSoup(r.text, "html.parser")
        rows = soup.find_all("tr", "team")
        
        print r.status_code

        for row in rows:
            name = getText(row, "td", "name")
            year = getText(row, "td", "year")
            wins = getText(row, "td", "wins")
            losses = getText(row, "td", "losses")
            otLosses = getText(row, "td", "losses")
            winRatio = getText(row, "td", "pct")
            goalsFor = getText(row, "td", "gf")
            goalsAgainst = getText(row, "td", "ga")
            goalDifference = getText(row, "td", "diff")

            writer.writerow([name, year, wins, losses, otLosses, winRatio, goalsFor, goalsAgainst, goalDifference])
        
        currentPage = currentPage + 1