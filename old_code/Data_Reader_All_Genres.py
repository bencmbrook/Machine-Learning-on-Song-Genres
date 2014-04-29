import pyen
import os

import csv

os.environ["ECHO_NEST_API_KEY"] = "SRCGPBCAPG5FQQKFR"

EchoNest = pyen.Pyen()

genres_response = EchoNest.get('genre/list')
genres = []
for genre in genres_response['genres']:
    genres.append(genre['name'])
genres = map(lambda x: x.encode('ascii'), genres)

# Open File
resultFyle = open("output.csv",'wb')

# Create Writer Object
wr = csv.writer(resultFyle, dialect='excel')

# Write Data to File
for item in genres:
     wr.writerow([item,])