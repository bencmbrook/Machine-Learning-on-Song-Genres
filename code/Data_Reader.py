import pyen
import os

SONGS_PER_GENRE = 3 # Up to 100 songs per genre. 100 songs per genre takes about 30 seconds so let it load.

os.environ["ECHO_NEST_API_KEY"] = "SRCGPBCAPG5FQQKFR"

EchoNest = pyen.Pyen()

def normalize(song_data):
	# Normalize time_signature and cast int to float
	if song_data['time_signature'] > 7:
		song_data['time_signature'] = 8.
	elif song_data['time_signature'] < 1:
		song_data['time_signature'] = 1.
	else:
		song_data['time_signature'] = float(song_data['time_signature'])
	# Make mode a float
	song_data['mode'] = float(song_data['mode'])
	# Normalize duration
	if song_data['duration'] > 7000.:
		song_data['duration'] = 7000.
	elif song_data['duration'] < 1.:
		song_data['duration'] = 1.
	# Normalize loudness
	if song_data['loudness'] > 5.:
		song_data['loudness'] = 5.
	elif song_data['loudness'] < -30.:
		song_data['loudness'] = -30.
	# Normalize tempo
	if song_data['tempo'] > 200.:
		song_data['tempo'] = 200.
	elif song_data['tempo'] < 0.:
		song_data['tempo'] = 0.

genres = ['blues', 'classical', 'electronic', 'hip hop', 'jazz', 'reggae', 'rock']


class Song
    def __init__(self, genre, data):
        self.data = data
        self.genre = genre
        
    def GetTruth(self):
        truth = []
        
        # convert the genre information into a vector of 0's, with a 1 in the position of the actual genre of the song
        for i, genre in enumerate(genres)
            if genre = self.genre
                truth[i] = 1
            else truth[i] = 0
        
        # return the vector.
        return truth
    
    def GetData(self):
        return self.data
    
def get_songs():
	Songs = []
    
    # iterate through the selected genres
	for genre in genres:
		tunes_of_genre = EchoNest.get('song/search', style=genre, bucket=['audio_summary'], results=SONGS_PER_GENRE)
        
        # iterate through each "tune" of the current genre
		for tune in tunes_of_genre['songs']:
			tune_data = tune['audio_summary']
            
			# Pop off unnecessary dictionary values
			for useless in ['analysis_url', 'audio_md5', 'key']: 
	  			tune_data.pop(useless)
                
            # normalize song_data
			normalize(tune_data)
            
            # construct the new songs from the ingredients we have
            new_song = Song.__init__(genre, song_data)
            
            # append it to our song list
			songs.append(new_song)
            
	return songs

print get_songs()

            
        
        


