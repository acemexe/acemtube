import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import SpotifyOAuth

bilgiler = "https://acemtubesecrets.glitch.me/STYconfig.json"
try:
    secapi = requests.get(bilgiler)
    APIs = json.loads(secapi.content)
except:
    print("Offline!")


def spver():
    client_credentials_manager = SpotifyClientCredentials(APIs["spotify"]["client_id"], APIs["spotify"]["client_secret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spotify

def getIsim(playlistid):
    client_credentials_manager = SpotifyClientCredentials(APIs["spotify"]["client_id"], APIs["spotify"]["client_secret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    isim = spotify.playlist(playlistid)

    return isim
    
def getSarki(sarkiurl):
    client_credentials_manager = SpotifyClientCredentials(APIs["spotify"]["client_id"], APIs["spotify"]["client_secret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    isim = spotify.track(sarkiurl)

    return isim

def getAlbüm(albümurl):
    client_credentials_manager = SpotifyClientCredentials(APIs["spotify"]["client_id"], APIs["spotify"]["client_secret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    albüm = spotify.album(albümurl)

    return albüm

def getTracks(playlistURL, sarkisayisi):

    client_credentials_manager = SpotifyClientCredentials(APIs["spotify"]["client_id"], APIs["spotify"]["client_secret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    #obama loves acem
    print("PIRTLADIM LAN " + str(sarkisayisi))
    listeekleniyor = True
    kaydırma = 0
    sarkilar = []
    
    #while listeekleniyor:
        #results = spotify.playlist_items(limit=100, offset=kaydırma,  playlist_id=playlistURL)
        ##tracks = results['items']
        #print("Liste Hazırlanıyor, Kaydırma: " + str(kaydırma))
        ##while results['next']:
        ##    
        ##    results = sp.next(results)
        ##    tracks.extend(results['items'])
        #trackList = [];
#
        #for i in results["tracks"]["items"]:
#
        #    if (i["track"]["artists"].__len__() == 1):
#
        #        trackList.append(i["track"]["name"] + " - " + i["track"]["artists"][0]["name"])
#
        #    else:
        #        nameString = "";
        #        for index, b in enumerate(i["track"]["artists"]):
        #            nameString += (b["name"]);
#
        #            if (i["track"]["artists"].__len__() - 1 != index):
        #                nameString += ", ";
#
        #        trackList.append(i["track"]["name"] + " - " + nameString);
        #print("kaydırma: " + str(kaydırma) + str(trackList))
        #sarkilar += trackList
        #if sarkisayisi - (kaydırma + 100) < 0:
        #    kaydırma += 100 + (sarkisayisi - (kaydırma + 100))
        #else:
        #    kaydırma += 100
        #if sarkisayisi == kaydırma:
        #    break

    pl_id = playlistURL
    offset = 0
    while True:
        response = spotify.playlist_tracks(pl_id, offset=offset, limit=50000, additional_types=['track'])

        if len(response["tracks"]['items']) == 0:
            break
        
        #pprint(response['items'])
        
        offset = offset + len(response["tracks"]['items'])

        print(offset, "/", response["tracks"]['total'])

        trackList = [];
        for i in response["tracks"]["items"]:
            if (i["track"]["artists"].__len__() == 1):
                trackList.append(i["track"]["name"] + " - " + i["track"]["artists"][0]["name"] + " (audio)")
            else:
                nameString = "";
                for index, b in enumerate(i["track"]["artists"]):
                    nameString += (b["name"]);
                    if (i["track"]["artists"].__len__() - 1 != index):
                        nameString += ", ";
                
                trackList.append(i["track"]["name"] + " - " + nameString);
                
        print("kaydırma: " + str(offset) + str(trackList))
        sarkilar += trackList
        if sarkisayisi < 101:
            break
        
    sarkilarr = list(dict.fromkeys(sarkilar))
    print(sarkilarr)

    return sarkilarr;