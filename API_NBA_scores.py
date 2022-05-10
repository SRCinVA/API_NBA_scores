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
    data = get(BASE_URL + stats).json()

    printer.pprint(data)

get_stats()
