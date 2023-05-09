from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Seleniium Options


class SiteScraper(Options):
    def __init__(self):
        super().__init__()
        self.options = Options()
        self.options.add_argument("--headless=new")
        self.homepage = "https://us.supreme.com/collections/all"
        self.driver = webdriver.Chrome(options=self.options)
        self.item_links = []
        self.item_details_lst = []
        self.main_content_class = "bpS-flexWrap-wrap"
        self.supreme_url = "https://us.supreme.com"
        self.color_class = (
            "fontWeight-bold mb-s display-none bpS-display-block js-variant"
        )

        self.item_title_class = "product-title"

    def get_item_links(self):
        self.driver.get(self.homepage)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        all_items = soup.find_all("a", attrs={"class": self.main_content_class})
        for item in all_items:
            link_href = item.get("href")
            if "Sold Out" not in item.text:
                self.item_links.append(f"{self.supreme_url}{link_href}")
        return self.item_links

    def get_item_details(self, list_of_link):
        for link in list_of_link:
            try:
                self.driver.get(link)
                item_content = BeautifulSoup(self.driver.page_source, "html.parser")
                color = item_content.find(
                    "div",
                    attrs={"class": self.color_class},
                ).text
                description = item_content.find(
                    "h1",
                    attrs={"class": self.item_title_class},
                ).text
                self.item_details_lst.append(
                    {"Item": description, "Color": color, "Link": link}
                )
                print(f"Adding {description} - {color} to list of items")
            except:
                pass
        return self.item_details_lst
