import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'nhNFDac7wxpIdUmJjMgrKKB68'
consumer_secret = '6f1jQpHTK52U8PP9JHB15zaSx6kQZn6zMBBNr6Csc883SBTRtI'
access_token = '1013780071499223045-FYFso89tQ6GXUouRIjZ4RUTP6xnmVA'
access_secret = 'UW4waSBwOZS16Q2zLRyRoXGsRxHbEj0FgO5RghHl5oc6Y'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
