import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetutItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com'
    ]

    def parse(self, response):
        # token = response.css('form input::attr(value)').extract_first()
        # return FormRequest.from_response(response, formdata = {
        #     'csrf_token': token,
        #     'username': 'hello@gmail.com',
        #     'password': '123456'
        # }, callback=self.start_scraping)

        items = QuotetutItem()
    
        all_div_quotes = response.css("div.quote")
        for quotes in all_div_quotes:
            title = quotes.css("span.text::text").extract_first()
            author = quotes.css("small.author::text").extract_first()
            tags = quotes.css("a.tag::text").extract_first()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items
    
    def start_scraping(self, response):
        pass
        # open_in_browser(response)
        

        

        # next_page = response.css('li.next a::attr(href)').get()

        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.start_scraping)