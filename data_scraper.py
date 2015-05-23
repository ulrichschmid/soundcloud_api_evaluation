__author__ = 'Ulrich'

import soundcloud

SOUNDCLOUD_CLIENT = soundcloud.Client(client_id="YOUR_CLIENT_ID")

def resolve_artist_url(url):
    return SOUNDCLOUD_CLIENT.get("/resolve", url=url).id

def get_artist_tracks(artist_id):
    return SOUNDCLOUD_CLIENT.get("/users/"+str(artist_id)+"/tracks")

def get_artist_followers(artist_id):
    return SOUNDCLOUD_CLIENT.get("/users/"+str(artist_id)+"/followers")


artist_id = resolve_artist_url("https://soundcloud.com/die-lochis")


for follower in get_artist_followers(artist_id):
    print follower.username