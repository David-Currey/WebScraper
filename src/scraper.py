import csv
import random
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager

# resources
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
service = ChromeService(
    r"C:\Users\dcurr\chromeDriver\chromedriver-win32\chromedriver.exe"
)
options = Options()
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.86 Safari/537.36"
)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.loblaws.ca/food/c/27985?page=1")

time.sleep(8)

# wait for page
time.sleep(3)

# create csv
file = open("scraped_data.csv", "w", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["PRODUCT", "PRICE"])

while True:
    # data
    titles = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-title"]')
    prices = driver.find_elements(By.CSS_SELECTOR, '[data-testid="price"]')

    # display data in console and add to csv file
    for title, price in zip(titles, prices):
        print(f"{title.text} - {price.text}")
        writer.writerow([title.text, price.text])
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Next Page"]')
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        next_button.click()
        time.sleep(random.randint(0, 3))
    except NoSuchElementException:
        break
file.close()  # close csv
driver.quit()  # close driver
