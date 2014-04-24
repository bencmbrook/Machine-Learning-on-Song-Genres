from pyechonest import config
config.ECHO_NEST_API_KEY="SRCGPBCAPG5FQQKFR"

from pyechonest import artist
bk = artist.Artist('bikini kill')
print "Artists similar to: %s:" % (bk.name,)
for similar_artist in bk.similar: print "\t%s" % (similar_artist.name,)



genres = []


song = (genre, {'danceability': danceability, 'energy': energy, 'tempo': tempo, 'loudness': loudness, 'time_signature': time_signature, 'duration': duration, 'mode': mode})