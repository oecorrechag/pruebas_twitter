import pandas as pd
import tweepy
from secrets_key import MY_BEARER_TOKEN

# create your client 
client = tweepy.Client(bearer_token=MY_BEARER_TOKEN)

# query = "#FestivalCordillera lang:es -is:retweet"
# query = "#covid19 lang:en -is:retweet"
# query = "#Rihanna lang:es -is:retweet"
# query = "Mario Bros (happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely OR incredible) lang:es -is:retweet"
# query = "Mario Bros -is:retweet"
# query = "musica colombiana lang:es"
query = "musica colombiana"

# your start and end time for fetching tweets
start_time = '2023-02-01T00:00:00Z'
end_time = "2023-02-25T00:00:00Z"
# get tweets from the API
tweets = client.search_recent_tweets(query=query,
                                     start_time=start_time,
                                     end_time=end_time,
                                     tweet_fields = ["author_id", "created_at", "text", "source", "geo", "lang"],
                                     user_fields = ["name", "username", "location", "verified", "description", "profile_image_url"],
                                     max_results = 10000,
                                     # place_fields = ['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id', 'name', 'place_type'],
                                     expansions= 'author_id',  #['author_id', 'geo.place_id']
                                     )

# tweet specific info
print(len(tweets.data))
# user specific info
print(len(tweets.includes["users"]))

# first tweet
first_tweet = tweets.data[0]
dict(first_tweet)

# user information for the first tweet
first_tweet_user = tweets.includes["users"][0]
dict(first_tweet_user)

# create a list of records
tweet_info_ls = []
# iterate over each tweet and corresponding user details
for tweet, user in zip(tweets.data, tweets.includes['users']):
    tweet_info = {
        'author_id': tweet.author_id,
        'created_at': tweet.created_at,
        'text': tweet.text,
        'source': tweet.source,
        'geo': tweet.geo,
        'lang': tweet.lang,
        'name': user.name,
        'username': user.username,
        'location': user.location,
        'verified': user.verified,
        'description': user.description,
        'profile_image_url': user.profile_image_url,
    }
    tweet_info_ls.append(tweet_info)
# create dataframe from the extracted records
tweets_df = pd.DataFrame(tweet_info_ls)
# display the dataframe
print(tweets_df.head())

# tweets_df.to_csv('tweets_df.csv', encoding = 'utf-8-sig', index = False)
# tweets_df.to_csv('tweets_rihanna.csv', encoding = 'utf-8-sig', index = False)
# tweets_df.to_csv('tweets_marioBross.csv', encoding = 'utf-8-sig', index = False)
tweets_df.to_csv('tweets_musica.csv', encoding = 'utf-8-sig', index = False)