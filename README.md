# twitter-bot
A Python script for a simple Twitter bot that replies to an account that posts songs lyrics hourly with the song the lyrics are from. 
The script uses the Tweepy library to to simplify the Twitter API v2 and OAuth 2.0, while utilizing the Genius API for lyrics queries.

<!-- GETTING STARTED -->
## Getting Started
Only the external Tweepy library and your Twitter/Genius API keys are required to run this script.

### Prerequisites

You will want to install the latest Tweepy module using
```sh
pip install tweepy
```

### Installation

1. Obtain your Twitter API keys at [https://developer.twitter.com](https://developer.twitter.com) and your Genius API keys at [https://docs.genius.com/](https://docs.genius.com/)
2. Clone the repo
   ```sh
   git clone https://github.com/krissowat/twitter-bot.git
   ```
3. Install the Tweepy library
   ```sh
   pip install tweepy
   ```
4. Enter your respective API Keys in `src.py`

   Twitter:
   ```py
   bearer_token = '------------INSERT BEARER TOKEN HERE------------'
   consumer_key = '------------INSERT CONSUMER KEY HERE------------'
   consumer_secret = '------------INSERT CONSUMER SECRET HERE------------'
   access_token = '------------INSERT ACCESS TOKEN HERE------------'
   access_token_secret = '------------INSERT ACCESS TOKEN SECRET HERE------------'
   ```
   Genius:
   ```py
   client_access_token = '------------INSERT CLIENT ACCESS TOKEN HERE------------'
   ```
5. Run the `src.py` script, which can be run within your IDE or through a hosting service

   <!-- USAGE EXAMPLES -->
## Usage

As of February 9th, 2023, Twitter will be removing its free API access and will require users to pay fee(s) to access the API and post tweets.

I used this script for the twitter account [@mitskibotlyrics](https://twitter.com/mitskibotlyrics) and ran it using AWS Glue and a Raspberry Pi.


This script can be run hourly using cron expressions, such as `13 0/1 * * ? *`

![image](https://user-images.githubusercontent.com/90125291/216881899-16f3c0f5-e581-421a-b5f5-f0c692b7542b.png)


_For information about API usage, please refer to the Genius and Twitter API Documentation and respect their API policies._
