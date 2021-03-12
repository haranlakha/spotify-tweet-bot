# Spotify Tweet Bot
This is a Spotify Tweet Bot which gets your currently playing song from Spotify and tweets it to your Twitter account.

# Installation
Clone this repository or download the .zip file.

Once it has downloaded you will need to add your own authentication keys and tokens to the SpotifyCredentials.py and TwitterCredentials.py files

The authentication tokens and keys for Spotify can be found when you create an app on https://developer.spotify.com/

The authentication tokens and keys for Twitter can be found when you create an app on https://developer.twitter.com/

You will need to import [Tweepy](https://www.tweepy.org/) and [Spotipy](https://spotipy.readthedocs.io/en/latest/#installation) to run this program.

As there is a problem with the current build of spotipy you will also need to run this command to get the latest build:

pip3 install git+https://github.com/plamere/spotipy.git --upgrade

This will eliminate any attribute errors when getting the user playback.

# Running the program

Run with: python3 SpotifyTweet.py

## Author

* **Haran Lakha** - [GitHub](https://github.com/haranlakha) - [Twitter](https://twitter.com/haranlakha)
