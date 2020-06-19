import tweepy

# The key and tokens are necessary for authentication and security
api_key = "yourKey"
api_secret_key = "yourSecretKey"

access_token = "yourToken"
token_secret = "yourTokeSecretValue"

# Authorise using the credentials
authorization = tweepy.OAuthHandler(api_key, api_secret_key)
authorization.set_access_token(access_token, token_secret)

api = tweepy.API(authorization)

# Start your analysis
tweets = api.home_timeline()
for tweet in tweets:
    print("================")
    print(tweet.text)

username = api.get_user('someOtherUsername')
print(username.screen_name)
print(username.followers_count)
for friend in username.friends():
    print(friend.screen_name)

# For further analysis and understanding

# To analyze each user in your account
# for friend in tweepy.Cursor(api.friends).items():
#     friend_analysis(friend)

# To analyze 10 tweets on your timeline

# numberOfTweetssToAnalyze = 10

# for tweet in tweepy.Cursor(api.home_timeline).items(numberOfTweetsToAnalyze):
#     sentiment_analysis(tweet)

