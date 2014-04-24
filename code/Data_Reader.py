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

def get_songs():
	songs = []
	for genre in genres:
		songs_of_genre = EchoNest.get('song/search', style=genre, bucket=['audio_summary'], results=SONGS_PER_GENRE)
		for song in songs_of_genre['songs']:
			song_data = song['audio_summary']
			# Pop off unnecessary dictionary values
			for useless in ['analysis_url', 'audio_md5', 'key']: 
	  			song_data.pop(useless)
			normalize(song_data)
			songs.append((genre, song_data))
	return songs

print get_songs()


