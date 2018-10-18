import tweepy
import requests as req
from bs4 import BeautifulSoup
from lxml import html
import scrapy
import re

new_tweet = "========New_News=============================="

from tweepy import OAuthHandler
 
consumer_key = 'nhNFDac7wxpIdUmJjMgrKKB68'
consumer_secret = '6f1jQpHTK52U8PP9JHB15zaSx6kQZn6zMBBNr6Csc883SBTRtI'
access_token = '1013780071499223045-FYFso89tQ6GXUouRIjZ4RUTP6xnmVA'
access_secret = 'UW4waSBwOZS16Q2zLRyRoXGsRxHbEj0FgO5RghHl5oc6Y'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True)

#twitter_stream = Stream(auth, MyListener())
listOfLinks = []
clean_display = ""

for i,status in enumerate(tweepy.Cursor(api.home_timeline).items(7)):
    
    try:
        listOfLinks.append(re.search("(?P<url>https?://[^\s]+)", status.text).group("url"))
    except AttributeError:
        print("A link does not exist")  

    x = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",status.text)
    clean_display = clean_display + "\n" + str(i) + ")   " + x + "\n"


print("Display the clean text and a list of links")
print(clean_display)
#print(listOfLinks)
