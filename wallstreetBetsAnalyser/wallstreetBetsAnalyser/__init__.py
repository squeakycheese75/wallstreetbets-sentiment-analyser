import sys
import os
import praw
import operator
from .reddit import parse_section, get_url
from .tickers import Ticker

def _setup(sub: str):
   # create a reddit instance
   reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                        username=os.getenv('REDDIT_USERNAME'), \
                        password=os.getenv('REDDIT_PASSWORD'),
                        user_agent=os.getenv('REDDIT_USER_AGENT'))
   # create an instance of the subreddit
   subreddit = reddit.subreddit(sub)
   return subreddit


def run(sub: str = "wallstreetbets", num_submissions: int = 100):
   ticker_dict = {}
   text = ""

   subreddit = _setup(sub)
   new_posts = subreddit.new(limit=num_submissions)

   for count, post in enumerate(new_posts):
      # if we have not already viewed this post thread
      if not post.clicked:
         # parse the post's title's text
         ticker_dict = parse_section(ticker_dict, post.title)
         
         # search through all comments and replies to comments
         comments = post.comments
         for comment in comments:
            # without this, would throw AttributeError since the instance in this represents the "load more comments" option
            if isinstance(comment, praw.models.MoreComments):
               continue
            ticker_dict = parse_section(ticker_dict, comment.body)

            # iterate through the comment's replies
            replies = comment.replies
            for rep in replies:
               # without this, would throw AttributeError since the instance in this represents the "load more comments" option
               if isinstance(rep, praw.models.MoreComments):
                  continue
               ticker_dict = parse_section(ticker_dict, rep.body)
         
         # update the progress count
         sys.stdout.write("\rProgress: {0} / {1} posts".format(count + 1, num_submissions))
         sys.stdout.flush()

   # text = "To help you YOLO your money away, here are all of the tickers mentioned at least 10 times in all the posts within the past 24 hours (and links to their Yahoo Finance page) along with a sentiment analysis percentage:"
   text += "\n\nTicker | Mentions | Bullish (%) | Neutral (%) | Bearish (%) | Score | %Change (%) | Price ($)"

   total_mentions = 0
   ticker_list = []
   for key in ticker_dict:
      total_mentions += ticker_dict[key].count
      ticker_list.append(ticker_dict[key])

   ticker_list = sorted(ticker_list, key=operator.attrgetter("count"), reverse=True)

   for ticker in ticker_list:
      Ticker.analyze_sentiment(ticker)

   for count, ticker in enumerate(ticker_list):
      if count == 25:
         break
      
      url = get_url(ticker.ticker, ticker.count, total_mentions)
 
      text += f"\n{ticker.show(url)}"
   return(text)
