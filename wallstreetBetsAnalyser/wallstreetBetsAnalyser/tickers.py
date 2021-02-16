from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Ticker:
   """A class for handling Tickers and functions

    Args:
        ticker: the name of the ticker
        weight: can overide the ticker weight
   """
   def __init__(self,
               ticker: str,
               weight: int = 2):
      self.ticker = ticker
      self.count = 0
      self.bodies = []
      self.pos_count = 0
      self.neg_count = 0
      self.bullish = 0
      self.bearish = 0
      self.neutral = 0
      self.sentiment = 0
      self.weight = weight

   def analyze_sentiment(self):
      analyzer = SentimentIntensityAnalyzer()
      neutral_count = 0
      for text in self.bodies:
         sentiment = analyzer.polarity_scores(text)
         if (sentiment["compound"] > .005) or (sentiment["pos"] > abs(sentiment["neg"])):
            self.pos_count += 1
         elif (sentiment["compound"] < -.005) or (abs(sentiment["neg"]) > sentiment["pos"]):
            self.neg_count += 1
         else:
            neutral_count += 1

      self.bullish = int(self.pos_count / len(self.bodies) * 100)
      self.bearish = int(self.neg_count / len(self.bodies) * 100)
      self.neutral = int(neutral_count / len(self.bodies) * 100)
   
   @property
   def score(self):
      """Calculate the ticker score

      Returns:
         the a calculated score range (-1 to 1)
      """
      return (self.bullish - (self.bearish + self.neutral / self.weight)) / 100

   def show(self, url: str):
      """
      Returns a str containing relvant ticker data.

      Args:
        url: link to financial data on the ticker
      """
      return(f"{url} | {self.ticker} | {self.bullish} | {self.bearish} | {self.neutral} | {self.score}")

   def __str__(self) -> str:
      return(f"{self.ticker} | {self.bullish} | {self.bearish} | {self.neutral} | {self.score}")
