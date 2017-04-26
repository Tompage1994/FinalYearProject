These are the files used within my final year project.

The programs within this repository are as follows:

|File                    | Description
|:-----------------------:|:-------------------:|
|article_ts.py           | Creates a time series of the frequency of all articles for each outlet|
|brexitArticles.py       | Filters out all of the non relevant articles and saves relevant ones to a file|
|brexitTweets.py         | Filters out all of the non relevant tweets and saves relevant ones to a file|
|keywords_articles.py    | Creates a time series of the frequency of usage of a number of keywords in articles across a year for all outlets|
|keywords_twitter.py     | Creates a time series of the frequency of usage of a number of keywords in tweets across a year|
|sentimentArticles.py    | Adds labels of the sentiment for each of the articles outputted by brexitArticles.py|
|sentimentTweets.py      | Adds labels of the sentiment for each of the tweets outputted by brexitTweets.py|
|sentiment_article_ts.py | Uses the output of sentimentArticles.py to generate a time series of mean hourly sentiment for each outlet across a year|
|sentiment_ts.py         | Uses the output of sentimentTweets.py to generate a time series of mean hourly sentiment across a year|
|wordmatrix.py           | Generates a vector space model for each day of the year|

A further description of each piece of code can be found within the program itself.
