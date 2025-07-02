Web Scraper for Loblaws Product Data

A simple Python script using Selenium to scrape product names and prices from the Loblaws website and export the data to a CSV file.

Navigates through paginated product listings

Extracts product titles and prices

Randomized delays to mimic human browsing

Exports results to scraped_data.csv

Prerequisites

Python 3.7 or higher

Google Chrome browser

ChromeDriver (matching your Chrome version)

Python packages:

selenium

Installation

Clone this repository or copy webscraper.py to your local machine.

Install dependencies:

pip install selenium

Download and unzip ChromeDriver from ChromeDriver Downloads.

Configuration

Set the ChromeDriver path in webscraper.py:

from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService("/full/path/to/chromedriver.exe")  # Replace with your path

Use an environment variable (optional):

import os
from selenium.webdriver.chrome.service import Service as ChromeService

service_path = os.getenv("CHROMEDRIVER_PATH", "/default/path/chromedriver.exe")
service = ChromeService(service_path)

(Optional) Adjust the User-Agent in options.add_argument(...) if needed.

Usage

Run the scraper:

python webscraper.py

The script will:

Launch Chrome and navigate to the specified Loblaws page.

Wait for the page to fully load.

Extract product titles and prices.

Write each pair to scraped_data.csv.

Click Next Page until no more pages are found.

Close the browser and finish.

Output

scraped_data.csv – CSV file with columns:

PRODUCT – Name of the product

PRICE – Listed price

Notes

Random delays (time.sleep(random.randint(0, 3))) help avoid rate limiting.

Increase time.sleep(8) at the top if your network is slow.

Verify CSS selectors ([data-testid="product-title"], [data-testid="price"], [aria-label="Next Page"]) match the current site layout.
