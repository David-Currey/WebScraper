Web Scraper for Loblaws Product Data

A simple Python script using Selenium to scrape product names and prices from the Loblaws website and export the data to a CSV file.

Features

Navigates through paginated product listings

Extracts product titles and prices

Randomized delays to mimic human browsing

Saves results to scraped_data.csv

Prerequisites

Python 3.7 or higher

Google Chrome browser installed

ChromeDriver compatible with your Chrome version

Python packages:

selenium

Installation

Clone the repository (or copy the script file) to your local machine.

Install dependencies:

pip install selenium

Download ChromeDriver:

Visit https://sites.google.com/chromium.org/driver/ and download the version matching your Chrome.

Unzip and note the path to chromedriver.exe.

Configuration

Set the ChromeDriver path placeholder in the script:

service = ChromeService("/full/path/to/chromedriver.exe")  # Replace "service path" with your actual path

(Optional) Use an environment variable to avoid hard-coding paths:

import os
service_path = os.getenv("CHROMEDRIVER_PATH", "/default/path/chromedriver.exe")
service = ChromeService(service_path)

(Optional) Adjust user-agent string in options.add_argument(...) to a different browser signature if needed.

Usage

Run the script:

python webscraper.py

The scraper will:

Wait for the page to load

Extract the product title and price elements

Write each pair to scraped_data.csv

Click the Next Page button until no more pages remain

When complete, open scraped_data.csv to view the collected data.

Output

scraped_data.csv - CSV file with two columns:

PRODUCT – Name of the product

PRICE – Listed price

Notes

Random delays (time.sleep(random.randint(0, 3))) help avoid triggering site rate limits.

Increase time.sleep(8) if your connection is slow or the page takes longer to load.

Ensure the CSS selectors ([data-testid="product-title"], [data-testid="price"], [aria-label="Next Page"]) match the site’s current structure, as they may change over time.
