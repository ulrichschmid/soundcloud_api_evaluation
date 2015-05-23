__author__ = 'Ulrich'

import soundcloud
import datetime

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

artist_urls = ["https://soundcloud.com/die-lochis",
               "https://soundcloud.com/joel-brandenstein",
               "https://soundcloud.com/joris-voorn",
               "https://soundcloud.com/minemusik",
               "https://soundcloud.com/adam-angst",
               "https://soundcloud.com/truemmer_official",
               "https://soundcloud.com/nessiberlin",
               "https://soundcloud.com/duerer-band",
               "https://soundcloud.com/moritzkraemer",
               "https://soundcloud.com/the-hirsch-effekt",
               "https://soundcloud.com/coppelius-hilft",
               "https://soundcloud.com/six-rockband",
               "https://soundcloud.com/hurricanedeanmusic"]

for url in artist_urls:
    artist_id = resolve_artist_url(url)
    artist = get_artist(artist_id)

    print "------------"
    print "artist:", artist.username

    followers = get_artist_followers(artist_id)
    follower_following_count = 0
    qualified_followers = 0
    for follower in followers:
        qualified_followers += 1 / follower.followings_count
        follower_following_count += follower.followings_count
    print "followers:", str(len(followers))
    print "followings per follower:", str(follower_following_count/len(followers))
    print "qualified followings:", str(qualified_followers)


    """
    tracks = get_artist_tracks(artist_id)
    print "tracks:" + str(len(tracks))
    for track in tracks:

        print "comments:",track.comment_count
        print "plays:",track.playback_count
        print "downloads:",track.download_count

        yr = track.release_year
        mt = track.release_month
        dy = track.release_day
        if yr is not None and mt is not None and dy is not None:
            uptime_days = (datetime.datetime.now() - datetime.datetime(yr, mt, dy)).days
            print "uptime days:",uptime_days
            print "average events(play,comment,download) per day:",str((track.comment_count+track.playback_count+track.download_count)/uptime_days)
        else:
            print "uptime of song not set"
    """