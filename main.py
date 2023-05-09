from item_scooper import SiteScraper
from twitter_bot import Bot
import time

scraper = SiteScraper()
supreme_bot = Bot()
api = supreme_bot.api_boject()


supreme_items = scraper.get_item_details(scraper.get_item_links())


user = api.get_user(screen_name="PremeStockBot")


for item in supreme_items:
    try:
        api.update_status(
            f"{item['Item']} is currently in stock.\n Color: {item['Color']}\n {item['Link']}"
        )
        print("Tweet posted successfully.")
    except:
        pass
    time.sleep(10)
