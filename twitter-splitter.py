#!/usr/bin/env python3

import sys

TWEET_LENGTH = 280 - 6

input = open(sys.argv[1], 'r')
data = input.read()

def find_last_space(text):
    last_space = 0
    for i in range(0, len(text)):
        if text[i].isspace():
            last_space = i
    return last_space

tweets = []
count = 0
while True:
    tweet = ""
    if tweets:
        tweet += "... "
    last_space = find_last_space(data)
    ellipsis = False
    if last_space > TWEET_LENGTH:
         last_space = find_last_space(data[:TWEET_LENGTH])
         ellipsis = True
    tweet += data[:last_space]
    if ellipsis:
        tweet += " ..."
    tweets.append(tweet.strip())
    data = data[last_space:]
    count += 1
    if not data.strip():
        break

if len(tweets) == 1:
    print(tweets[0])
    print('------------------------------')
else:
    for tweet in tweets:
        print(tweet)
        print('------------------------------')
