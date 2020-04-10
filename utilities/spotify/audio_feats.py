# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import pandas as pd

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False


list_songs = ["La vida es un carnaval",
              "i took a pill in ibiza",
              "not afraid",
              "Shape of you",
              "Happy pharrel",
              "Over the rainbow"
              ]



names = []
artists = []
popularitys = []
danceabilitys = []
energys = []
loudnesss = []
modes = []
speechinesss = []
acousticnesss = []
instrumentalnesss = []
livenesss = []
valences = []
tempos = []





for query in list_songs:
    results = sp.search(q=query, limit=1)
    print(results)
    print("**********")
    names.append(results["tracks"]["items"][0]["name"])

    artist_list = [t["name"] for t in results["tracks"]["items"][0]["artists"]]
    artists.append(artist_list)
    
    popularitys.append(results["tracks"]["items"][0]["popularity"])

    tids = results["tracks"]["items"][0]["uri"]
    features = sp.audio_features(tids)[0]

    danceabilitys.append(features["danceability"]*100)
    energys.append(features["energy"]*100)
    loudnesss.append(features["loudness"])
    modes.append(features["mode"])
    speechinesss.append(features["speechiness"]*100)
    acousticnesss.append(features["acousticness"]*100)
    instrumentalnesss.append(features["instrumentalness"]*100)
    livenesss.append(features["liveness"]*100)
    valences.append(features["valence"]*100)
    tempos.append(features["tempo"])
    
df = pd.DataFrame({
    "name" : names,
    "artist" : artists,
    "popularity" : popularitys ,
    "danceability" : danceabilitys,
    "energy" : energys,
    "loudness" : loudnesss,
    "mode" : modes,
    "speechiness" : speechinesss,
    "acousticness" : acousticnesss,
    "instrumentalness" : instrumentalnesss,
    "liveness" : livenesss,
    "valence" : valences,
    "tempo" : tempos
})
    
df.to_csv("audio_features.csv", index=False)