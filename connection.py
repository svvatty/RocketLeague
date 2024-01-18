#pyenv into this project
#git, gitignore
import requests
import json

#look into storing these in secrets 
headers = {"Authorization": "p3PT08nY9motwCZJ5uy5MxJK4CH0LuzyguZ2tomY"}

baseUrl = 'https://ballchasing.com/api/replays'


#param: filename of type string
#return: None
def get_all_replays(filename: str) -> None:
    url = f"{baseUrl}/"
    file = f"{filename}.json"

    try: 
        req = requests.get(url, headers=headers)
        response = req.json()

        #look into storing files in external location or database or even directory within project
        with open(file, 'w') as f:
            json.dump(response, f)
    except:
        print(f"{req.status_code}: Request was not successful for retrieving all data")
        
#param: player name of type string (default is Svvatty)
#return: None
def get_player_replays(player: str = "Svvatty") -> None:
    param = f"?player-name={player}"
    url = f"{baseUrl}{param}"
    file = f"{player}_Replays.json"

    try:
        req = requests.get(url, headers=headers)
        response = req.json()

        with open(file, 'w') as f:
            json.dump(response, f)
    except:
        print(f"{req.status_code}: Request was not successful for {player}'s all data")
        
#params: URI parameters
#return: int based off number of replays returned
def get_replays_param(**kwargs) -> int: 
#implement method for allowing users to use query paramters (ex: player-name, playlist, season)
#This method will return the number of games given the filters (query parameters)
    'https://ballchasing.com/api/replays?player-name=name1&player-name=name2'
    
    url = 'https://ballchasing.com/api/replays?'
    numParams = len(kwargs)
    print(numParams)
    ctr = 0

    if kwargs != None:
        for k, v in kwargs.items():
            #print(kwargs)
            print(k,v)
            url += f"{k}=" + v
            if ctr == numParams - 1:
                pass
            else:
                url += "&"
            ctr += 1

    print(url)

    try:
        req = requests.get(url, headers=headers)
        response = req.json()

        with open('filtered_data', 'w') as f:
            json.dump(response, f)
    except:
        print(f"{req.status_code}: Request was not successful for the parameterized request")

    return 0




#Maybe method for removing json files manually from project directory?

get_all_replays()
get_player_replays()
get_replays_param(**{'player-name': 'Svvatty', 'Rank':'Dizzy'})
    