import csv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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

# create csv
file = open("scraped_data.csv", "w", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["QUOTES", "AUTHORS"])

while True:
    # data
    quotes = driver.find_elements(By.CLASS_NAME, "text")
    authors = driver.find_elements(By.CLASS_NAME, "author")

    # display data in console and add to csv file
    for quote, author in zip(quotes, authors):
        print(quote.text + " - " + author.text)
        writer.writerow([quote.text, author.text])
    try:
        driver.find_element(
            By.PARTIAL_LINK_TEXT, "Next"
        ).click()  # click next page button
    except NoSuchElementException:
        break
file.close()  # close csv
driver.quit()  # close driver
