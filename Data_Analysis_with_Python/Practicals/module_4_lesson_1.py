import scrapy

class ECommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    start_urls = ['https://example.com/products']

    def parse(self, response):
        # Extract product URLs
        product_urls = response.css('a.product-link::attr(href)').extract()
        
        # Follow each product URL and parse product details
        for product_url in product_urls:
            yield scrapy.Request(url=product_url, callback=self.parse_product)
            
        # Follow pagination links
        next_page = response.css('a.next-page::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_product(self, response):
        # Extract product details
        product = {
            'name': response.css('h1.product-name::text').extract_first(),
            'price': response.css('span.product-price::text').extract_first(),
            'description': response.css('div.product-description::text').extract_first(),
            # Add more fields as needed
        }
        
        yield product