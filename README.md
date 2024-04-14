# Project: Smash Word Scraper

## Description

This Python project utilizes Beautiful Soup for efficient parsing and (optionally) Selenium for handling dynamic elements to scrape data from the Smash Word website. The scraped data can be sorted using customizable algorithms and searched based on specific criteria.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/<your-username>/smash-word-scraper.git
    ```

2. Install required dependencies:

    ```bash
    pip install beautifulsoup4 
    ```

## Usage

### With Beautiful Soup (for non-dynamic content):

    Run the `scrape_with_beautifulsoup.py` script:
    
    ```bash
    python scrape_with_beautifulsoup.py
## With Selenium (optional, for dynamic content):
    Ensure you have the necessary web drivers for Selenium installed (refer to Selenium documentation for details).
          Run the scrape_with_selenium.py script:
       ```bash
        Copy code
        python scrape_with_selenium.py
## Data Sorting
Applying sorting algorithms to sort the data .There are  linear sorting algo.

## Data Searching
Binary search is availble by different   Filters.

## Qt Designer Integration (optional)
Integrate a user interface created using Qt Designer with the scraping and manipulation logic using PyQt.
