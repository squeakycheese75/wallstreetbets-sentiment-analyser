import re
import datetime
from .tickers import Ticker
from .exclusions import blacklist_words


def extract_ticker(body, start_index):
   """
   Given a starting index and text, this will extract the ticker, return None if it is incorrectly formatted.
   """
   count  = 0
   ticker = ""

   for char in body[start_index:]:
      # if it should return
      if not char.isalpha():
         # if there aren't any letters following the $
         if (count == 0):
            return None

         return ticker.upper()
      else:
         ticker += char
         count += 1

   return ticker.upper()

def parse_section(ticker_dict, body):
   """ Parses the body of each comment/reply """

   if '$' in body:
      index = body.find('$') + 1
      # print(body)
      word = extract_ticker(body, index)
      # if word:
      #    print(f"Post ticker count {len(word)}")
      if word and word not in blacklist_words:
        #  print(f"Looking up {word}")
         try:
            if word in ticker_dict:
               ticker_dict[word].count += 1
               ticker_dict[word].bodies.append(body)
         except Exception as  e:
            print(e)
   
   # checks for non-$ formatted comments, splits every body into list of words
   word_list = re.sub("[^\w]", " ",  body).split()
   for count, word in enumerate(word_list):
      # initial screening of words
      if word.isupper() and len(word) != 1 and (word.upper() not in blacklist_words) and len(word) <= 5 and word.isalpha():
         # sends request to IEX API to determine whether the current word is a valid ticker
         # if it isn't, it'll return an error and therefore continue on to the next word
         # add/adjust value of dictionary
         if word in ticker_dict:
            ticker_dict[word].count += 1
            ticker_dict[word].bodies.append(body)
         else:
            ticker_dict[word] = Ticker(word)
            ticker_dict[word].count = 1
            ticker_dict[word].bodies.append(body)

   return ticker_dict

def get_url(key, value, total_count):
   """
   Builds a urls for the ticker.
   """
   mention = ("mentions", "mention") [value == 1]
   if int(value / total_count * 100) == 0:
         perc_mentions = "<1"
   else:
         perc_mentions = int(value / total_count * 100)
   return "${0} | [{1} {2} ({3}% of all mentions)](https://finance.yahoo.com/quote/{0}?p={0})".format(key, value, mention, perc_mentions)

def get_date():
   """
   Returns a formatted date.
   """
   now = datetime.datetime.now()
   return now.strftime("%b %d, %Y")