from wallstreetBetsAnalyser import run

if __name__ == "__main__":
   number_of_posts = 10
   reddit_sub = "wallstreetbets"

   resval = run(reddit_sub, number_of_posts)
   print(resval)