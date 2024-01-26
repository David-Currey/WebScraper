import csv
import getpass
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# import requests
# from bs4 import BeautifulSoup

# resource
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://quotes.toscrape.com")

web_page.find_element(By.LINK_TEXT, "login").click()

"""
time.sleep(3)
username = web_page.find_element(By.ID, "username")
password = web_page.find_element(By.ID, "username")
username.send_keys("admin")
my_pass = getpass.getpass()
password.send_keys(my_pass)
web_page.find_element(By.CSS_SELECTOR, "input.btn-primary").click()
"""

# data
quotes = web_page.find_elements(By.CLASS_NAME, "text")
authors = web_page.find_elements(By.CLASS_NAME, "author")

# create csv
file = open("scraped_data.csv", "w")
writer = csv.writer(file)
writer.writerow(["QUOTES", "AUTHORS"])

# display data in console and add to csv file
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()  # close csv
