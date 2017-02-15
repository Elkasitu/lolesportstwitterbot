#! /usr/bin/python
# Author: Adrian Torres
# Date: 2017-02-15
# Version: 1.0

import twitter
import json


def main():

    with open('.auth', 'r') as f:
        auth_data = json.load(f)

    # Authentication data
    consumer_key = auth_data["consumer_key"]
    consumer_secret = auth_data["consumer_secret"]
    access_token_key = auth_data["access_token_key"]
    access_token_secret = auth_data["access_token_secret"]

    # Connect to the twitter API
    api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

    # Send a message!
    status = api.PostUpdate("My first tweet! Posted with the Twitter API by a bot!")

if __name__ == "__main__":
    main()
