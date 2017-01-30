#
# Purpose: Using Python get the 95 (up to) most recent user 
#          handles who retweeted a tweet.
#
# Requires: 
#    - you to 'pip install python-twitter'
#    - a file id.txt with the id of the tweet you want the retweeters of
#    - a file credentials.json with Twitter dev user credentials in
#
# The id of a tweet is at the end of the URL when you view its detail
#   e.g. for https://twitter.com/GGCamden/status/826059923830214657
#        it is 826059923830214657
#
#  User credentials are obtained by registering an app at:
#       https://apps.twitter.com/
#
# The package python-twitter can be seen at:
#   https://github.com/bear/python-twitter
#
# I believe it uses https://dev.twitter.com/rest/reference/get/statuses/retweets/id
# for the calls to Twitter.
#

import twitter
import json

# load Twitter user credentials
with open('credentials.json') as data_file:    
    data = json.load(data_file)

# authenticate
api = twitter.Api(consumer_key=data["CONSUMER_KEY"],
                  consumer_secret=data["CONSUMER_SECRET"],
                  access_token_key=data["OAUTH_TOKEN"],
                  access_token_secret=data["OAUTH_SECRET"])

# get id from file
with open('id.txt') as f:
    post_id = f.read()

# get results (for some reason 100 returns 95 results!)
results = api.GetRetweets(post_id, count='100')

# print results
print([result._json.get("user").get("screen_name") for result in results])