import os
from perolas import perolas
import tweepy

consumer_key = os.environ["APIKEY"]
consumer_secret = os.environ["APISECRET"]
access_token = os.environ["ACCESSTOKEN"]
access_token_secret = os.environ["ACCESSTOKENSECRET"]

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

if perolas() == "\"olha essa mikasa brasileira 100% jesus completamente gostosa\"":
    api.update_status_with_media(perolas(), "minhacasa.png")
else:
    api.update_status(perolas())
user = api.get_user(screen_name="@supimpa_bot")
userID = user._json['id']
myTweets = api.user_timeline(user_id=userID)
try:
    for tweets in myTweets:
        tweetID = tweets._json['id']
        api.create_favorite(tweetID)
except:
    print("já curtido!")