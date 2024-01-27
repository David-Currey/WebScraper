import csv
import getpass
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager

# resources
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
service = ChromeService(
    r"C:\Users\dcurr\chromeDriver\chromedriver-win32\chromedriver.exe"
)
driver = webdriver.Chrome(service=service)
driver.get("https://quotes.toscrape.com")

# driver.find_element(By.LINK_TEXT, "login").click()

"""
time.sleep(3)
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("admin")
my_pass = getpass.getpass()
password.send_keys(my_pass)
driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()
"""

# data
quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

# create csv
file = open("scraped_data.csv", "w")
writer = csv.writer(file)
writer.writerow(["QUOTES", "AUTHORS"])

# display data in console and add to csv file
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()  # close csv
driver.quit()  # close driver
