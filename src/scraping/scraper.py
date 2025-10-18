import scrapy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ImdbSpider(scrapy.Spider):
    name = "imdb_tv"

    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def get_genres(self, url):
        """ IMDb dizi sayfasına giderek türleri alır. """
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.ipc-chip__text"))
            )
            genres = [genre.text for genre in self.driver.find_elements(By.CSS_SELECTOR, "span.ipc-chip__text")]
        except Exception as e:
            genres = ["Bilinmiyor"]  
        return genres

    def start_requests(self):
        url = "https://www.imdb.com/chart/toptv/"
        self.driver.get(url)

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break  
            last_height = new_height

        html_content = self.driver.page_source
        response = scrapy.Selector(text=html_content)

        for show in response.css("div.cli-children"):
            title = show.css("h3.ipc-title__text::text").get()
            link = "https://www.imdb.com" + show.css("a.ipc-title-link-wrapper::attr(href)").get()
            rating = show.css("span.ipc-rating-star--rating::text").get()
            release_date = show.css("span.cli-title-metadata-item::text").get()

            if title and link and rating:
                genres = self.get_genres(link)
                

                yield {
                    "Dizi Adı": title,
                    "IMDb Puanı": rating,
                    "Link": link,
                    "Çıkış Tarihi": release_date,
                    "Türler": genres,
                }

        self.driver.quit()
