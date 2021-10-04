import pandas as pd

#!curl -O https://lp-prod-resources.s3.amazonaws.com/635/67812/2021-07-02-13-15-41/tweet_engagements.csv
  
df = pd.read_csv("tweet_engagements.csv")
df.describe()
