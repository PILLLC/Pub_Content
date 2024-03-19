
import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class MySpider(scrapy.Spider):
    name = "my_spider"

    def start_requests(self):
        # Start with SeleniumRequest to load the initial page
        yield SeleniumRequest(url="https://example.com", callback=self.parse)

    def parse(self, response):
        # Use Selenium to interact with dynamic content
        # For example, clicking a button to load more content
        driver = response.meta['driver']
        load_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='load-more-button']"))
        )
        load_more_button.click()

        # Wait for dynamic content to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='dynamic-content']"))
        )

        # Pass the HTML source to BeautifulSoup for parsing
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract structured data using Scrapy Selectors
        # For example, extract product titles
        titles = Selector(text=driver.page_source).xpath("//h2[@class='product-title']/text()").extract()

        # Extract dynamic content using BeautifulSoup
        # For example, extract text from a div with class 'dynamic-content'
        dynamic_content = soup.find("div", class_="dynamic-content").get_text()

        # Process or yield the extracted data as needed
        yield {
            'titles': titles,
            'dynamic_content': dynamic_content
        }