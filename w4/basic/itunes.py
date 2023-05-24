import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Invalid Arguments")

#lets user choose which artist's song to search for
artist = requests.get("https://itunes.apple.com/search?entity=song&limit=6&term=" + sys.argv[1])



#artist.json()  format the data got back in artist into JSON format
#json.dumps is to pretty print the output(indent etc)
#print(json.dumps   (artist.json(), indent=2)    )


#print specific key
output = artist.json()
for result in output["results"]:   #result is the dict in the list
    print(result["trackName"])