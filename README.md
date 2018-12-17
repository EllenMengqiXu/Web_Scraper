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
```
source activate ScrapyEnvironment
```
* scrapy startproject "name",
```
scrapy startproject test
```
* scrapy genspider "name" domain,
```
scrapy genspider ts ts.com
```
* go to scrapy shell --> fetch webiste url [make sure crawl(200)],
```
scrapy shell
fetch('test.com/example')
```
* use css/xpath to select every class unit that you want to crawl, (Reference: https://www.w3schools.com/cssref/css_selectors.asp)
```
response.css('.item::test').extract_first().strip()
```
* write in python spiders and items (chenge user agent in setting.py if needed),
```
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
```
* after finish coding, go to terminal, make your path in spiders folder and put in: scrapy crawl spidername -o XXX.csv,
```
scrapy crawl ts -o firstbach.csv
```
* your export file should be saved in spiders folder named xxx.csv.


