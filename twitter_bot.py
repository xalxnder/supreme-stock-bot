from tweepy import API, OAuthHandler
import os


class Bot(API):
    def __init__(self):
        super().__init__()
        self.API_KEY = os.getenv("TWITTER_API_KEY")
        self.API_SECRET = os.getenv("TWITTER_API_SECRET")
        self.ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
        self.ACCESS_TOKEN_SECRET = os.getenv("TWITTER_TOKEN_SECRET")

    def api_boject(self):
        # Authenticate to Twitter
        auth = OAuthHandler(self.API_KEY, self.API_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = API(auth)
        return api

    def credentials_verifier(self, api_object):
        try:
            api_object.verify_credentials()
            print("All good!")
            return True
        except:
            print("Error during authentication")
            return False
