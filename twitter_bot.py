import tweepy
import time
from secrets import *
from get_items import get_item_details, item_details

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY,
                           API_SECRET)
auth.set_access_token(ACCESS_TOKEN,
                      ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("All good!")
except:
    print("Error during authentication")

user = api.me()

get_item_details()

for i in item_details:
    api.update_status(
        f"{i['Item']} is currently in stock.\n Color: {i['Color']}\n {i['Link']}")
    print("Tweet posted successfully.")
    time.sleep(30)
