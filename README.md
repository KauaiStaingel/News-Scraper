# News Scraper

This repository contains a Python script that uses Selenium to search for news on a specific website, extracting information such as title, date, description, and image link, and saving this data into an Excel file.

## Requirements

Before running the script, ensure you have the following requirements installed:

- Python 3.12.2
- Google Chrome
- ChromeDriver (compatible with the installed version of Chrome)
- Required Python libraries:

  ```bash
  pip install selenium pandas

##  Execution
Navigate to the project directory.

Run the app.py script:

        python app.py

When prompted, enter the keyword for the news search.

The script will search for related news and create a news.xlsx file with the results.

##  Features
News Search: Searches for news using a keyword provided by the user.
Data Extraction: Collects titles, dates, descriptions, and image links from the news articles.
Excel Export: The collected data is exported to an Excel file (news.xlsx).

##  Code Structure
The code is structured into functions to facilitate maintenance and reuse:

-  click_element_by_selector(element_selector, time): Clicks on an element based on the CSS selector.
-  find_element_by_tag(element_tag, time, web_element): Returns an element based on the HTML tag.
-  find_element_by_class(element_class, time, web_element): Returns an element based on the CSS class.
-  find_all_element_by_tag(element_tag, time, web_element): Returns all elements based on the HTML tag.
-  write_element_by_selector(element_selector, time, text): Writes text into an element based on the CSS selector.
-  scroll_element_selector(element_selector, time): Scrolls the page to a specific element based on the CSS selector.
-  press_enter(): Simulates the ENTER key press.

##  Errors and Solutions
If any error occurs during the script's execution, it will be captured and displayed in the terminal. The script also handles common situations, such as cookie prompts on the website.
