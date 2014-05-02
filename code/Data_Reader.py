import pyen
import os
import math
import random

SONGS_PER_GENRE = 10 # Up to 100 songs per genre. 100 songs per genre takes about 30 seconds so let it load.

os.environ["ECHO_NEST_API_KEY"] = "SRCGPBCAPG5FQQKFR"

EchoNest = pyen.Pyen()

def sigmoid(data, stretch=1, midpoint=0):
    return 1 / (1 + math.exp(-1*stretch*(data-midpoint)))

def normalize(song_data):

    # Normalize time_signature
    song_data['time_signature'] = song_data['time_signature']/7

    # Normalize duration
    song_data['duration'] = sigmoid(song_data['duration'])

    # Normalize loudness
    song_data['loudness'] = sigmoid(song_data['loudness'])

    # Normalize tempo
    song_data['tempo'] = sigmoid(song_data['tempo'])

    
genres = ['blues', 'classical', 'electronic', 'hip hop', 'jazz', 'reggae', 'rock']

class Song:
    def __init__(self, genre, data):
        self.data = data
        self.genre = genre
        
    def GetTruth(self):
        truth = []
        
        # convert the genre information into a vector of 0's, with a 1 in the position of the actual genre of the song
        for genre in genres:
            if genre == self.genre:
                truth.append(1)
            else: truth.append(0)
        
        # return the vector.
        return truth
    
    def GetData(self):
        return self.data
    
def get_songs():
    songs = []
    
    # iterate through the selected genres
    for genre in genres:
        tunes_of_genre = EchoNest.get('song/search', style=genre, bucket=['audio_summary'], results=SONGS_PER_GENRE)
        
        # iterate through each "tune" of the current genre
        for tune in tunes_of_genre['songs']:
            tune_data = tune['audio_summary']

            # pop off unnecessary dictionary values
            for useless in ['analysis_url', 'audio_md5', 'key']:
                tune_data.pop(useless)

            # normalize the dictionary values
            normalize(tune_data)

            # construct the new songs from the ingredients we have
            new_song = Song(genre, tune_data.values())

            # append it to our song list
            songs.append(new_song)

    return songs



def get_data(songs):
    data_list = []

    for i in range(0, len(songs)):
        data = songs[i].GetData()
        data_list.append(data)

    return data_list

def get_truth(songs):
    truth_list = []

    for i in range(0, len(songs)):
        truth = songs[i].GetTruth()
        truth_list.append(truth)

    return truth_list



print(len(get_songs()))


