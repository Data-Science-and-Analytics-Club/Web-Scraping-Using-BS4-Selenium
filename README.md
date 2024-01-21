
# Overview
This README provides an introduction to web scraping, web crawling, and spiders, along with an overview of popular Python tools used for scraping, including Scrapy, BeautifulSoup (Bs4), Selenium, and Requests.

## What are Web Scrapers, Web Crawlers, and Spiders?


**1. Web Scrapers:**


Web scrapers are programs or scripts designed to extract data from websites. They navigate through the HTML structure of web pages, locate specific elements, and extract relevant information. Scraping is commonly used to gather data for analysis, research, or to populate databases.

**2. Web Crawlers:**

Web crawlers, also known as web spiders or bots, are automated programs that systematically browse the internet, following links from one page to another. Their primary purpose is to index and gather information from websites. Search engines use web crawlers to index web pages and provide relevant results to users.

**3. Spiders:**

In the context of web crawling, spiders are specific types of programs or scripts that are designed to navigate through websites, following links and gathering data. Spiders are a crucial component of web crawlers, helping to systematically traverse the web and collect information.

## Python Tools for Web Scraping
**1. Scrapy**


Scrapy is an open-source and collaborative web crawling framework for Python. It provides a set of built-in tools for handling common crawling tasks, making it efficient for large-scale web scraping projects. Scrapy follows the "don't repeat yourself" (DRY) principle and is extensible. \
[Read Docs](https://docs.scrapy.org/en/latest/)

**2. BeautifulSoup (Bs4)**


BeautifulSoup is a Python library for pulling data out of HTML and XML files. It provides Pythonic idioms for iterating, searching, and modifying the parse tree. Bs4 is often used in conjunction with other libraries like Requests for web scraping tasks. \
[Read Docs](https://readthedocs.org/projects/beautiful-soup-4/)

**3. Selenium**


Selenium is a browser automation tool commonly used for testing web applications. It can also be used for web scraping when dynamic content or user interactions are involved. Selenium allows you to control a browser programmatically, making it useful for scenarios where static HTML retrieval is not sufficient. \
[Read Docs](https://selenium-python.readthedocs.io)



**4. Requests**


Requests is a simple and elegant HTTP library for Python. While not a scraping library on its own, it is often used in conjunction with BeautifulSoup or other parsing libraries to retrieve HTML content from web pages. \
[Read Docs](https://requests.readthedocs.io/en/latest/)


## Setup and Installation

[Github cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf) 

**For Experiment One:** 



1. Install the Dependencies using the following command: 
   
   `pip3 install -r requirements.txt`

2. run the script using: 
   
   `python3 scrapish0.py`

**For Experiment Two**

1. Install Jupyter Notebook:
   
   `pip install notebook`
3. Install other dependencies:
   
   `pip install -r requirements.txt`
4. Open Jupyter Notebook:
    
   `jupyter notebook`
   
5. Replace Your details from `scraping.ipynb` file
   
6. Run the file using Jupyter GUI 




 
