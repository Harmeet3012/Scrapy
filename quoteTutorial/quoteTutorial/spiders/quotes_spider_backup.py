import scrapy
from ..items import QuotetutorialItem
# Spiders are basically crawlers

class QuoteSpider(scrapy.Spider): # importing class Spider from module scrapy
	
	# don't change the name of the below variables(name and start_url) 
	# because Spider class expects these two to have the same name
	name ='quotes' # quotes is the name of the spider
	# start_url specifies the list of url's we want to scrape data from
	start_urls = [
	'http://quotes.toscrape.com/'
	]

	def parse(self,response): # quotes.toscrape will send its source code in the response variable
		title = response.css('title::text').extract() # .css will look for the title tag
												# .extract extracts data from the title tag, if found
		# Output(if in .css('title') is given) : {'title text': ['<title>Quotes to Scrape</title>']}
		# Output(if in .css('title::text') is given) : {'title text': ['Quotes to Scrape']}
		# yield {'title text' : title} # data is returned(yielded) in the form of dictionary

		# print all of it together
		#all_div_quotes = response.css('div.quote')
		#quotes = all_div_quotes.css('span.text::text').extract()
		#authors = all_div_quotes.css('.author::text').extract()
		#tags = all_div_quotes.css('.tag::text').extract()

		#yield {
		#	'title ' : title,
		#	'quotes ' : quotes,
		#	'authors ' : authors,
		#	'tags ' : tags
		#}

		# print quotes, authors and tags one by one
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

		next_page = response.css('li.next a::attr(href)').get()
		print(next_page)
		
		if next_page is not None:
			yield response.follow(next_page, callback = self.parse)







