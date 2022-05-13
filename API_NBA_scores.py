from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

# need this to make the output readable:
printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

# printer.pprint(scoreboard)

def get_scoreboard():
    scoreboard = get_links()['currentScoreboard'] # builds on the previous method
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:  # to pull these specific items out of the dictionary 
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']
        
        print("-----------------------------------------------")
        print(f"{home_team['triCode']} vs. {away_team['triCode']}")  # can drill into the data for more specific name
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{clock} - {period['current']}")

        # printer.pprint(game.keys()) # print out the keys (it's a dictionary) because otherwise it's hard to read.
        # break
def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams'] # note that the next is embedded in the previous.
            # last item in the dictionary has to be the variable name? Unclear ... 
    
    # to get them to present in the order of their rank 
    teams = list(filter(lambda x: x['name'] != "Team", teams)) # the lambda will run a function against every single element in "teams."
                                                                # if that function returns True, it will keep the element; if not, it will discard. We don't want to grab the filler "Team" dictionaries. 
                                                                # need to cast the filter as a list
    # next is to sort them acc. to rank and points:
    teams.sort(key=lambda x:int(x['ppg']['rank'])) # 'rank' is nested in the dict. 'ppg', which e are grabbing for each team and casting as an int. 
                                                    # key is necessary for .sort() to do its thing...

    for i, team in enumerate(teams): # now we can loop through each team to pick up the information below:
                        # not sure how enumerate works with this ...
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']  # if we drill down to 'avg', it cleans up the appearance considerably.
        print(f"{i + 1}. {name} - {nickname} - {ppg}")

get_stats()
