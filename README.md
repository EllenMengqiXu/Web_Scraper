SCRAPY FRAMEWORK
===

Use Scrapy framework to crawl information from advertising website.
---

In this project, I use scrapy framework to extract title, url, address, Zipcode and phone number from yelp, 168ganji and other Chinese restauarant advertising website.

Steps:

* go to terminal and write bash as "source activate ScrapyEnvironment",
* scrapy startproject "name",
* scrapy genspider "name" domain,
* go to scrapy shell --> fetch webiste url,
* use css to select every class unit that you want to crawl.
* write in python spiders and items.
* after finish coding, go to terminal and put in: scrapy crawl spidername -o XXX.csv.
* your export file should be saved in spiders file named xxx.csv.
