import json
import requests
import sys

#if function for getting argument from user in terminal window
if len(sys.argv) != 2:
    sys.exit()

    
#assign response with the itunes' api plus the users argument in the terminal window
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

#store the result in a variable and print specific item from the list and dictionaries
X = response.json()
for result in X ["results"]:
    print(result["trackName"])