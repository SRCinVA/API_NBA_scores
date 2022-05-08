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
    data = get(BASE_URL + scoreboard).json()['games']

    printer.pprint(data) # print out the keys (it's a dictionary) because otherwise it's hard to read.

get_scoreboard()
