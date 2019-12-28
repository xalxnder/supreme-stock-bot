import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
init()


supreme = requests.get("https://www.supremenewyork.com/shop/all")


# The Beautiful Soup Object
soup = BeautifulSoup(supreme.content, 'html.parser')
all_items = soup.select('.inner-article')

def get_items():
    for item in all_items:
        link = item.find('a')
        extension = link.attrs['href']
        new_supreme = requests.get(f"https://supremenewyork.com{extension}")
        if item.text != 'sold out':
            more_soup = BeautifulSoup(new_supreme.content, 'html.parser')
            actual_item = more_soup.select('#details')
            for description in actual_item:
                final_item = description.find('h2').text
                color = description.find('p').text
                print(
                    Fore.GREEN + f"Item:{final_item}\n Color: {color}\n https://supremenewyork.com{extension} \n \n")

get_items()

print('done')
    # print(pic.attrs['src'])
