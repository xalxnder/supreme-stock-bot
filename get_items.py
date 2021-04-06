import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
#Initialize colorama
init()

supreme = requests.get("https://www.supremenewyork.com/shop/all")

# List of links to the items currently in stock
item_links = []
# Details of the items in stock.
item_details_lst = []


# The Beautiful Soup Object
main_content = BeautifulSoup(supreme.content, 'html.parser')
all_items = main_content.select('.inner-article')

# Loop over items on the home page.
# If item is in stock, append the link to the list of item_links, above.
for item in all_items:
    link_href = item.find('a').attrs['href']
    if item.text != 'sold out':
        item_links.append(f"https://supremenewyork.com{link_href}")


def get_item_details():
    for link in item_links:
        supreme_item = requests.get(link)
        item_content = BeautifulSoup(supreme_item.content, 'html.parser')
        item_details = item_content.select('#details')
        for description in item_details:
            print(description.find('h2').text)
            item_name = description.find('h2').text
            item_color = description.find('p').text
            item_details_lst.append(
                {"Item": item_name, "Color": item_color, "Link": link})

get_item_details()