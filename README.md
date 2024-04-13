# Project: Smash Word Scraper

## Description

This Python project utilizes Beautiful Soup for efficient parsing and (optionally) Selenium for handling dynamic elements to scrape data from the Smash Word website. The scraped data can be sorted using customizable algorithms and searched based on specific criteria.

## Ethical Considerations

- Always respect website terms of service and robots.txt guidelines.
- Implement rate limiting and polite scraping practices to avoid overloading the server.
- Consider the potential impact of your scraping on the website's performance and stability.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/<your-username>/smash-word-scraper.git
    ```

2. Install required dependencies:

    ```bash
    pip install beautifulsoup4 requests  # Adjust dependencies based on your needs
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
Replace the provided basic bubble sort implementation with your preferred sorting algorithm (e.g., merge sort, quick sort) in either script.

## Data Searching
Customize the provided basic search function to search based on different criteria in either script.

## Qt Designer Integration (optional)
Integrate a user interface created using Qt Designer with the scraping and manipulation logic using PyQt.
