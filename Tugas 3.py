# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:24:09 2019

@author: Laura Natalia
"""

import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'eNly7n62NgPBr1cwUUsLDXvWN'
consumer_secret = 'iHPbHMLum74zSFz0NCwERWnnw0ZCfR4bGCMuUIDSE3czlDY9Sq'
access_token = '702183804-JvE0qIBEvqfv5Al3KGuEVsbhbyhRVhLn4kqJ5KN9'
access_token_secret = 'WoXhuxup1EpbFXS8O3McBABteUvcPvyerOyrNNNjGmD3f'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth,wait_on_rate_limit=True)

# Membuat list dengan nama hastags yang berisi 5 keywords
hashtags = ["Jerome Polin","Fiersa Besari","Stephanie Poetri","Angela Tanoesoedibjo","Rachel Venya"]

# Mencari tweet dengan topik yang ada pada hastags dengan jumlah 200, mencari tweet dengah bahasa indonesia dengan range waktu tertentu
for hashtag in hashtags:
    for tweet in tweepy.Cursor(api.search,q=hashtag, count=200, lang="id", since="2019-10-23", until="2019-10-24").items():
        print (tweet.created_at, tweet.text)
