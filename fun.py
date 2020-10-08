import requests
import discord
from datetime import date
from tabulate import tabulate

uri = 'https://api.football-data.org/v2/'
headers = {'X-Auth-Token': '',
           'Accept-Encoding': ''}
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# function to determine which competitions are free tiers


def free_tier(uri, headers):
    response = requests.get('{}/competitions'.format(uri), headers=headers)
    data = response.json()
    free_leagues = {}
    for i in data['competitions']:
        if i['plan'] == "TIER_ONE":
            free_leagues[i['name']] = ([i['area']['name'], i['id']])
    return free_leagues


# for standings
def league_standings(uri, headers, league):

    available = free_tier(uri, headers)

    standings = requests.get(
        '{}/competitions/{}/standings'.format(uri, available[league][1]), headers=headers)
    standings = standings.json()
    final = []
    for team in standings['standings'][0]['table']:
        final.append((team['position'], team['team']
                      ['name'], team['playedGames'], team["won"], team["draw"], team["lost"], team["points"]))
    headers = ['', '', 'GP', 'W', 'D', 'L',
               'Points']
    return (tabulate(final, headers))


@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content.startswith('$EPL-standings'):
        a = league_standings(uri, headers, "Premier League")
        await message.channel.send('The standings as of {}'.format(date.today()))
        await message.channel.send("```{}```".format(a))

    if message.content.startswith('$Bundesliga-standings'):
        a = league_standings(uri, headers, "Bundesliga")
        await message.channel.send('The standings as of {}'.format(date.today()))
        await message.channel.send("```{}```".format(a))

    if message.content.startswith('$Championship-standings'):
        a = league_standings(uri, headers, "Championship")
        await message.channel.send('The standings as of {}'.format(date.today()))
        await message.channel.send("```{}```".format(a))

    if message.content.startswith('$Ligue1-standings'):
        a = league_standings(uri, headers, "Ligue 1")
        await message.channel.send('The standings as of {}'.format(date.today()))
        await message.channel.send("```{}```".format(a))

    if message.content.startswith('$SerieA-standings'):
        a = league_standings(uri, headers, "Serie A")
        await message.channel.send('The standings as of {}'.format(date.today()))
        await message.channel.send("```{}```".format(a))

    if message.content.startswith('$Eredivisie-standings'):
        a = league_standings(uri, headers, "Eredivisie")
        await message.channel.send('The standings as of {}'.format(date.today()))
        await message.channel.send("```{}```".format(a))

    if message.content.startswith('$LaLiga-standings'):
        a = league_standings(uri, headers, "Primera Division")
        await message.channel.send('The standings as of {}'.format(date.today()))
        await message.channel.send("```{}```".format(a))

    if message.content.startswith('$PrimeiraLiga-standings'):
        a = league_standings(uri, headers, "Primera Liga")
        await message.channel.send('The standings as of {}'.format(date.today()))
        await message.channel.send("```{}```".format(a))


client.run("")
