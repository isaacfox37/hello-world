import requests
import json
import pandas as pd
from twython import Twython
import pprint

# Twitter API Credentials

credentials = {}
credentials['CONSUMER_KEY'] = 'VcRa3mclbZCNnMjFnJP0nsHgH'
credentials['CONSUMER_SECRET'] = 'gSDOTH2PykumBCN4jwyVcxzYNwDNcY90FnEQqTcwQqqXgiodsg'
credentials['ACCESS_TOKEN'] = '254123557-DGI4EE5ybr5HfJ1FyJEsmNCKBtNuMY9aJYsUZEGV'
credentials['ACCESS_SECRET'] = 'tdAJmIFkNbQcDVPokZe1tvw40tsjWONtIiGUMzGsoayjw'

# save credentials to a file
with open('twitter_credentials.json', "w") as file:
    json.dump(credentials, file)


# Retrieve Twitter Credentials

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
# full list of parameters here https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
query = {'q': ['trump', 'obama'],
         'result_type': 'popular',
         'count': 10,
         'lang': 'en',
         }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df.iloc[:, 1:3])

raw_data = python_tweets.search(**query)

# pprint.pprint(raw_data)

dates = df['date']
print(dates)

data = raw_data['statuses']

# pprint.pprint(data)

for i in data:
    print(i['user']['screen_name'] + " - favorites: " + str(i['user']['favourites_count']))




