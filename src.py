import tweepy
import urllib.request
import urllib.parse
import json

bearer_token = '------------INSERT BEARER TOKEN HERE------------'
consumer_key = '------------INSERT CONSUMER KEY HERE------------'
consumer_secret = '------------INSERT CONSUMER SECRET HERE------------'
access_token = '------------INSERT ACCESS TOKEN HERE------------'
access_token_secret = '------------INSERT ACCESS TOKEN SECRET HERE------------'

#Create a Tweepy Client
client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)

# Define a user to check tweets from
target_username = 'MITSKILYRICSBOT'
target_ID = id=870648949983637505

# Function to find song and album using song lyrcs
def find_song_title(lyrics: str):
    client_access_token = '------------INSERT CLIENT ACCESS TOKEN HERE------------'
    song_lyrics = lyrics.replace('\n', ' ')
    if len(song_lyrics)>70:
        song_lyrics = song_lyrics[0:70]
    encoding = urllib.parse.urlencode([('access_token', client_access_token), ('q', 'mitski ' + song_lyrics)])
    url = 'https://api.genius.com/search?'
    search_url = url + encoding
    request = urllib.request.Request(search_url)
    response = urllib.request.urlopen(request)
    data = response.read()
    response.close()
    data = json.loads(data)
    return data['response']['hits'][0]['result']['title']

#Get the tweets from the user
tweets = client.get_users_tweets(id=870648949983637505)
tweet = tweets.data[0]
tweet_id = tweet.id

#Find the latest tweet and reply to it with the song title
lyrics = tweets.data[0]
song_title = find_song_title(str(lyrics))

reply_text = f'These lyrics are from her song "{song_title}"'

try:
    if client.create_tweet(in_reply_to_tweet_id = tweet_id, text=reply_text):
        print('Posted')
except tweepy.errors.TweepyException as e:
    print(e)