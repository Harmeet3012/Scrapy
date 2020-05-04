import scrapy
from ..items import QuotetutorialItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

# Spiders are basically crawlers

class QuoteSpider(scrapy.Spider): # importing class Spider from module scrapy
	
	# don't change the name of the below variables(name and start_url) 
	# because Spider class expects these two to have the same name
	name ='quotes_login' # quotes is the name of the spider
	# start_url specifies the list of url's we want to scrape data from
	start_urls = [
	'http://quotes.toscrape.com/login'
	]

	def parse(self,response):
		token = response.css('form input::attr(value)').extract_first();
		# extracting token value
		print(token);
		return FormRequest.from_response(response,formdata={
				'csrf_token' : token,
				'username' : 'harmeetsingh',
				'password' : 'H@rm33t'
			},callback = self.start_scraping);

	def start_scraping(self,response):
		open_in_browser(response)# it will open it in browser and 
								 # logout automatically after it has finished scraping
		title = response.css('title::text').extract() 
		items = QuotetutorialItem()
		all_div_quotes = response.css('div.quote')
		for quote in all_div_quotes:
			quotes = quote.css('span.text::text').extract()
			authors = quote.css('.author::text').extract()
			tags = quote.css('.tag::text').extract()

			items['quote'] = quotes
			items['author'] = authors
			items['tag'] = tags
			#yield{
			#	'quotes ' : quotes,
			#	'authors ' : authors,
			#	'tags ' : tags	
			#}

			yield items

		# next_page = response.css('li.next a::attr(href)').get()
		# print(next_page)
		
		# if next_page is not None:
		# 	yield response.follow(next_page, callback = self.start_scraping)









