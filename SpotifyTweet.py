import spotipy
import spotipy.util as util
import tweepy

from SpotifyCredentials import *
from TwitterCredentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id=CLIENT_ID,
                                   client_secret=CLIENT_SECRET,
                                   redirect_uri=redirect_uri)

spotify = spotipy.Spotify(auth=token)

while True:
    try:
        current_track = spotify.current_user_playing_track()
        current_track_id = current_track['item']['id']

        if current_track_id is not None:
            api.update_status("Currently playing:" + '\n' + current_track['item']['artists'][0]['name'] + " - " +
                                                            current_track['item']['name'] + '\n' + str(
                                                            current_track['item']['external_urls']['spotify']) + '\n' + "#" + str(
                                                            current_track['item']['artists'][0]['name']).replace(" ", ""))
            break
        else:
            continue
    except spotipy.client.SpotifyException:
        token = util.prompt_for_user_token(username,
                                           scope,
                                           client_id=CLIENT_ID,
                                           client_secret=CLIENT_SECRET,
                                           redirect_uri=redirect_uri)

        spotify = spotipy.Spotify(auth=token)
    except (tweepy.TweepError, TypeError) as e:
        pass

while True:
    try:
        new_track = spotify.current_user_playing_track()
        new_track_id = new_track['item']['id']

        if current_track_id is not None and new_track_id != current_track_id:
            api.update_status("Currently playing:" + '\n' + new_track['item']['artists'][0]['name'] + " - " + 
                                                            new_track['item']['name'] + '\n' + str(
                                                            new_track['item']['external_urls']['spotify']) + '\n' + "#" + str(
                                                            new_track['item']['artists'][0]['name']).replace(" ", ""))
            current_track_id = new_track_id
        else:
            continue
    except spotipy.client.SpotifyException:
        token = util.prompt_for_user_token(username,
                                           scope,
                                           client_id=CLIENT_ID,
                                           client_secret=CLIENT_SECRET,
                                           redirect_uri=redirect_uri)

        spotify = spotipy.Spotify(auth=token)
    except (tweepy.TweepError, TypeError)as e:
        pass
