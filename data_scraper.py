__author__ = 'Ulrich'

import soundcloud

SOUNDCLOUD_CLIENT = soundcloud.Client(client_id="f3d7bf9ecd30174aea387f4b15d48804")

def resolve_artist_url(url):
    return SOUNDCLOUD_CLIENT.get("/resolve", url=url).id

def get_artist_tracks(artist_id):
    track_count = get_artist(artist_id).track_count
    tracks = []
    while (len(tracks) < track_count):
        acc = []
        for track in SOUNDCLOUD_CLIENT.get("/users/"+str(artist_id)+"/tracks", offset=len(tracks)):
            acc += [track]
        tracks += acc
    return tracks

def get_artist(artist_id):
    return SOUNDCLOUD_CLIENT.get("/users/"+str(artist_id))

def get_artist_followers(artist_id):
    followers_count = get_artist(artist_id).followers_count
    followers = []
    while (len(followers) < followers_count):
        acc = []
        for follower in SOUNDCLOUD_CLIENT.get("/users/"+str(artist_id)+"/followers",offset=len(followers)):
            acc += [follower]
        followers += acc
    return followers

artist_urls = ["https://soundcloud.com/die-lochis"]

for url in artist_urls:
    artist_id = resolve_artist_url(url)
    artist = get_artist(artist_id)

    print "artist:", artist.username
    print "id:", artist_id
    followers = get_artist_followers(artist_id)

    follower_following_count = 0
    qualified_followers = 0
    for follower in followers:
        qualified_followers += 1 / follower.followings_count
        follower_following_count += follower.followings_count
    print "followers:", str(len(followers))
    print "followings per follower:", str(follower_following_count/len(followers))
    print "qualified followings:", str(qualified_followers)
