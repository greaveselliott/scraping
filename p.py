import requests
from bs4 import BeautifulSoup
import csv

url = "https://scrapethissite.com/pages/simple/"

with open("./output.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "Capital", "Population", "Area"])

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    countries = soup.find_all("div", "country")

    for country in countries:
        name = country.find("h3").text.strip().encode("utf-8")
        capital = country.find("span", "country-capital").text.strip().encode("utf-8")
        population = country.find("span", "country-population").text.strip()
        area = country.find("span", "country-area").text.strip()

        writer.writerow([name, capital, population, area])