import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
init()

supreme = requests.get("https://www.supremenewyork.com/shop/all")

# List of links to the items currently in stock
links = []
# Details of the items in stock.
items_in_stock = []


# The Beautiful Soup Object
soup = BeautifulSoup(supreme.content, 'html.parser')
all_items = soup.select('.inner-article')

# Loop over items on the home page.
# If item is in stock, append the link to the list of links, above.
for item in all_items:
    link_href = item.find('a').attrs['href']
    if item.text != 'sold out':
        links.append(f"https://supremenewyork.com{link_href}")


def get_items():
    for link in links:
        new_supreme = requests.get(link)
        more_soup = BeautifulSoup(new_supreme.content, 'html.parser')
        actual_item = more_soup.select('#details')
        for description in actual_item:
            item_name = description.find('h2').text
            color = description.find('p').text
            print(
                Fore.GREEN + f"Item:{item_name}\n Color: {color}\n {link}\n")
            items_in_stock.append(
                {"Item": item_name, "Color": color, "Link": link})


get_items()
