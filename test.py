from http import client
from pydoc import cli

from matplotlib.pyplot import hot
import praw


reddit = praw.Reddit(client_id='EBohoWcmdN-cPi8HTOIUSw',
                     client_secret='tWUMO3InJO1KrY8d5iJ7DasBoUQy4w',
                     username="Automatic-Bid4538",
                     password="X890TNzsJj93",
                     user_agent="bda_sentimentv1")

subreddit = reddit.subreddit('ukraine')


hot_python = subreddit.hot(limit=10)
for i in hot_python:
    if not i.stickied and i.is_self:
        print(i.selftext)
