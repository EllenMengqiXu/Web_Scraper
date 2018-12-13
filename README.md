SCRAPY FRAMEWORK
===

Use Scrapy framework to crawl information from advertising website.
---

In this project, I use scrapy framework to extract title, url, address, Zipcode and phone number from yelp, 168ganji and other Chinese restauarant advertising website.

Prerequisites:

* Python - programming language
* Sublime - code editor
* scrapy 
* scrapy virtual environment

Steps:

* go to terminal and write bash as "source activate ScrapyEnvironment"(mac) OR go to CMD find users-->exu-->env-->script and put in activate(windows),
* scrapy startproject "name",
* scrapy genspider "name" domain,
* go to scrapy shell --> fetch webiste url [make sure crawl(200)],
* use css/xpath to select every class unit that you want to crawl, (Reference: https://www.w3schools.com/cssref/css_selectors.asp)
* write in python spiders and items (chenge user agent in setting.py if needed),
* after finish coding, go to terminal, make your path in spiders folder and put in: scrapy crawl spidername -o XXX.csv,
* your export file should be saved in spiders folder named xxx.csv.


