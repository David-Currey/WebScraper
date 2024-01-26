import csv

import requests
from bs4 import BeautifulSoup

# resource
web_page = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(web_page.text, "html.parser")

# data
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

# create csv
file = open("scraped_data.csv", "w")
writer = csv.writer(file)
writer.writerow(["QUOTES", "AUTHORS"])

# display data in console and add to csv file
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()  # close csv
